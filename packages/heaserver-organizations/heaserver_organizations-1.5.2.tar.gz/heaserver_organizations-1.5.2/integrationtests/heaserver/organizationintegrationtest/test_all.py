from .testcase import TestCase
from heaserver.service.testcase.mixin import GetOneMixin, GetAllMixin, PostMixin, PutMixin, DeleteMixin
from unittest.mock import patch


class TestGet(TestCase, GetOneMixin):
    pass

class TestGetAll(TestCase, GetAllMixin):
    pass


class TestPost(TestCase, PostMixin):
    pass

async def _mock_update_group_membership(request, user, added_groups, deleted_groups, group_url_getter):
    pass

async def _mock_update_volumes_and_credentials(app, changed):
    pass

@patch('heaserver.organization.service._update_group_membership', _mock_update_group_membership)
@patch('heaserver.organization.service._update_volumes_and_credentials', _mock_update_volumes_and_credentials)
class TestPut(TestCase, PutMixin):
    pass


class TestDelete(TestCase, DeleteMixin):
    pass
