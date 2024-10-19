"""
The HEA Person Microservice is a wrapper around a Keycloak server for HEA to access user information. It accesses
Keycloak using an admin account. The default account is 'admin' with password of 'admin'. To configure this (and you
must do this to be secure!), add a Keycloak section to the service's configuration file with the following properties:
    Realm = the Keyclock realm from which to request user information.
    VerifySSL = whether to verify the Keycloak server's SSL certificate (defaults to True).
    Host = The Keycloak host (defaults to https://localhost:8444).
    Username = the admin account username (defaults to admin).
    Password = the admin account password.
    PasswordFile = the path to the filename with the password (overrides use of the PASSWORD property).

This microservice tries getting the password from the following places, in order:
    1) the KEYCLOAK_QUERY_USERS_PASSWORD property in the HEA Server Registry Microservice.
    2) the above config file.

If not present in any of those sources, a password of admin will be used.
"""
import logging

from heaserver.service import response, client
from heaserver.service.runner import init_cmd_line, routes, start, web
from heaserver.service.wstl import action, builder_factory, add_run_time_action
from heaserver.service import appproperty
from heaserver.service.heaobjectsupport import new_heaobject_from_type, type_to_resource_url
from heaserver.service.oidcclaimhdrs import SUB
from heaobject.error import DeserializeException
from heaobject.person import Group, Person, Role, decode_role, decode_group, encode_role
from heaobject.registry import Collection
from heaobject.keychain import Credentials
from heaobject.organization import Organization
from heaobject.volume import Volume
from heaobject.root import PermissionContext, DefaultPermissionGroup
from heaobject.settings import SettingsObject
from .keycloakmongo import KeycloakMongoManager
from heaobject.user import NONE_USER
from aiohttp import ClientResponseError, hdrs
from base64 import urlsafe_b64decode
from binascii import Error as B64DecodeError
from collections.abc import Mapping
from multidict import istr

MONGODB_PERSON_COLLECTION = 'people'


@routes.get('/ping')
async def ping(request: web.Request) -> web.Response:
    """
    For testing whether the service is up.

    :param request: the HTTP request.
    :return: Always returns status code 200.
    """
    return response.status_ok(None)


@routes.get('/people/me')
@action(name='heaserver-people-person-get-properties', rel='hea-properties')
@action(name='heaserver-people-person-get-self', rel='self', path='people/{id}')
@action(name='heaserver-people-person-get-organizations', rel='application/x.organization', path='organizations/')
@action(name='heaserver-people-person-get-volumes', rel='application/x.volume', path='volumes/')
@action(name='heaserver-people-person-get-desktop-object-actions', rel='application/x.desktopobjectaction', path='desktopobjectactions/')
async def get_me(request: web.Request) -> web.Response:
    """
    Gets the currently logged in person.

    :param request: the HTTP request.
    :return: the requested person or Not Found.
    ---
    summary: A specific person.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        person = await request.app[appproperty.HEA_DB].get_user(request, request.headers.get(SUB, NONE_USER))
    except ClientResponseError as e:
        if e.status == 404:
            person = None
        else:
            return response.status_generic(e.status, body=e.message)
    if person is not None:
        context = context = await _add_collection_run_time_actions(request, sub)
        return await response.get(request, person.to_dict(),
                                  permissions=await person.get_permissions(context),
                                  attribute_permissions=await person.get_all_attribute_permissions(context))
    else:
        return await response.get(request, None)


@routes.get('/people/{id}')
@action(name='heaserver-people-person-get-properties', rel='hea-properties')
@action(name='heaserver-people-person-get-self', rel='self', path='people/{id}')
@action(name='heaserver-people-person-get-organizations', rel='application/x.organization', path='organizations/')
@action(name='heaserver-people-person-get-volumes', rel='application/x.volume', path='volumes/')
@action(name='heaserver-people-person-get-desktop-object-actions', rel='application/x.desktopobjectaction', path='desktopobjectactions/')
async def get_person(request: web.Request) -> web.Response:
    """
    Gets the person with the specified id.
    :param request: the HTTP request.
    :return: the requested person or Not Found.
    ---
    summary: A specific person.
    tags:
        - heaserver-people
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        person = await request.app[appproperty.HEA_DB].get_user(request, request.match_info['id'])
    except ClientResponseError as e:
        if e.status == 404:
            person = None
        else:
            return response.status_generic(e.status, body=e.message)
    if person is not None:
        context = await _add_collection_run_time_actions(request, sub)
        return await response.get(request, person.to_dict(),
                                  permissions=await person.get_permissions(context),
                                  attribute_permissions=await person.get_all_attribute_permissions(context))
    else:
        return await response.get(request, None)


@routes.get('/people/byname/{name}')
@action(name='heaserver-people-person-get-self', rel='self', path='people/{id}')
async def get_person_by_name(request: web.Request) -> web.Response:
    """
    Gets the person with the specified id.
    :param request: the HTTP request.
    :return: the requested person or Not Found.
    ---
    summary: A specific person, by name.
    tags:
        - heaserver-people
    parameters:
        - $ref: '#/components/parameters/name'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        persons = await request.app[appproperty.HEA_DB].get_users(request, params={'name': request.match_info['name']})
        if persons:
            context: PermissionContext[Person] = PermissionContext(sub)
            first_person = persons[0]
            return await response.get(request, first_person.to_dict(),
                                      permissions=await first_person.get_permissions(context),
                                      attribute_permissions=await first_person.get_all_attribute_permissions(context))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        return response.status_generic(e.status, body=e.message)


@routes.get('/people')
@routes.get('/people/')
@action(name='heaserver-people-person-get-properties', rel='hea-properties')
@action(name='heaserver-people-person-get-self', rel='self', path='people/{id}')
@action(name='heaserver-people-person-get-organizations', rel='application/x.organization', path='organizations/')
@action(name='heaserver-people-person-get-volumes', rel='application/x.volume', path='volumes/')
@action(name='heaserver-people-person-get-desktop-object-actions', rel='application/x.desktopobjectaction', path='desktopobjectactions/')
async def get_all_persons(request: web.Request) -> web.Response:
    """
    Gets all persons.
    :param request: the HTTP request.
    :return: all persons.
    ---
    summary: All persons.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    try:
        persons = await request.app[appproperty.HEA_DB].get_users(request)
        context = await _add_collection_run_time_actions(request, sub)
        return await response.get_all(request, [person.to_dict() for person in persons],
                                      permissions=[await person.get_permissions(context) for person in persons],
                                      attribute_permissions=[await person.get_all_attribute_permissions(context) for person in persons])
    except ClientResponseError as e:
        return response.status_generic(e.status, body=e.message)

@routes.get('/roles')
@routes.get('/roles/')
@action(name='heaserver-people-role-get-properties', rel='hea-properties')
@action(name='heaserver-people-role-get-self', rel='self', path='roles/{id}')
async def get_all_roles(request: web.Request) -> web.Response:
    """
    Gets all roles that are known to Keycloak.
    :param request: the HTTP request.
    :return: all roles.
    ---
    summary: All roles.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    try:
        roles = await request.app[appproperty.HEA_DB].get_all_roles(request)
        context: PermissionContext[Role] = PermissionContext(sub)
        return await response.get_all(request, [role.to_dict() for role in roles],
                                      permissions=[await role.get_permissions(context) for role in roles],
                                      attribute_permissions=[await role.get_all_attribute_permissions(context) for role in roles])
    except ClientResponseError as e:
        if e.status == 404:
            return await response.get_all(request, [])
        else:
            return response.status_generic(e.status, body=e.message)


@routes.get('/roles/{id}')
@action(name='heaserver-people-role-get-properties', rel='hea-properties')
@action(name='heaserver-people-role-get-self', rel='self', path='roles/{id}')
async def get_role(request: web.Request) -> web.Response:
    """
    Gets the requested role.

    :param request: the HTTP request. Requires an Authorization header with a valid Bearer token, in
    addition to the usual OIDC_CLAIM_sub header.
    :return: all roles.
    ---
    summary: All roles.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    id_ = request.match_info['id']
    try:
        roles = await request.app[appproperty.HEA_DB].get_all_roles(request)
        role = next((role for role in roles if role.id == id_), None)
        if role is not None:
            context: PermissionContext[Role] = PermissionContext(sub)
            return await response.get(request, role.to_dict(),
                                      permissions=await role.get_permissions(context),
                                      attribute_permissions=await role.get_all_attribute_permissions(context))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)


@routes.get('/roles/byname/{name}')
async def get_role_by_name(request: web.Request) -> web.Response:
    """
    Gets the requested role. Requires an Authorization header with a valid Bearer token, in
    addition to the usual OIDC_CLAIM_sub header.

    :param request: the HTTP request.
    :return: all roles.
    ---
    summary: All roles.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    name = request.match_info['name']
    try:
        roles = await request.app[appproperty.HEA_DB].get_all_roles(request)
        role = next((role for role in roles if role.name == name), None)
        if role is not None:
            context: PermissionContext[Role] = PermissionContext(sub)
            return await response.get(request, role.to_dict(),
                                      permissions=await role.get_permissions(context),
                                      attribute_permissions=await role.get_all_attribute_permissions(context))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)

@routes.post('/roles/internal')
@routes.post('/roles/internal/')
async def create_role_internal(request: web.Request) -> web.Response:
    try:
        obj = await new_heaobject_from_type(request, Role)
    except DeserializeException as e:
        return response.status_bad_request(str(e))
    location = await request.app[appproperty.HEA_DB].create_role(request, obj.role)
    headers: Mapping[str | istr, str] = {hdrs.LOCATION: location}
    return web.HTTPCreated(headers=headers)


@routes.delete('/roles/internal/{id}')
async def delete_role_internal(request: web.Request) -> web.Response:
    await request.app[appproperty.HEA_DB].delete_role(request, decode_role(request.match_info['id']))
    return await response.delete(True)

@routes.delete('/roles/internal/byname/{name}')
async def delete_role_internal_byname(request: web.Request) -> web.Response:
    await request.app[appproperty.HEA_DB].delete_role(request, decode_role(request.match_info['name']))
    return await response.delete(True)


@routes.post('/groups/internal')
@routes.post('/groups/internal/')
async def create_group_internal(request: web.Request) -> web.Response:
    try:
        obj = await new_heaobject_from_type(request, Group)
    except DeserializeException as e:
        return response.status_bad_request(str(e))
    location = await request.app[appproperty.HEA_DB].create_group(request, obj)
    headers: Mapping[str | istr, str] = {hdrs.LOCATION: location}
    return web.HTTPCreated(headers=headers)


@routes.delete('/groups/internal/{id}')
async def delete_group_internal(request: web.Request) -> web.Response:
    await request.app[appproperty.HEA_DB].delete_group(request, request.match_info['id'])
    return await response.delete(True)

@routes.delete('/groups/internal/byname/{name}')
async def delete_group_internal_byname(request: web.Request) -> web.Response:
    await request.app[appproperty.HEA_DB].delete_group(request, decode_group(request.match_info['name']))
    return await response.delete(True)


@routes.get('/groups')
@routes.get('/groups/')
@action(name='heaserver-people-group-get-properties', rel='hea-properties')
@action(name='heaserver-people-group-get-self', rel='self', path='groups/{id}')
async def get_all_groups(request: web.Request) -> web.Response:
    """
    Gets all groups that are known to Keycloak.
    :param request: the HTTP request.
    :return: all groups.
    ---
    summary: All groups.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    try:
        groups = await request.app[appproperty.HEA_DB].get_all_groups(request)
        logger.debug('groups: %s', groups)
        context: PermissionContext[Group] = PermissionContext(sub)
        return await response.get_all(request, [group.to_dict() for group in groups],
                                      permissions=[await group.get_permissions(context) for group in groups],
                                      attribute_permissions=[await group.get_all_attribute_permissions(context) for group in groups])
    except ClientResponseError as e:
        if e.status == 404:
            return await response.get_all(request, [])
        else:
            return response.status_generic(e.status, body=e.message)


@routes.get('/groups/{id}')
@action(name='heaserver-people-group-get-properties', rel='hea-properties')
@action(name='heaserver-people-group-get-self', rel='self', path='groups/{id}')
async def get_group(request: web.Request) -> web.Response:
    """
    Gets the requested group. Requires an Authorization header with a valid Bearer token, in
    addition to the usual OIDC_CLAIM_sub header.

    :param request: the HTTP request.
    :return: all groups.
    ---
    summary: All groups.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    id_ = request.match_info['id']
    try:
        groups = await request.app[appproperty.HEA_DB].get_all_groups(request)
        group = next((group for group in groups if group.id == id_), None)
        if group is not None:
            context: PermissionContext[Group] = PermissionContext(sub)
            return await response.get(request, group.to_dict(),
                                      permissions=await group.get_permissions(context),
                                      attribute_permissions=await group.get_all_attribute_permissions(context))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)

@routes.get('/groups/byname/{name}')
async def get_group_by_name(request: web.Request) -> web.Response:
    """
    Gets the requested group. Requires an Authorization header with a valid Bearer token, in
    addition to the usual OIDC_CLAIM_sub header.

    :param request: the HTTP request.
    :return: all groups.
    ---
    summary: All groups.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    name = request.match_info['name']
    try:
        groups = await request.app[appproperty.HEA_DB].get_all_groups(request)
        group = next((group for group in groups if group.name == name), None)
        if group is not None:
            context: PermissionContext[Group] = PermissionContext(sub)
            return await response.get(request, group.to_dict(),
                                      permissions=await group.get_permissions(context),
                                      attribute_permissions=await group.get_all_attribute_permissions(context))
        else:
            return await response.get(request, None)
    except ClientResponseError as e:
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)

@routes.post('/people/internal/{person_id}/groups')
@routes.post('/people/internal/{person_id}/groups/')
async def post_user_group(request: web.Request) -> web.Response:
    logger = logging.getLogger(__name__)
    person_id = request.match_info['person_id']
    logger.debug('Adding group to user %s', person_id)
    try:
        obj = await new_heaobject_from_type(request, Group)
    except DeserializeException as e:
        return response.status_bad_request(str(e))
    logger.debug('Adding group %r to user %s', obj, person_id)
    if person_id == 'me':
        await request.app[appproperty.HEA_DB].add_current_user_to_group(request, obj.id)
    else:
        await request.app[appproperty.HEA_DB].add_user_to_group(request, person_id, obj.id)
    return await response.post(request, obj.id, 'groups')

@routes.get('/people/{person_id}/groups')
@routes.get('/people/{person_id}/groups/')
async def get_user_group(request: web.Request) -> web.Response:
    """
    Gets all groups for the current user.
    :param request: the HTTP request.
    :return: all groups.
    ---
    summary: All groups.
    tags:
        - heaserver-people
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    person_id = request.match_info['person_id']
    sub = request.headers.get(SUB, NONE_USER)
    try:
        if person_id == 'me':
            groups = await request.app[appproperty.HEA_DB].get_current_user_groups(request)
        else:
            groups = await request.app[appproperty.HEA_DB].get_user_groups(request, person_id)
        context: PermissionContext[Group] = PermissionContext(sub)
        return await response.get_all(request, [group.to_dict() for group in groups],
                                      permissions=[await group.get_permissions(context) for group in groups],
                                      attribute_permissions=[await group.get_all_attribute_permissions(context) for group in groups])
    except ClientResponseError as e:
        if e.status == 404:
            return await response.get_all(request, [])
        else:
            return response.status_generic(e.status, body=e.message)

@routes.delete('/people/{person_id}/groups/{id}')
async def delete_user_group(request: web.Request) -> web.Response:
    id_ = request.match_info['id']
    person_id = request.match_info['person_id']
    if person_id == 'me':
        result = await request.app[appproperty.HEA_DB].remove_current_user_group(request, id_)
    else:
        result = await request.app[appproperty.HEA_DB].remove_user_group(request, person_id, id_)
    return await response.delete(result)

@routes.delete('/people/{person_id}/groups/bygroup/{group}')
async def delete_group_by_group(request: web.Request) -> web.Response:
    group = request.match_info['group']
    person_id = request.match_info['person_id']
    if person_id == 'me':
        result = await request.app[appproperty.HEA_DB].remove_current_user_group_by_group(request, group)
    else:
        result = await request.app[appproperty.HEA_DB].remove_user_group_by_group(request, person_id, group)
    return await response.delete(result)

@routes.delete('/people/{person_id}/groups/byname/{name}')
async def delete_group_by_name(request: web.Request) -> web.Response:
    name = request.match_info['name']
    person_id = request.match_info['person_id']
    group = decode_group(name)
    if person_id == 'me':
        result = await request.app[appproperty.HEA_DB].remove_current_user_group_by_group(request, group)
    else:
        result = await request.app[appproperty.HEA_DB].remove_user_group_by_group(request, person_id, group)
    return await response.delete(result)

@routes.get('/people/internal/token')
async def get_token(request: web.Request) -> web.Response:
    logger = logging.getLogger(__name__)
    try:
        if logger.getEffectiveLevel() == logging.DEBUG:
            logger.debug('headers %s', request.headers)
        token = await request.app[appproperty.HEA_DB].get_keycloak_alt_access_token(request)
    except ClientResponseError as e:
        logger.exception('Got client response error')
        if e.status == 404:
            return response.status_not_found()
        else:
            return response.status_generic(e.status, body=e.message)
    except B64DecodeError as e:
        return response.status_not_found()
    return await response.get(request, token.to_dict())

def main() -> None:
    config = init_cmd_line(description='Read-only wrapper around Keycloak for accessing user information.',
                           default_port=8080)
    start(package_name='heaserver-people', db=KeycloakMongoManager, config=config, wstl_builder_factory=builder_factory(__package__))


async def _add_collection_run_time_actions(request: web.Request, sub: str) -> PermissionContext:
    collection_map: dict[str, Collection] = {}
    url = await type_to_resource_url(request, Collection)
    async for collection in client.get_all(request.app, url, Collection, headers={SUB: sub}):
        assert collection.collection_type_name is not None, 'collection.collection_type_name cannot be None'
        collection_map[collection.collection_type_name] = collection
    if collection_map.get(Credentials.get_type_name()):
        add_run_time_action(request, name='heaserver-people-person-get-credential-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.keychain.Credentials')
    if collection_map.get(Organization.get_type_name()):
        add_run_time_action(request, name='heaserver-people-person-get-organization-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.organization.Organization')
    if collection_map.get(SettingsObject.get_type_name()):
        add_run_time_action(request, name='heaserver-people-person-get-settings', rel='hea-system-menu-item hea-user-menu-item application/x.settingsobject application/x.collection', path='collections/heaobject.settings.SettingsObject')
    if collection_map.get(Volume.get_type_name()):
        add_run_time_action(request, name='heaserver-people-person-get-volumes-collection', rel='hea-system-menu-item application/x.collection', path='collections/heaobject.volume.Volume')
    return PermissionContext(sub)
