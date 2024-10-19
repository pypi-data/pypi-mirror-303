"""
Creates a test case class for use with the unittest library that is built into Python.
"""

from heaserver.service.testcase.microservicetestcase import get_test_case_cls_default
from heaserver.organization import service
from heaobject.user import NONE_USER
from heaserver.service.testcase.expectedvalues import Action
from datetime import datetime

db_store = {
    service.MONGODB_ORGANIZATION_COLLECTION: [
        {
            "id": "666f6f2d6261722d71757578",
            "instance_id": 'heaobject.organization.Organization^666f6f2d6261722d71757578',
            "source": None,
            'source_detail': None,
            "name": "Bob",
            "display_name": "Bob",
            "description": "Description of Bob",
            "owner": NONE_USER,
            "created": datetime(2021, 12, 2, 17, 31, 15, 630000),
            "modified": datetime(2021, 12, 2, 17, 31, 15, 630000),
            "invites": [],
            "shares": [],
            "derived_by": None,
            "derived_from": [],
            "principal_investigator_id": "23423DAFSDF12adfasdf3",
            "manager_ids": [],
            "member_ids": [],
            "admin_ids": [],
            'type': 'heaobject.organization.Organization',
            'mime_type': 'application/x.organization',
            'account_ids': [],
            'type_display_name': 'Organization',
            'member_group_ids': [],
            'manager_group_ids': [],
            'admin_group_ids': [],
            'collaborator_ids': []
        },
        {
            "id": "0123456789ab0123456789ab",
            "instance_id": 'heaobject.organization.Organization^0123456789ab0123456789ab',
            "source": None,
            'source_detail': None,
            "name": "Reximus",
            "display_name": "Reximus",
            "description": "Description of Reximus",
            "owner": NONE_USER,
            "created": datetime(2021, 12, 2, 17, 31, 15, 630000),
            "modified": datetime(2021, 12, 2, 17, 31, 15, 630000),
            "invites": [],
            "shares": [],
            "derived_by": None,
            "derived_from": [],
            "principal_investigator_id": "11234867890b0123a56789ab",
            "manager_ids": ["11234867890b0123a56789ab"],
            "member_ids": [],
            "admin_ids": [],
            'type': 'heaobject.organization.Organization',
            'mime_type': 'application/x.organization',
            'account_ids': [],
            'type_display_name': 'Organization',
            'member_group_ids': [],
            'manager_group_ids': [],
            'admin_group_ids': [],
            'collaborator_ids': []
        }
    ],
    'people': [{
        'id': '666f6f2d6261722d71757578',
        'created': None,
        'derived_by': None,
        'derived_from': [],
        'description': None,
        'display_name': 'Reximus',
        'invited': [],
        'modified': None,
        'name': 'reximus',
        'owner': NONE_USER,
        'shares': [],
        'source': None,
        'source_detail': None,
        'type': 'heaobject.person.Person',
        'version': None
    }, {
        'id': '0123456789ab0123456789ab',
        'created': None,
        'derived_by': None,
        'derived_from': [],
        'description': None,
        'display_name': 'Reximus Thomas',
        'invited': [],
        'modified': None,
        'title': 'Manager',
        'name': 'Reximus Thomas',
        'owner': NONE_USER,
        'shares': [],
        'source': None,
        'source_detail': None,
        'type': 'heaobject.person.Person',
        'version': None
    }]

}

TestCase = get_test_case_cls_default(coll=service.MONGODB_ORGANIZATION_COLLECTION,
                                     wstl_package=service.__package__,
                                     href='http://localhost:8080/organizations/',
                                     fixtures=db_store,
                                     get_actions=[Action(name='heaserver-organizations-organization-get-properties',
                                                         rel=['hea-properties']),
                                                  Action(name='heaserver-organizations-organization-get-open-choices',
                                                         url='http://localhost:8080/organizations/{id}/opener',
                                                         rel=['hea-opener-choices']),
                                                  Action(name='heaserver-organizations-organization-duplicate',
                                                         url='http://localhost:8080/organizations/{id}/duplicator',
                                                         rel=['hea-duplicator']),
                                                  Action(name='heaserver-organizations-organization-get-self',
                                                         url='http://localhost:8080/organizations/{id}',
                                                         rel=['self']),
                                                  Action(name='heaserver-organizations-organization-get-memberseditor',
                                                         url='http://localhost:8080/organizations/{id}/memberseditor',
                                                         rel=['hearesource-organizations-memberseditor'])
                                                  ],
                                     get_all_actions=[Action(name='heaserver-organizations-organization-get-properties',
                                                             rel=['hea-properties']),
                                                      Action(
                                                          name='heaserver-organizations-organization-get-open-choices',
                                                          url='http://localhost:8080/organizations/{id}/opener',
                                                          rel=['hea-opener-choices']),
                                                      Action(name='heaserver-organizations-organization-duplicate',
                                                             url='http://localhost:8080/organizations/{id}/duplicator',
                                                             rel=['hea-duplicator']),
                                                      Action(name='heaserver-organizations-organization-get-self',
                                                             url='http://localhost:8080/organizations/{id}',
                                                             rel=['self']),
                                                      Action(name='heaserver-organizations-organization-get-memberseditor',
                                                             url='http://localhost:8080/organizations/{id}/memberseditor',
                                                             rel=['hearesource-organizations-memberseditor'])
                                                      ],
                                     duplicate_action_name='heaserver-organizations-organization-duplicate-form')
