from heaobject.person import Person
from heaobject.user import NONE_USER, ALL_USERS, CREDENTIALS_MANAGER_USER

person1 = Person()
person2 = Person()
person1.from_dict({
    'id': 'system|none',
    'created': '2022-01-01T00:00:00',
    'derived_by': None,
    'derived_from': [],
    'description': None,
    'display_name': 'Reximus Max',
    'invites': [],
    'modified': None,
    'name': 'reximusmax',
    'owner': NONE_USER,
    'shares': [{
        'invite': None,
        'permissions': ['VIEWER'],
        'type': 'heaobject.root.ShareImpl',
        'user': ALL_USERS
    }, {
        'invite': None,
        'permissions': ['EDITOR'],
        'type': 'heaobject.root.ShareImpl',
        'user': CREDENTIALS_MANAGER_USER
    }],
    'source': None,
    'first_name': 'Reximus',
    'last_name': 'Max',
    'type': 'heaobject.person.Person',
    'version': None,
    'title': None,
    'phone_number': None,
    'preferred_name': None,
    'id_labs_collaborator': None,
    'id_labs_manage': None,
    'id_labs_member': None,
    'id_projects_collaborator': None,
    'email': None
})
person2.from_dict({
    'id': 'system|test',
    'created': '2022-01-01T00:00:00',
    'derived_by': None,
    'derived_from': [],
    'description': None,
    'display_name': 'Luximus Max',
    'invites': [],
    'modified': None,
    'name': 'luximusmax',
    'owner': NONE_USER,
    'shares': [{
        'invite': None,
        'permissions': ['VIEWER'],
        'type': 'heaobject.root.ShareImpl',
        'user': ALL_USERS
    }, {
        'invite': None,
        'permissions': ['EDITOR'],
        'type': 'heaobject.root.ShareImpl',
        'user': CREDENTIALS_MANAGER_USER
    }],
    'source': None,
    'first_name': 'Luximus',
    'last_name': 'Max',
    'type': 'heaobject.person.Person',
    'version': None,
    'title': None,
    'phone_number': None,
    'preferred_name': None,
    'id_labs_collaborator': None,
    'id_labs_manage': None,
    'id_labs_member': None,
    'id_projects_collaborator': None,
    'email': None
})
