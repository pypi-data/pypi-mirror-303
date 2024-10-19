"""
We can only test get-all because we have no way to know what user id will be generated by Keycloak. There is no way
to hard-code it.
"""
from aiohttp import web
from typing import Union, Type, Optional
from collections.abc import Mapping, Sequence
from heaobject.root import DesktopObject
from heaobject.registry import Collection
from heaserver.service import heaobjectsupport
async def _mock_type_to_resource_url(request: web.Request, type_or_type_name: Union[str, Type[DesktopObject]],
                                     parameters: Optional[Mapping[str, Union[Sequence[Union[int, float, complex, str]], Mapping[str, Union[int, float, complex, str]], tuple[str, Union[int, float, complex, str]], int, float, complex, str]]] = None,
                                     **kwargs: Union[Sequence[Union[int, float, complex, str]], Mapping[str, Union[int, float, complex, str]], tuple[str, Union[int, float, complex, str]], int, float, complex, str]) -> str:
    if type_or_type_name in (Collection, Collection.get_type_name()):
        return 'http://localhost:8080/collections'
    else:
        raise ValueError(f'Unexpected type {type_or_type_name}')
heaobjectsupport.type_to_resource_url = _mock_type_to_resource_url
from heaserver.service import client
from heaobject.keychain import Credentials
from heaobject.settings import SettingsObject
async def _mock_get_all(app, url, type_or_type_name, headers=None):
    coll = Collection()
    coll.collection_type_name = Credentials.get_type_name()
    yield coll
    coll1 = Collection()
    coll1.collection_type_name = SettingsObject.get_type_name()
    yield coll1
client.get_all = _mock_get_all
from .testcase import TestCase
from .permissionstestcase import PermissionsTestCase
from heaserver.service.testcase.mixin import GetAllMixin, PermissionsGetAllMixin


class TestGetAll(TestCase, GetAllMixin):
    pass


class TestGetAllWithBadPermissions(PermissionsTestCase, PermissionsGetAllMixin):
    """A test case class for testing GET all requests with bad permissions."""
    pass
