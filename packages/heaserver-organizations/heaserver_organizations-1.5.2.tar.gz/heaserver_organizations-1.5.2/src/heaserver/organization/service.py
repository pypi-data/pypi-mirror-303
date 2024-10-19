"""
The HEA Server Organization provides ...
"""
from aiohttp import ClientResponseError, hdrs
from heaobject.error import DeserializeException
from heaserver.service.runner import init_cmd_line, routes, start, web
from heaserver.service.db import mongo, mongoservicelib
from heaserver.service.wstl import builder_factory, action
from heaserver.service.appproperty import HEA_DB, HEA_CACHE
from heaserver.service.oidcclaimhdrs import SUB
from heaserver.service.heaobjectsupport import type_to_resource_url, new_heaobject_from_type, RESTPermissionGroup
from heaserver.service import response, client
from heaserver.service.messagebroker import publisher_cleanup_context_factory, subscriber_cleanup_context_factory
from heaserver.service.util import queued_processing
from heaobject.organization import Organization
from heaobject.account import Account, AWSAccount, AccountView
from heaobject.volume import AWSFileSystem, Volume
from heaobject.person import Person, Group, GroupType, AddingCollaborator, RemovingCollaborator
from heaobject.user import NONE_USER, CREDENTIALS_MANAGER_USER
from heaobject.root import Permission, ShareImpl, DesktopObjectDict, desktop_object_type_for_name, PermissionContext, desktop_object_from_dict, DesktopObject
from heaobject.keychain import Credentials
from collections.abc import AsyncGenerator, Sequence, Awaitable, Collection
from yarl import URL
from asyncio import gather, Lock
from itertools import chain
from functools import partial
from typing import Coroutine, Callable, Any
from multidict import MultiDict
from itertools import chain
import logging

MONGODB_ORGANIZATION_COLLECTION = 'organizations'

_logger = logging.getLogger(__name__)
_sub_header = {SUB: CREDENTIALS_MANAGER_USER}
_put_lock = Lock()

@routes.get('/organizationsping')
async def ping(request: web.Request) -> web.Response:
    """
    Checks if this service is running.

    :param request: the HTTP request.
    :return: the HTTP response.
    """
    return await mongoservicelib.ping(request)


@routes.get('/organizations/{id}')
@action('heaserver-organizations-organization-get-properties', rel='hea-properties')
@action('heaserver-organizations-organization-get-open-choices', rel='hea-opener-choices', path='organizations/{id}/opener')
@action('heaserver-organizations-organization-duplicate', rel='hea-duplicator', path='organizations/{id}/duplicator')
@action('heaserver-organizations-organization-get-self', rel='self', path='organizations/{id}')
@action('heaserver-organizations-organization-get-memberseditor', rel='hearesource-organizations-memberseditor', path='organizations/{id}/memberseditor')
async def get_organization(request: web.Request) -> web.Response:
    """
    Gets the organization with the specified id.
    :param request: the HTTP request.
    :return: the requested organization or Not Found.
    ---
    summary: A specific organization.
    tags:
        - heaserver-organizations-get-organization
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.get(request, MONGODB_ORGANIZATION_COLLECTION)

@routes.get('/organizations/{id}/memberseditor')
@action('heaserver-organizations-organization-edit-membership', rel='hea-properties')
@action('heaserver-organizations-organization-get-members', rel='application/x.person', path='organizations/{id}/members/')
async def get_organization_memberseditor(request: web.Request) -> web.Response:
    """
    Gets the organization with the specified id.
    :param request: the HTTP request.
    :return: the requested organization or Not Found.
    ---
    summary: A specific organization.
    tags:
        - heaserver-organizations-get-organization
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.get(request, MONGODB_ORGANIZATION_COLLECTION)


@routes.put('/organizations/{id}/memberseditor')
async def put_organization_memberseditor(request: web.Request) -> web.Response:
    """
    Updates the organization with the specified id.
    :param request: the HTTP request.
    :return: a Response object with a status of No Content or Not Found.
     ---
    summary: Organization updates
    tags:
        - heaserver-organizations-put-organization
    parameters:
        - $ref: '#/components/parameters/id'
    requestBody:
      description: An updated organization object.
      required: true
      content:
        application/vnd.collection+json:
          schema:
            type: object
          examples:
            example:
              summary: Organization example
              value: {
                "template": {
                  "data": [{
                    "name": "created",
                    "value": null
                  },
                  {
                    "name": "derived_by",
                    "value": null
                  },
                  {
                    "name": "derived_from",
                    "value": []
                  },
                  {
                    "name": "description",
                    "value": null
                  },
                  {
                    "name": "display_name",
                    "value": "Reximus Max"
                  },
                  {
                    "name": "invites",
                    "value": []
                  },
                  {
                    "name": "modified",
                    "value": null
                  },
                  {
                    "name": "name",
                    "value": "reximus"
                  },
                  {
                    "name": "owner",
                    "value": "system|none"
                  },
                  {
                    "name": "shares",
                    "value": []
                  },
                  {
                    "name": "source",
                    "value": null
                  },
                  {
                    "name": "version",
                    "value": null
                  },
                  {
                    "name": "aws_account_ids",
                    "value": ["1234", "5678"]
                  },
                  {
                    "name": "principal_investigator_id",
                    "value": "1",
                  },
                  {
                    "name": "admin_ids",
                    "value": ["1234", "5678"]
                  },
                  {
                    "name": "manager_ids",
                    "value": ["4321", "8765"]
                  },
                  {
                    "name": "member_ids",
                    "value": ["1", "2"]
                  },
                  {
                  "name": "id",
                  "value": "666f6f2d6261722d71757578"
                  },
                  {
                  "name": "type",
                  "value": "heaobject.organization.Organization"
                  }]
                }
              }
        application/json:
          schema:
            type: object
          examples:
            example:
              summary: Organization example
              value: {
                "id": "666f6f2d6261722d71757578",
                "created": null,
                "derived_by": null,
                "derived_from": [],
                "description": null,
                "display_name": "Reximus Max",
                "invites": [],
                "modified": null,
                "name": "reximus",
                "owner": "system|none",
                "shares": [],
                "source": null,
                "type": "heaobject.organization.Organization",
                "version": null,
                "aws_account_ids": ["1234", "5678"],
                "principal_investigator_id": "1",
                "admin_ids": ["1234", "5678"],
                "manager_ids": ["4321", "8765"],
                "member_ids": ["1", "2"]
              }
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    await _update_permissions(request)
    return await mongoservicelib.put(request, MONGODB_ORGANIZATION_COLLECTION, Organization)

@routes.get('/organizations/byname/{name}')
@action('heaserver-organizations-organization-get-self', rel='self', path='organizations/{id}')
async def get_organization_by_name(request: web.Request) -> web.Response:
    """
    Gets the organization with the specified id.
    :param request: the HTTP request.
    :return: the requested organization or Not Found.
    ---
    summary: A specific organization, by name.
    tags:
        - heaserver-organizations-get-organization-by-name
    parameters:
      - name: name
        in: path
        required: true
        description: The name of the organization.
        schema:
          type: string
        examples:
          example:
            summary: An organization name
            value: Bob

    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.get_by_name(request, MONGODB_ORGANIZATION_COLLECTION)


@routes.get('/organizations/byaccountid/{account_id}')
@action('heaserver-organizations-organization-get-self', rel='self', path='organizations/{id}')
async def get_organization_by_account_id(request: web.Request) -> web.Response:
    """
    Gets the organization with the specified account id.
    :param request: the HTTP request.
    :return: the requested organization or Not Found.
    ---
    summary: A specific organization, by account id.
    tags:
        - heaserver-organizations-get-organization-by-account-id
    parameters:
      - name: account_id
        in: path
        required: true
        description: An account id in the organization.
        schema:
          type: string
        examples:
          example:
            summary: An account id.
            value: 123456789

    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    async with mongo.MongoContext(request, None) as mongo_ctx:
        account_id = request.match_info['account_id']
        logger.debug('Looking for organization with account id %s for user %s', account_id, sub)
        result = await mongo_ctx.get(request, MONGODB_ORGANIZATION_COLLECTION,
                                     mongoattributes={'account_ids': account_id},
                                     sub=sub)
        logger.debug('Got organization %s', result)
        if result is not None:
            obj = desktop_object_from_dict(result)
            permitted = await obj.has_permissions(perms=RESTPermissionGroup.GETTER_PERMS,
                                                    context=PermissionContext[DesktopObject](sub=sub))
            if not permitted:
                return await response.get(request, None)
            context: PermissionContext[DesktopObject] = PermissionContext(sub)
            return await response.get(request, result,
                                      permissions=await obj.get_permissions(context),
                                      attribute_permissions=await obj.get_all_attribute_permissions(context))
        else:
            return await response.get(request, None)


@routes.get('/organizations')
@routes.get('/organizations/')
@action('heaserver-organizations-organization-get-properties', rel='hea-properties')
@action('heaserver-organizations-organization-get-open-choices', rel='hea-opener-choices', path='organizations/{id}/opener')
@action('heaserver-organizations-organization-duplicate', rel='hea-duplicator', path='organizations/{id}/duplicator')
@action('heaserver-organizations-organization-get-self', rel='self', path='organizations/{id}')
@action('heaserver-organizations-organization-get-memberseditor', rel='hearesource-organizations-memberseditor', path='organizations/{id}/memberseditor')
async def get_all_organizations(request: web.Request) -> web.Response:
    """
    Gets all organizations.
    :param request: the HTTP request.
    :return: all organizations.
    ---
    summary: All organizations.
    tags:
        - heaserver-organizations-get-all-organizations
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    logger = logging.getLogger(__name__)
    logger.debug('Getting all organizations...')
    sort = request.query.get('sort', None)
    if sort is None:
        sort_int = None
    else:
        if sort != 'asc' and sort != 'desc':
            return response.status_bad_request(f'sort may be asc or desc but was {sort}')
        sort_int = 1 if sort == 'asc' else -1
    get_all = partial(mongoservicelib.get_all, request, MONGODB_ORGANIZATION_COLLECTION)
    if sort_int is not None:
        get_all = partial(get_all, sort={'display_name': sort_int})
    return await get_all()


@routes.get('/organizations/{id}/duplicator')
@action(name='heaserver-organizations-organization-duplicate-form', path='organizations/{id}')
async def get_organization_duplicate_form(request: web.Request) -> web.Response:
    """
    Gets a form template for duplicating the requested organization.

    :param request: the HTTP request. Required.
    :return: the requested form, or Not Found if the requested organization was not found.
    """
    return await mongoservicelib.get(request, MONGODB_ORGANIZATION_COLLECTION)


@routes.post('/organizations/duplicator')
async def post_organization_duplicator(request: web.Request) -> web.Response:
    """
    Posts the provided organization for duplication.
    :param request: the HTTP request.
    :return: a Response object with a status of Created and the object's URI in the
    """
    return await mongoservicelib.post(request, MONGODB_ORGANIZATION_COLLECTION, Organization)


@routes.get('/organizations/{id}/accounts')
@routes.get('/organizations/{id}/accounts/')
async def get_organization_accounts(request: web.Request) -> web.Response:
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    org_dict = await mongoservicelib.get_dict(request, MONGODB_ORGANIZATION_COLLECTION)
    if org_dict is None:
        return response.status_not_found()
    org = Organization()
    org.from_dict(org_dict)
    account_ids = org.account_ids
    resource_url = await type_to_resource_url(request, AccountView)
    assert resource_url is not None, 'resource_url cannot be None'
    accounts: list[AccountView] = []
    async def gen() -> AsyncGenerator[Coroutine[Any, Any, AccountView | None], None]:
        logger.debug('Getting accounts for ids %s from resource URL %s', account_ids, resource_url)
        for account_id in account_ids:
            account_coro = client.get(request.app, URL(resource_url) / account_id, AccountView, headers={SUB: sub})
            yield account_coro
    async def proc(account_coro: Coroutine[None, None, AccountView | None]):
        account = await account_coro
        logger.debug('Got account %s from resource URL %s', account, resource_url)
        if account is not None:
            accounts.append(account)
    await queued_processing(gen, proc)
    context: PermissionContext[AccountView] = PermissionContext(sub)
    return await response.get_all(request, [account.to_dict() for account in accounts],
                                  permissions=[await account.get_permissions(context) for account in accounts],
                                  attribute_permissions=[await account.get_all_attribute_permissions(context) for account in accounts])


@routes.post('/organizations')
@routes.post('/organizations/')
async def post_organization(request: web.Request) -> web.Response:
    """
    Posts the provided organization.
    :param request: the HTTP request.
    :return: a Response object with a status of Created and the object's URI in the Location header.
    ---
    summary: Organization creation
    tags:
        - heaserver-organizations-post-organization
    requestBody:
      description: A new organization object.
      required: true
      content:
        application/vnd.collection+json:
          schema:
            type: object
          examples:
            example:
              summary: Organization example
              value: {
                "template": {
                  "data": [{
                    "name": "created",
                    "value": null
                  },
                  {
                    "name": "derived_by",
                    "value": null
                  },
                  {
                    "name": "derived_from",
                    "value": []
                  },
                  {
                    "name": "description",
                    "value": null
                  },
                  {
                    "name": "display_name",
                    "value": "Joe"
                  },
                  {
                    "name": "invites",
                    "value": []
                  },
                  {
                    "name": "modified",
                    "value": null
                  },
                  {
                    "name": "name",
                    "value": "joe"
                  },
                  {
                    "name": "owner",
                    "value": "system|none"
                  },
                  {
                    "name": "shares",
                    "value": []
                  },
                  {
                    "name": "source",
                    "value": null
                  },
                  {
                    "name": "version",
                    "value": null
                  },
                  {
                    "name": "aws_account_ids",
                    "value": ["1234", "5678"]
                  },
                  {
                    "name": "principal_investigator_id",
                    "value": "1",
                  },
                  {
                    "name": "admin_ids",
                    "value": ["1234", "5678"]
                  },
                  {
                    "name": "manager_ids",
                    "value": ["4321", "8765"]
                  },
                  {
                    "name": "member_ids",
                    "value": ["1", "2"]
                  },
                  {
                  "name": "type",
                  "value": "heaobject.organization.Organization"
                  }]
                }
              }
        application/json:
          schema:
            type: object
          examples:
            example:
              summary: Organization example
              value: {
                "created": null,
                "derived_by": null,
                "derived_from": [],
                "description": null,
                "display_name": "Joe",
                "invited": [],
                "modified": null,
                "name": "joe",
                "owner": "system|none",
                "shares": [],
                "source": null,
                "type": "heaobject.organization.Organization",
                "version": null,
                "aws_account_ids": ["1234", "5678"],
                "principal_investigator_id": "1",
                "admin_ids": ["4321", "8765"],
                "manager_ids": ["4321", "8765"],
                "member_ids": ["1", "2"]
              }
    responses:
      '201':
        $ref: '#/components/responses/201'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.post(request, MONGODB_ORGANIZATION_COLLECTION, Organization)


@routes.put('/organizations/{id}')
async def put_organization(request: web.Request) -> web.Response:
    """
    Updates the organization with the specified id.
    :param request: the HTTP request.
    :return: a Response object with a status of No Content or Not Found.
     ---
    summary: Organization updates
    tags:
        - heaserver-organizations-put-organization
    parameters:
        - $ref: '#/components/parameters/id'
    requestBody:
      description: An updated organization object.
      required: true
      content:
        application/vnd.collection+json:
          schema:
            type: object
          examples:
            example:
              summary: Organization example
              value: {
                "template": {
                  "data": [{
                    "name": "created",
                    "value": null
                  },
                  {
                    "name": "derived_by",
                    "value": null
                  },
                  {
                    "name": "derived_from",
                    "value": []
                  },
                  {
                    "name": "description",
                    "value": null
                  },
                  {
                    "name": "display_name",
                    "value": "Reximus Max"
                  },
                  {
                    "name": "invites",
                    "value": []
                  },
                  {
                    "name": "modified",
                    "value": null
                  },
                  {
                    "name": "name",
                    "value": "reximus"
                  },
                  {
                    "name": "owner",
                    "value": "system|none"
                  },
                  {
                    "name": "shares",
                    "value": []
                  },
                  {
                    "name": "source",
                    "value": null
                  },
                  {
                    "name": "version",
                    "value": null
                  },
                  {
                    "name": "aws_account_ids",
                    "value": ["1234", "5678"]
                  },
                  {
                    "name": "principal_investigator_id",
                    "value": "1",
                  },
                  {
                    "name": "admin_ids",
                    "value": ["1234", "5678"]
                  },
                  {
                    "name": "manager_ids",
                    "value": ["4321", "8765"]
                  },
                  {
                    "name": "member_ids",
                    "value": ["1", "2"]
                  },
                  {
                  "name": "id",
                  "value": "666f6f2d6261722d71757578"
                  },
                  {
                  "name": "type",
                  "value": "heaobject.organization.Organization"
                  }]
                }
              }
        application/json:
          schema:
            type: object
          examples:
            example:
              summary: Organization example
              value: {
                "id": "666f6f2d6261722d71757578",
                "created": null,
                "derived_by": null,
                "derived_from": [],
                "description": null,
                "display_name": "Reximus Max",
                "invites": [],
                "modified": null,
                "name": "reximus",
                "owner": "system|none",
                "shares": [],
                "source": null,
                "type": "heaobject.organization.Organization",
                "version": null,
                "aws_account_ids": ["1234", "5678"],
                "principal_investigator_id": "1",
                "admin_ids": ["1234", "5678"],
                "manager_ids": ["4321", "8765"],
                "member_ids": ["1", "2"]
              }
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    async with _put_lock:
        try:
            obj_ = await new_heaobject_from_type(request, Organization)
        except DeserializeException as e:
            return response.status_bad_request(str(e))
        async with mongo.MongoContext(request, None) as mongo_ctx:
            org_dict = await mongo_ctx.get(request, MONGODB_ORGANIZATION_COLLECTION)
            if org_dict is not None:
                obj_.collaborator_ids = org_dict.get('collaborator_ids', [])
        await _update_permissions(request)
        return await mongoservicelib.put(request, MONGODB_ORGANIZATION_COLLECTION, Organization, obj=obj_)


@routes.delete('/organizations/{id}')
async def delete_organization(request: web.Request) -> web.Response:
    """
    Deletes the organization with the specified id.
    :param request: the HTTP request.
    :return: A Response object with a status of No Content or Not Found.
    ---
    summary: Organization deletion
    tags:
        - heaserver-organizations-delete-organization
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.delete(request, MONGODB_ORGANIZATION_COLLECTION)


@routes.get('/organizations/{id}/opener')
@action('heaserver-organizations-organization-open-awsaccounts', rel=f'hea-opener hea-context-aws hea-default {AWSAccount.get_mime_type()}', path='organizations/{id}/awsaccounts')
async def get_organization_opener(request: web.Request) -> web.Response:
    """

    :param request: the HTTP Request.
    :return: A Response object with a status of Multiple Choices or Not Found.
    ---
    summary: Organization opener choices
    tags:
        - heaserver-organizations-organization-get-open-choices
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '300':
        $ref: '#/components/responses/300'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.opener(request, MONGODB_ORGANIZATION_COLLECTION)

@routes.get('/organizations/{id}/volumes')
@routes.get('/organizations/{id}/volumes/')
async def get_organization_volumes(request: web.Request) -> web.Response:
    result = [v.to_dict() async for v in _get_organization_volumes(request)]
    return await response.get_all(request, result)


@routes.get('/organizations/{id}/awsaccounts')
@routes.get('/organizations/{id}/awsaccounts/')
@action('heaserver-organizations-account-get-actual', rel='hea-actual', path='{+actual_object_uri}')
async def get_organization_aws_accounts(request: web.Request) -> web.Response:
    """

    :param request: the HTTP Request.
    :return: a Response object with a status code of 200.
    ---
    summary: An organization's AWS accounts.
    tags:
        - heaserver-organizations-organization-get-aws-accounts
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB, NONE_USER)
    org_dict = await request.app[HEA_DB].get(request, MONGODB_ORGANIZATION_COLLECTION, var_parts='id', sub=sub)
    if org_dict is None:
        return response.status_not_found()
    org = Organization()
    org.from_dict(org_dict)
    headers = {SUB: sub or '',
               hdrs.AUTHORIZATION: request.headers.get(hdrs.AUTHORIZATION, '')} if SUB in request.headers else None
    account_url = await type_to_resource_url(request, AWSAccount)
    account_ids = org.account_ids
    query = [('account_id', account_id) for account_id in account_ids]
    result: list[DesktopObjectDict] = []
    if account_ids:
        async for a in client.get_all(request.app, URL(account_url).with_path('accounts').with_query(query), AccountView, headers=headers):
            result.append(a.to_dict())
    return await response.get_all(request, result)


@routes.get('/organizations/{id}/members')
@routes.get('/organizations/{id}/members/')
@action('heaserver-organizations-member-get-self', rel='self', path='people/{id}')
async def get_organization_members(request: web.Request) -> web.Response:
    """
    Gets everyone with access to this organization.

    :param request: the HTTP Request.
    :return: a Response object with status code 200 and a body containing either an empty list or a list of buckets.
    ---
    summary: the buckets in an AWS account.
    tags:
        - heaserver-get-members
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
        '200':
            $ref: '#/components/responses/200'
    """
    sub = request.headers.get(SUB)
    headers = {SUB: sub or '',
               hdrs.AUTHORIZATION: request.headers.get(hdrs.AUTHORIZATION, '')} if SUB in request.headers else None

    org_dict = await request.app[HEA_DB].get(request, MONGODB_ORGANIZATION_COLLECTION, var_parts='id', sub=sub)
    if org_dict is None:
        return response.status_not_found()
    org = Organization()
    org.from_dict(org_dict)
    org_members = {k: None for k in chain([org.principal_investigator_id] if org.principal_investigator_id is not None else [],
                                          org.admin_ids if org.admin_ids else [],
                                          org.manager_ids if org.manager_ids else [],
                                          org.member_ids if org.member_ids else [],
                                          org.collaborator_ids if org.collaborator_ids else [])}

    url = URL(await type_to_resource_url(request=request, type_or_type_name=Person))

    def get_one_member_dict(m):
        _logger.debug("People names %s returning", m.display_name if m is not None else None)
        return m.to_dict()

    people_dictionaries = [get_one_member_dict(p_obj) for p_obj in await gather(
        *[client.get(app=request.app, url=url / m_id, type_or_obj=Person, headers=headers) for m_id in org_members])
                           if p_obj is not None]

    return await response.get_all(request, people_dictionaries)


async def collaborator_cb(app: web.Application, desktop_object: DesktopObject):
    async with _put_lock:
        logger = logging.getLogger(__name__)
        logger.debug('Received collaborator action %r', desktop_object)
        match desktop_object:
            case AddingCollaborator():
                collaborator_id = desktop_object.collaborator_id
                organization_id = desktop_object.to_organization_id
            case RemovingCollaborator():
                collaborator_id = desktop_object.collaborator_id
                organization_id = desktop_object.from_organization_id
        if collaborator_id is None:
            raise ValueError('collaborator_id cannot be None')
        logger.debug('Getting organization %s', organization_id)
        org_dict = await app[HEA_DB].get_admin(MONGODB_ORGANIZATION_COLLECTION, mongoattributes={'id': organization_id})
        if org_dict is None:
            raise ValueError(f'No organization with id {organization_id} found')
        org = Organization()
        org.from_dict(org_dict)
        logger.debug('Got organization %r', org)
        modified = False
        match desktop_object:
            case AddingCollaborator():
                org.add_collaborator_id(collaborator_id)
                modified = True
                logger.debug('Collaborator added to organization %s: %s', organization_id, collaborator_id)
            case RemovingCollaborator():
                try:
                    org.remove_collaborator_id(collaborator_id)
                    modified = True
                    logger.debug('Collaborator removed from organization %s: %s', organization_id, collaborator_id)
                except ValueError:
                    logger.debug(f'Collaborator {collaborator_id} not found in organization')
        if modified and ((result := await app[HEA_DB].update_admin(org, MONGODB_ORGANIZATION_COLLECTION)) is None or result.modified_count < 1):
            raise ValueError(f'Organization {organization_id} not updated')
        to_delete = []
        for cache_key in app[HEA_CACHE]:
            if cache_key[1] == MONGODB_ORGANIZATION_COLLECTION and cache_key[2] in (None, f"id^{organization_id}"):
                to_delete.append(cache_key)
        for cache_key in to_delete:
            app[HEA_CACHE].pop(cache_key, None)
        logger.debug('Organization %s updated successfully', org.id)


def main() -> None:
    config = init_cmd_line(description='a service for managing organization information for research laboratories and other research groups',
                           default_port=8087)
    start(package_name='heaserver-organizations', db=mongo.MongoManager,
          wstl_builder_factory=builder_factory(__package__), config=config,
          cleanup_ctx=[publisher_cleanup_context_factory(config),
                       subscriber_cleanup_context_factory(message_body_cb=collaborator_cb, config=config,
                                                          topics=[AddingCollaborator.get_type_name(), RemovingCollaborator.get_type_name()])])

class _OrganizationPermissionsChanged:
    def __init__(self) -> None:
        super().__init__()
        self.__user_id: str = NONE_USER
        self.__group_ids: list[str] = []
        self.__old_account_ids: list[str] = []
        self.__new_account_ids: list[str] = []
        self.__new_org_display_name: str | None = None

    @property
    def user_id(self) -> str:
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: str):
        if user_id == '':
            raise ValueError('user_id cannot be the empty string')
        self.__user_id = str(user_id) if user_id is not None else NONE_USER

    @property
    def group_ids(self) -> list[str]:
        return self.__group_ids.copy()

    @group_ids.setter
    def group_ids(self, group_ids: list[str]):
        if group_ids is None:
            self.__group_ids = []
        elif not isinstance(group_ids, str):
            self.__group_ids = [str(i) for i in group_ids]
        else:
            self.__group_ids = [str(group_ids)]

    def add_group_id(self, group_id: str):
        self.__group_ids.append(str(group_id))

    def remove_group_id(self, group_id: str):
        self.__group_ids.remove(str(group_id))

    @property
    def old_account_ids(self) -> list[str]:
        return self.__old_account_ids.copy()

    @old_account_ids.setter
    def old_account_ids(self, account_ids: list[str]):
        if account_ids is None:
            self.__old_account_ids = []
        elif not isinstance(account_ids, str):
            self.__old_account_ids = [str(i) for i in account_ids]
        else:
            self.__old_account_ids = [str(account_ids)]

    def add_old_account_id(self, account_id: str):
        self.__old_account_ids.append(str(account_id))

    def remove_old_account_id(self, account_id: str):
        self.__old_account_ids.remove(str(account_id))

    @property
    def new_account_ids(self) -> list[str]:
        return self.__new_account_ids.copy()

    @new_account_ids.setter
    def new_account_ids(self, account_ids: list[str]):
        if account_ids is None:
            self.__new_account_ids = []
        elif not isinstance(account_ids, str):
            self.__new_account_ids = [str(i) for i in account_ids]
        else:
            self.__new_account_ids = [str(account_ids)]

    def add_new_account_id(self, account_id: str):
        self.__new_account_ids.append(str(account_id))

    def remove_new_account_id(self, account_id: str):
        self.__new_account_ids.remove(str(account_id))

    @property
    def new_organization_display_name(self) -> str | None:
        return self.__new_org_display_name

    @new_organization_display_name.setter
    def new_organization_display_name(self, new_organization_display_name: str | None):
        self.__new_org_display_name = str(new_organization_display_name) if new_organization_display_name is not None else None

    def __str__(self):
        return f'_OrganizationPermissionsChanged(user_id={self.user_id}, group_ids={self.group_ids}, ' \
               f'old_account_ids={self.old_account_ids}, new_account_ids={self.new_account_ids}, ' \
               f'new_organization_display_name={self.new_organization_display_name})'

async def _get_organization_volumes(request: web.Request) -> AsyncGenerator[Volume, None]:
    sub = request.headers.get(SUB)
    org_dict = await request.app[HEA_DB].get(request, MONGODB_ORGANIZATION_COLLECTION, var_parts='id', sub=sub)
    if org_dict is None:
        raise response.status_not_found()
    org = Organization()
    org.from_dict(org_dict)
    headers = {SUB: sub or '',
               hdrs.AUTHORIZATION: request.headers.get(hdrs.AUTHORIZATION, '')} if SUB in request.headers else None


    volume_url = await type_to_resource_url(request, Volume)
    if volume_url is None:
        raise ValueError('No Volume service registered')
    get_volumes_url = URL(volume_url) / 'byfilesystemtype' / AWSFileSystem.get_type_name()

    aws_account_url = await type_to_resource_url(request, AWSAccount)
    if aws_account_url is None:
        raise ValueError('No AWSAccount service registered')

    async def get_one(volume_id):
        return await client.get(request.app, URL(aws_account_url) / volume_id / 'awsaccounts' / 'me', AWSAccount, headers=headers)
    async for v in client.get_all(request.app, get_volumes_url, Volume, headers=headers):
        if await get_one(v.id) is not None:
            yield v

async def _update_permissions(request: web.Request):
    """
    Updates the organization's permissions.

    :param request: the HTTP request (required).
    :raises ClientResponseError: if something goes wrong, an error to send as the HTTP response.
    """
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    old_dict = await mongoservicelib.get_dict(request, MONGODB_ORGANIZATION_COLLECTION)
    if old_dict is not None:
        old_org = Organization()
        old_org.from_dict(old_dict)
        try:
            new_org = await new_heaobject_from_type(request, Organization)
        except DeserializeException as e:
            raise response.status_bad_request(str(e))
        context: PermissionContext[Organization] = PermissionContext(sub)
        def return_response(display: str) -> web.HTTPBadRequest:
            return response.status_bad_request(f"You have insufficient permissions to change this organization's {display}")
        if old_org.admin_ids != new_org.admin_ids and await old_org.is_attribute_read_only('admin_ids', context):
            raise return_response('administrators')
        if old_org.manager_ids != new_org.manager_ids and await old_org.is_attribute_read_only('manager_ids', context):
            raise return_response("managers")
        if old_org.member_ids != new_org.member_ids and await old_org.is_attribute_read_only('member_ids', context):
            raise return_response("members")
        if old_org.admin_group_ids != new_org.admin_group_ids and await old_org.is_attribute_read_only('admin_group_ids', context):
            raise return_response("admin group mappings")
        if old_org.manager_group_ids != new_org.manager_group_ids and await old_org.is_attribute_read_only('manager_group_ids', context):
            raise return_response("manager group mappings")
        if old_org.member_group_ids != new_org.member_group_ids and await old_org.is_attribute_read_only('member_group_ids', context):
            raise return_response("member group mappings")

        person_url: str | None = None
        async def get_person_url():
            nonlocal person_url
            async with Lock():
                if person_url is None:
                    person_url = await type_to_resource_url(request, Person)
                return str(URL(person_url) / 'internal')

        group_url: str | None = None
        async def get_group_url():
            nonlocal group_url
            async with Lock():
                if group_url is None:
                    group_url = await type_to_resource_url(request, Group)
                return group_url

        async def add_and_delete(old_group_ids: Collection[str], new_group_ids: Collection[str], user_ids: Collection[str]):
            added_group_id_strs = set(new_group_ids).difference(old_group_ids)
            deleted_group_id_strs = set(old_group_ids).difference(new_group_ids)
            groups = await gather(*[client.get(request.app, URL(await get_group_url()) / group_id_str, Group) for group_id_str in deleted_group_id_strs])
            for group in groups:
                assert group is not None, 'group cannot be None'
                assert group.id is not None, 'group.id cannot be None'
                if group.group_type != GroupType.ORGANIZATION:
                    deleted_group_id_strs.remove(group.id)
            coros = []
            for user_id in user_ids:
                coros.append(_update_group_membership(request,
                                                    user_id,
                                                    added_group_id_strs,
                                                    deleted_group_id_strs,
                                                    get_person_url))
            await gather(*coros)

        await gather(
            add_and_delete(old_org.member_group_ids,
                           new_org.member_group_ids,
                           set(new_org.member_ids).intersection(old_org.member_ids)),
            add_and_delete(old_org.member_group_ids, [], set(old_org.member_ids).difference(new_org.member_ids)),
            add_and_delete([], new_org.member_group_ids, set(new_org.member_ids).difference(old_org.member_ids))
        )

        old_manager_ids = set(old_org.manager_ids)
        if old_org.principal_investigator_id is not None:
            old_manager_ids.add(old_org.principal_investigator_id)
        new_manager_ids = set(new_org.manager_ids)
        if new_org.principal_investigator_id is not None:
            new_manager_ids.add(new_org.principal_investigator_id)
        await gather(
            add_and_delete(old_org.manager_group_ids,
                             new_org.manager_group_ids,
                             new_manager_ids.intersection(old_manager_ids)),
            add_and_delete(old_org.manager_group_ids, [], old_manager_ids.difference(new_manager_ids)),
            add_and_delete([], new_org.manager_group_ids, new_manager_ids.difference(old_manager_ids))
        )

        await gather(
            add_and_delete(old_org.admin_group_ids,
                             new_org.admin_group_ids,
                             set(new_org.admin_ids).intersection(old_org.admin_ids)),
            add_and_delete(old_org.admin_group_ids, [], set(old_org.admin_ids).difference(new_org.admin_ids)),
            add_and_delete([], new_org.admin_group_ids, set(new_org.admin_ids).difference(old_org.admin_ids))
        )

        coros = []
        old_org_user_ids = set(chain(old_org.admin_ids, old_manager_ids, old_org.member_ids))
        new_org_user_ids = set(chain(new_org.admin_ids, new_manager_ids, new_org.member_ids))
        group_ids = [group_id for group_id in chain(new_org.admin_group_ids, new_org.manager_group_ids,
                                                    new_org.member_group_ids)]
        for user_id in old_org_user_ids.intersection(new_org_user_ids):
            changed = _OrganizationPermissionsChanged()
            changed.old_account_ids = old_org.account_ids
            changed.new_account_ids = new_org.account_ids
            changed.group_ids = group_ids
            changed.user_id = user_id
            changed.new_organization_display_name = new_org.display_name
            coros.append(_update_volumes_and_credentials(request, changed))
        for user_id in old_org_user_ids.difference(new_org_user_ids):
            changed = _OrganizationPermissionsChanged()
            changed.old_account_ids = old_org.account_ids
            changed.new_account_ids = []
            changed.group_ids = group_ids
            changed.user_id = user_id
            changed.new_organization_display_name = new_org.display_name
            coros.append(_update_volumes_and_credentials(request, changed))
        for user_id in new_org_user_ids.difference(old_org_user_ids):
            changed = _OrganizationPermissionsChanged()
            changed.old_account_ids = []
            changed.new_account_ids = new_org.account_ids
            changed.group_ids = group_ids
            changed.user_id = user_id
            changed.new_organization_display_name = new_org.display_name
            coros.append(_update_volumes_and_credentials(request, changed))
        await gather(*coros)
    else:
        raise response.status_not_found()


async def _update_volumes_and_credentials(request: web.Request, changed: _OrganizationPermissionsChanged):
    """
    Synchronizes volumes and credentials for a user, and tries to repair volumes and credentials for a user. If the
    user is not found in the people microservice, their volumes and credentials are deleted.

    :param request: The HTTP request (required).
    :param changed: the changes to make (required).
    :raises ClientResponseError: if something goes wrong, an error to send as the HTTP response.
    """
    logger = logging.getLogger(__name__)
    logger.debug('Updating volumes and credentials %s', changed)
    app = request.app
    sub = request.headers.get(SUB, NONE_USER)
    group_url_str = await client.get_resource_url(app, Group)
    assert group_url_str is not None, 'group_url_str cannot be None'
    group_url = URL(group_url_str)
    person_url_str = await client.get_resource_url(app, Person)
    assert person_url_str is not None, 'person_url_str cannot be None'
    person, groups_, account_view_url_str, volume_url_str = await gather(
        client.get(app, URL(person_url_str) / changed.user_id,
                    type_or_obj=Person,
                    headers=_sub_header),
        gather(*[client.get(app, group_url / group_id, type_or_obj=Group) for group_id in changed.group_ids]),
        client.get_resource_url(app, AccountView),
        client.get_resource_url(app, Volume)
    )
    groups: list[Group] = []
    for group in groups_:
        assert group is not None, 'group cannot be None'
        groups.append(group)
    assert account_view_url_str is not None, 'account_view_url_str cannot be None'
    assert volume_url_str is not None, 'volume_url_str cannot be None'
    account_view_url, volume_url = URL(account_view_url_str), URL(volume_url_str)
    acct_headers = {SUB: sub, hdrs.AUTHORIZATION: request.headers[hdrs.AUTHORIZATION]}
    awaitables: list[Awaitable[None]] = []
    context: PermissionContext[Volume] = PermissionContext(changed.user_id)
    if deleted_accounts := set(changed.old_account_ids).difference(changed.new_account_ids if person is not None else []):
        async def deleted_accounts_coro() -> None:
            logger.debug('Deleting volumes and credentials for accounts %s for user %s', deleted_accounts, changed.user_id)
            volumes_to_delete = await client.get_all_list(app, volume_url, Volume,
                                                          query_params=_account_query_params(deleted_accounts),
                                                          headers=_sub_header)
            volumes_for_current_user = [v for v in volumes_to_delete if await v.has_permissions(RESTPermissionGroup.GETTER_PERMS, context)]
            await gather(*[_delete_volume_and_credentials(app, volume_url, volume, credential_id) \
                        for volume, credential_id in ((volume, volume.credential_id) for volume in volumes_for_current_user)])
        awaitables.append(deleted_accounts_coro())

    if person is not None:
        if accounts_needing_updates := set(changed.old_account_ids).intersection(changed.new_account_ids):
            async def accounts_needing_updates_coro() -> None:
                logger.debug('Updating credentials for accounts %s for person %s', accounts_needing_updates, person.id)
                awaitables_: list[Awaitable] = []
                volumes_to_update = await client.get_all_list(app, volume_url, Volume,
                                                        query_params=_account_query_params(accounts_needing_updates),
                                                        headers=_sub_header)
                volumes_for_current_user = [v for v in volumes_to_update if await v.has_permissions(RESTPermissionGroup.GETTER_PERMS, context)]
                awaitables_.extend(_update_credentials(request, account_view_url, volume, credential_id, person, groups,
                                                            changed.new_organization_display_name, volume_url) \
                            for volume, credential_id in ((volume, volume.credential_id) for volume in volumes_for_current_user))
                if person is not None:
                    accounts_missing_a_volume = accounts_needing_updates.difference(v.account_id for v in volumes_for_current_user)
                    account_views_by_account_id: dict[str, AccountView | None] = {}
                    for acct_id in accounts_missing_a_volume:
                        logger.warn('Replacing missing volume for account %s for user %s', acct_id, person.id)
                        async def replace_missing_volume(account_id: str):
                            if (account_view := account_views_by_account_id.get(account_id)) is None:
                                account_view = await client.get(app, account_view_url / account_id, AccountView, headers=acct_headers)
                                account_views_by_account_id[account_id] = account_view
                            if account_view is None:
                                logger.warn("Current user %s does not have access to account %s and there is nothing we can do to change that", person.id, account_id)
                            else:
                                await _new_volume_and_credentials(request, account_view, person, groups, changed.new_organization_display_name, volume_url)
                        awaitables_.append(replace_missing_volume(acct_id))
                await gather(*awaitables_)
            awaitables.append(accounts_needing_updates_coro())

        if added_accounts := set(changed.new_account_ids).difference(changed.old_account_ids):
            async def added_accounts_coro() -> None:
                logger.debug('Creating new volumes and credentials for accounts %s for user %s', added_accounts, person.id)
                awaitables_: list[Awaitable] = []
                async for account_view in client.get_all(app, account_view_url, AccountView,
                                                        query_params=_account_query_params(added_accounts),
                                                        headers=acct_headers):
                    awaitable = _new_volume_and_credentials(request, account_view, person, groups, changed.new_organization_display_name, volume_url)
                    awaitables_.append(awaitable)
                await gather(*awaitables_)
            awaitables.append(added_accounts_coro())
    await gather(*awaitables)

def _account_query_params(account_ids: Collection[str]) -> MultiDict[str]:
    return MultiDict(('account_id', account_id) for account_id in account_ids)

async def _update_credentials(request: web.Request,
                                         account_view_url: URL,
                                         volume: Volume,
                                         credential_id: str | None,
                                         person: Person,
                                         groups: Sequence[Group],
                                         organization_display_name: str | None,
                                         volume_url: URL):
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    app = request.app
    assert person.id is not None, 'person.id cannot be None'
    async def do_nothing() -> None:
        return None
    assert volume.credential_type_name is not None, 'volume.credential_type_name cannot be None'
    assert volume.id is not None, 'volume.id cannot be None'
    assert volume.account_id is not None, 'volume.account_id cannot be None'
    credential_url_str = await client.get_resource_url(app, volume.credential_type_name)
    assert credential_url_str is not None, 'credential_url_str cannot be None'
    credential, account_view = await gather(
        client.get(app,  URL(credential_url_str) / credential_id,
                   type_or_obj=desktop_object_type_for_name(volume.credential_type_name, Credentials), headers=_sub_header) if credential_id is not None else do_nothing(),
        client.get(app,
                   account_view_url / volume.account_id,
                   type_or_obj=AccountView,
                   headers={SUB: sub, hdrs.AUTHORIZATION: request.headers[hdrs.AUTHORIZATION]})
    )
    assert account_view is not None, 'account_view cannot be None'
    assert account_view.actual_object_type_name is not None, 'account_view.actual_object_type_name cannot be None'
    actual_account_url_str = await client.get_resource_url(app, account_view.actual_object_type_name)
    assert actual_account_url_str is not None, 'actual_account_url_str cannot be None'
    assert account_view.actual_object_id is not None, 'account_view.actual_object_id cannot be None'
    actual_account_url = URL(actual_account_url_str) / account_view.actual_object_id
    logger.debug('Actual account URL is %s', actual_account_url)
    actual_account = await client.get(app,
                                    actual_account_url,
                                    type_or_obj=desktop_object_type_for_name(account_view.actual_object_type_name, Account),  # type: ignore[type-abstract]
                                    headers={SUB: sub, hdrs.AUTHORIZATION: request.headers[hdrs.AUTHORIZATION]})
    assert actual_account is not None, 'actual_account should not be None'
    volume.display_name = _volume_display_name(account_view)
    if credential is None:
        logger.warn('Replacing missing credentials for account %s and volume %s for user %s', actual_account, volume, person)
        new_credentials = actual_account.new_credentials(person, groups)
        if new_credentials is None:
            raise ValueError('Unexpected None new credentials')
        new_credentials.display_name = _credentials_display_name(actual_account, organization_display_name)
        new_credentials.owner = CREDENTIALS_MANAGER_USER
        new_credentials.temporary = True
        share = ShareImpl()
        share.user = person.id
        share.permissions=[Permission.VIEWER]
        new_credentials.shares = [share]
        volume.credential_type_name = new_credentials.type
        credentials_url_str = await client.get_resource_url(app, type(new_credentials))
        assert credentials_url_str is not None, 'credentials_url_str cannot be None'
        credentials_url_ = URL(credentials_url_str)
        try:
            new_credential_url = await client.post(app, credentials_url_,
                                            new_credentials, headers=_sub_header)
            volume.credential_id = new_credential_url[new_credential_url.rindex('/') + 1:]
        except web.HTTPConflict:
            assert new_credentials.name is not None, 'new_credentials.name cannot be None'
            credential_by_name = await client.get(app, credentials_url_ / 'byname' / new_credentials.name, type(new_credentials), headers=_sub_header)
            assert credential_by_name is not None, 'credential_by_name cannot be None'
            volume.credential_id = credential_by_name.id
    else:
        credential.role = actual_account.get_role_to_assume(person, groups)
        credential.display_name = _credentials_display_name(actual_account, organization_display_name)
        credential.expiration = None
        credential.temporary = True
        credential.name = f'{person.id}_{actual_account.type}_{actual_account.id}'
        credentials_url_str_ = await client.get_resource_url(app, type(credential))
        assert credentials_url_str_ is not None, 'credentials_url_str_ cannot be None'
        credentials_url = URL(credentials_url_str_)
        assert credential.id is not None, 'credential.id cannot be None'
        await client.put(app, credentials_url / credential.id, credential, headers=_sub_header)
    await client.put(app, volume_url / volume.id, volume, headers=_sub_header)

async def _delete_volume_and_credentials(app: web.Application,
                                         volume_url: URL,
                                         volume: Volume,
                                         credential_id: str | None):
    try:
        assert volume.id is not None, 'volume.id cannot be None'
        assert volume.credential_type_name is not None, 'volume.credential_type_name cannot be None'
        await client.delete(app, volume_url / volume.id, headers=_sub_header)
        if credential_id:
            credential_url_str = await client.get_resource_url(app, volume.credential_type_name)
            assert credential_url_str is not None, 'credential_url_str cannot be None'
            credential_url = URL(credential_url_str)
            await client.delete(app, credential_url / credential_id, headers=_sub_header)
    except ClientResponseError as e:
        if e.status != 404:
            raise e

async def _new_volume_and_credentials(request: web.Request,
                                      account_view: AccountView,
                                      person: Person,
                                      groups: Sequence[Group],
                                      organization_display_name: str | None,
                                      volume_url: URL):
    logger = logging.getLogger(__name__)
    sub = request.headers.get(SUB, NONE_USER)
    app = request.app
    volume_name = _volume_name(account_view, person)
    volume = await client.get(app, volume_url / 'byname' / volume_name, Volume, headers=_sub_header)
    if volume is None or volume.owner != CREDENTIALS_MANAGER_USER:
        volume = Volume()
        volume_exists = False
        volume.owner = CREDENTIALS_MANAGER_USER
        share = ShareImpl()
        assert person.id is not None, 'person.id cannot be None'
        share.user = person.id
        share.add_permission(Permission.VIEWER)
        volume.shares = [share]
    else:
        volume_exists = True
    volume.account_id = account_view.id
    volume.display_name = _volume_display_name(account_view)
    volume.name = volume_name
    volume.file_system_type = account_view.file_system_type
    volume.file_system_name = account_view.file_system_name
    assert account_view.actual_object_type_name is not None, 'account_view.actual_object_type_name cannot be None'
    account_url_str = await client.get_resource_url(app, account_view.actual_object_type_name)
    assert account_url_str is not None, 'account_url_str cannot be None'
    assert account_view.actual_object_id is not None, 'account_view.actual_object_id cannot be None'
    actual_account = await client.get(app, URL(account_url_str) / account_view.actual_object_id,
                                      type_or_obj=desktop_object_type_for_name(account_view.actual_object_type_name, Account),  # type: ignore[type-abstract]
                                      headers={SUB: sub, hdrs.AUTHORIZATION: request.headers[hdrs.AUTHORIZATION]})
    assert actual_account is not None, 'actual_account cannot be None'
    logger.debug('Getting new credentials for %r with groups %s', person, groups)
    new_credentials = actual_account.new_credentials(person, groups)
    if new_credentials is not None:
        new_credentials.display_name = _credentials_display_name(actual_account, organization_display_name)
        new_credentials.owner = CREDENTIALS_MANAGER_USER
        share = ShareImpl()
        assert person.id is not None, 'person.id cannot be None'
        share.user = person.id
        share.add_permission(Permission.VIEWER)
        new_credentials.add_share(share)
        new_credentials.temporary = True
        credentials_url_str = await client.get_resource_url(app, type(new_credentials))
        assert credentials_url_str is not None, 'credentials_url_str cannot be None'
        credentials_url = URL(credentials_url_str)
        assert new_credentials.name is not None, 'new_credentials.name cannot be None'
        existing_credentials = await client.get(app, credentials_url / 'byname' / new_credentials.name,
                                                type(new_credentials), headers=_sub_header)
        logger.debug('Got existing credentials %r', existing_credentials)
        if existing_credentials is not None and existing_credentials.owner == CREDENTIALS_MANAGER_USER:
            assert existing_credentials.id is not None, 'existing_credentials.id cannot be None'
            volume.credential_id = existing_credentials.id
            existing_credentials.name = new_credentials.name
            existing_credentials.display_name = _credentials_display_name(actual_account, organization_display_name)
            existing_credentials.temporary = True
            existing_credentials.expiration = None
            logger.debug('Updating existing credentials %r', existing_credentials)
            await client.put(app, credentials_url / existing_credentials.id, existing_credentials, headers=_sub_header)
        else:
            new_credential_url = await client.post(app, credentials_url, new_credentials, headers=_sub_header)
            volume.credential_id = new_credential_url[new_credential_url.rindex('/') + 1:]
        volume.credential_type_name = new_credentials.type
        if volume_exists:
            assert volume.id is not None, 'volume.id cannot be None'
            await client.put(app, volume_url / volume.id, volume, headers=_sub_header)
        else:
            await client.post(app, volume_url, volume, headers=_sub_header)

def _volume_display_name(account_view):
    return f'{account_view.type_display_name} {account_view.display_name}'

def _volume_name(account_view, person):
    return f'{person.id}_{account_view.id}'

def _credentials_display_name(account: Account, organization_display_name: str | None):
    return f'{account.display_name} - {organization_display_name}'

async def _update_group_membership(request: web.Request,
                                   user: str,
                                   added_group_ids: Collection[str],
                                   deleted_group_ids: Collection[str],
                                   group_url_getter: Callable[[], Coroutine[None, None, str]]):
    coros = []
    group_url = URL(await group_url_getter())
    async def delete(deleted_group):
        try:
            await client.delete(request.app, group_url / user / 'groups' / deleted_group, headers={SUB: CREDENTIALS_MANAGER_USER})
        except ClientResponseError as e:
            if e.status != 404:
                raise e
    for deleted_group_id in deleted_group_ids:
        coros.append(delete(deleted_group_id))
    for added_group_id in added_group_ids:
        group = Group()
        group.id = added_group_id
        coros.append(client.post(request.app, group_url / user / 'groups', group, headers={SUB: CREDENTIALS_MANAGER_USER}))
    await gather(*coros)
