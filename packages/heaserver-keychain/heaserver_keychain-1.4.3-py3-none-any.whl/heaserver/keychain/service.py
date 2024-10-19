"""
The HEA Keychain provides ...
"""
from datetime import timedelta
from functools import partial

from aiohttp import hdrs, ClientResponseError
from heaobject.activity import Status
from heaobject.data import ClipboardData
from heaobject.registry import Property
from heaobject.root import ShareImpl, Permission, desktop_object_from_dict
from heaserver.service import response, appproperty, client
from heaserver.service.activity import DesktopObjectActionLifecycle
from heaserver.service.heaobjectsupport import type_to_resource_url
from heaserver.service.oidcclaimhdrs import SUB
from heaobject.user import NONE_USER, CREDENTIALS_MANAGER_USER
from heaserver.service.runner import init_cmd_line, routes, start, web, scheduled_cleanup_ctx
from heaserver.service.db import mongoservicelib, awsservicelib, aws
from heaserver.service.wstl import builder_factory, action
from heaserver.service.messagebroker import publisher_cleanup_context_factory, publish_desktop_object
from heaserver.service.util import now
from heaobject.keychain import Credentials, AWSCredentials
import asyncio
from heaserver.service.appproperty import HEA_CACHE, HEA_DB
from botocore.exceptions import ClientError as BotoClientError, ClientError

from heaobject.error import DeserializeException
from io import StringIO

import logging

from mypy_boto3_iam import IAMClient
from mypy_boto3_iam.type_defs import ListAttachedRolePoliciesResponseTypeDef, CreateAccessKeyResponseTypeDef, \
    EmptyResponseMetadataTypeDef
from typing_extensions import Optional
from yarl import URL
from typing import Any

_logger = logging.getLogger(__name__)
MONGODB_CREDENTIALS_COLLECTION = 'credentials'


@routes.get('/credentialsping')
async def ping(request: web.Request) -> web.Response:
    """
    Checks if this service is running.

    :param request: the HTTP request.
    :return: the HTTP response.
    """
    return await mongoservicelib.ping(request)


@routes.get('/credentials/internal/token')
async def test(request: web.Request) -> web.Response:
    """
    Checks if this service is running.

    :param request: the HTTP request.
    :return: the HTTP response.
    """
    return web.HTTPOk()


@routes.get('/credentials/{id}')
@action('heaserver-keychain-credentials-get-properties', rel='hea-properties hea-context-menu',
        itemif='type=="heaobject.keychain.Credentials"')
@action('heaserver-keychain-awscredentials-get-properties', rel='hea-properties hea-context-menu',
        itemif='type=="heaobject.keychain.AWSCredentials"')
@action(name='heaserver-keychain-awscredentials-get-cli-credentials-file',
        rel='hea-dynamic-clipboard hea-retrieve-clipboard-icon hea-context-menu',
        path='credentials/{id}/awsclicredentialsfile', itemif='type=="heaobject.keychain.AWSCredentials"')
@action(name='heaserver-keychain-get-generate-awscredential',
        rel='hea-dynamic-clipboard hea-generate-clipboard-icon hea-context-menu',
        path='credentials/{id}/managedawscredential', itemif='type=="heaobject.keychain.AWSCredentials"')
# @action('heaserver-keychain-credentials-open-choices', rel='hea-opener-choices hea-context-menu', path='credentials/{id}/opener')
# @action('heaserver-keychain-credentials-duplicate', rel='hea-dynamic-standard hea-icon-duplicator hea-context-menu', path='credentials/{id}/duplicator')
@action('heaserver-keychain-credentials-get-self', rel='self', path='credentials/{id}')
async def get_credentials(request: web.Request) -> web.Response:
    """
    Gets the credentials with the specified id.

    :param request: the HTTP request.
    :return: the requested credentials or Not Found.
    ---
    summary: A specific credentials.
    tags:
        - heaserver-keychain-get-credentials
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    _logger.debug('Requested credentials by id %s' % request.match_info["id"])
    return await mongoservicelib.get(request, MONGODB_CREDENTIALS_COLLECTION)


@routes.get('/credentials/{id}/managedawscredential')
@routes.get('/credentials/{id}/managedawscredential/')
@action(name="heaserver-keychain-get-generate-awscredential-form")
async def get_new_aws_credential_form(request: web.Request) -> web.Response:
    return await _get_aws_credential_form(request, managed=True)


@routes.get('/credentials/{id}/awsclicredentialsfile')
@action(name="heaserver-keychain-awscredentials-get-cli-credentials-file-form")
async def get_cli_credentials_file_form(request: web.Request) -> web.Response:
    return await _get_aws_credential_form(request)


@routes.get('/credentials/byname/{name}')
async def get_credentials_by_name(request: web.Request) -> web.Response:
    """
    Gets the credentials with the specified name.

    :param request: the HTTP request.
    :return: the requested credentials or Not Found.
    ---
    summary: Specific credentials queried by name.
    tags:
        - heaserver-keychain-get-credentials-by-name
    parameters:
        - $ref: '#/components/parameters/name'
    responses:
      '200':
        $ref: '#/components/responses/200'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.get_by_name(request, MONGODB_CREDENTIALS_COLLECTION)


@routes.get('/credentials')
@routes.get('/credentials/')
@action('heaserver-keychain-credentials-get-properties', rel='hea-properties hea-context-menu',
        itemif='type=="heaobject.keychain.Credentials"')
@action('heaserver-keychain-awscredentials-get-properties', rel='hea-properties hea-context-menu',
        itemif='type=="heaobject.keychain.AWSCredentials"')
@action(name='heaserver-keychain-awscredentials-get-cli-credentials-file',
        rel='hea-dynamic-clipboard hea-retrieve-clipboard-icon hea-context-menu',
        path='credentials/{id}/awsclicredentialsfile', itemif='type=="heaobject.keychain.AWSCredentials"')
@action(name='heaserver-keychain-get-generate-awscredential',
        rel='hea-dynamic-clipboard hea-generate-clipboard-icon hea-context-menu',
        path='credentials/{id}/managedawscredential', itemif='type=="heaobject.keychain.AWSCredentials"')
# @action('heaserver-keychain-credentials-open-choices', rel='hea-opener-choices hea-context-menu', path='credentials/{id}/opener')
# @action('heaserver-keychain-credentials-duplicate', rel='hea-dynamic-standard hea-icon-duplicator hea-context-menu', path='credentials/{id}/duplicator')
@action('heaserver-keychain-credentials-get-self', rel='self', path='credentials/{id}')
async def get_all_credentials(request: web.Request) -> web.Response:
    """
    Gets all credentials.

    :param request: the HTTP request.
    :return: all credentials.

    ---
    summary: All credentials.
    tags:
        - heaserver-keychain-get-all-credentials
    responses:
      '200':
        $ref: '#/components/responses/200'
    """
    return await mongoservicelib.get_all(request, MONGODB_CREDENTIALS_COLLECTION)


# @routes.get('/credentials/{id}/duplicator')
# @action(name='heaserver-keychain-credentials-duplicate-form')
# async def get_credentials_duplicate_form(request: web.Request) -> web.Response:
#     """
#     Gets a form template for duplicating the requested credentials.
#
#     :param request: the HTTP request. Required.
#     :return: the requested form, or Not Found if the requested credentials was not found.
#     """
#     return await mongoservicelib.get(request, MONGODB_CREDENTIALS_COLLECTION)
#
#
# @routes.post('/credentials/duplicator')
# async def post_credentials_duplicator(request: web.Request) -> web.Response:
#     """
#     Posts the provided credentials for duplication.
#     :param request: the HTTP request.
#     :return: a Response object with a status of Created and the object's URI in the
#     """
#     return await mongoservicelib.post(request, MONGODB_CREDENTIALS_COLLECTION, Credentials)


@routes.post('/credentials')
@routes.post('/credentials/')
async def post_credentials(request: web.Request) -> web.Response:
    """
    Posts the provided credentials.

    :param request: the HTTP request.
    :return: a Response object with a status of Created and the object's URI in the Location header.
    ---
    summary: Credentials creation
    tags:
        - heaserver-keychain-post-credentials
    requestBody:
      description: A new credentials object.
      required: true
      content:
        application/vnd.collection+json:
          schema:
            type: object
          examples:
            example:
              summary: Credentials
              value: {
                "template": {
                  "data": [
                    {
                      "name": "created",
                      "value": null,
                      "prompt": "created",
                      "display": true
                    },
                    {
                      "name": "derived_by",
                      "value": null,
                      "prompt": "derived_by",
                      "display": true
                    },
                    {
                      "name": "derived_from",
                      "value": [],
                      "prompt": "derived_from",
                      "display": true
                    },
                    {
                      "name": "description",
                      "value": null,
                      "prompt": "description",
                      "display": true
                    },
                    {
                      "name": "display_name",
                      "value": "Joe",
                      "prompt": "display_name",
                      "display": true
                    },
                    {
                      "name": "invites",
                      "value": [],
                      "prompt": "invites",
                      "display": true
                    },
                    {
                      "name": "modified",
                      "value": null,
                      "prompt": "modified",
                      "display": true
                    },
                    {
                      "name": "name",
                      "value": "joe",
                      "prompt": "name",
                      "display": true
                    },
                    {
                      "name": "owner",
                      "value": "system|none",
                      "prompt": "owner",
                      "display": true
                    },
                    {
                      "name": "shares",
                      "value": [],
                      "prompt": "shares",
                      "display": true
                    },
                    {
                      "name": "source",
                      "value": null,
                      "prompt": "source",
                      "display": true
                    },
                    {
                      "name": "version",
                      "value": null,
                      "prompt": "version",
                      "display": true
                    },
                    {
                      "name": "type",
                      "value": "heaobject.keychain.Credentials"
                    }
                  ]
                }
              }
        application/json:
          schema:
            type: object
          examples:
            example:
              summary: Credentials
              value: {
                "created": null,
                "derived_by": null,
                "derived_from": [],
                "description": null,
                "display_name": "Joe",
                "invites": [],
                "modified": null,
                "name": "joe",
                "owner": "system|none",
                "shares": [],
                "source": null,
                "type": "heaobject.keychain.Credentials",
                "version": null
              }
    responses:
      '201':
        $ref: '#/components/responses/201'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.post(request, MONGODB_CREDENTIALS_COLLECTION, Credentials)


@routes.post('/credentials/{id}/managedawscredential')
@routes.post('/credentials/{id}/managedawscredential/')
async def post_create_managed_aws_credentials_form(request: web.Request) -> web.Response:
    """
    Posts a template for requesting the generation of managed credentials.

    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: Managed credential url
    tags:
        - heaserver-keychain
    parameters:
        - name: id
          in: path
          required: true
          description: The id of the credential.
          schema:
            type: string
          examples:
            example:
              summary: A credential id
              value: 666f6f2d6261722d71757578
        - $ref: '#/components/parameters/id'
    requestBody:
        description: The expiration time for the presigned URL.
        required: true
        content:
            application/vnd.collection+json:
              schema:
                type: object
              examples:
                example:
                  summary: The time before the key expires in hours
                  value: {
                    "template": {
                      "data": [
                      {
                        "name": "key_lifespan",
                        "value": 72
                      }]
                    }
                  }
            application/json:
              schema:
                type: object
              examples:
                example:
                  summary: The time before the key expires in hours
                  value: {
                    "key_lifespan": 72
                  }
    responses:
      '200':
        $ref: '#/components/responses/200'
      '403':
        $ref: '#/components/responses/403'
      '404':
        $ref: '#/components/responses/404'
    """
    credential_id = request.match_info.get('id', None)
    sub = request.headers.get(SUB, NONE_USER)
    # request for admin
    auth_header_value = request.headers.get(hdrs.AUTHORIZATION)
    if auth_header_value is None:
        return response.status_bad_request('No Authorization header value')
    req = request.clone(headers={hdrs.CONTENT_TYPE: 'application/json',
                                 SUB: CREDENTIALS_MANAGER_USER,
                                 hdrs.AUTHORIZATION: auth_header_value
                                 })
    if not credential_id:
        return response.status_bad_request(body="credential id is required")

    try:
        key_lifespan: int = await _extract_key_lifespan(await request.json())
    except Exception as e:
        return response.status_bad_request(body="Invalid option for key duration")
    aws_cred = await _get_aws_cred(request)

    # if aws_cred.owner != CREDENTIALS_MANAGER_USER:
    #     return response.status_bad_request("Invalid source credential to make managed credential from")

    if aws_cred is None:
        return response.status_not_found("Could not get credential")
    if aws_cred.role is None:
        return response.status_bad_request('Cannot create managed credentials from these credentials: no role is defined')

    try:
        resource_url = await type_to_resource_url(request, Credentials)
        m_index = aws_cred.display_name.lower().rfind("managed")
        display_name = aws_cred.display_name[:m_index] if m_index > -1 else aws_cred.display_name
        r_index = aws_cred.role.rindex('/') + 1
        role_name = aws_cred.role[r_index:]
    except Exception as e:
        return response.status_bad_request(str(e))

    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-create',
                                            description=f'Creating Managed AWS CLI credentials for {aws_cred.display_name}',
                                            activity_cb=publish_desktop_object) as activity:
        # get client authorized by user's credentials
        # is this actually needed if the iam_client isn't used? investigate further
        async with aws.IAMClientContext(request=request, credentials=aws_cred) as _iam_client:
            if aws_cred.temporary and not aws_cred.managed:
                # now act as admin to do following steps
                loop = asyncio.get_running_loop()
                
                admin_cred = await request.app[HEA_DB].elevate_privileges(request, aws_cred)
                async with aws.IAMClientContext(request=req, credentials=admin_cred) as iam_admin_client:
                    try:
                        username = f"{sub}_{aws_cred.account_id}_{key_lifespan}"
                        r_policies = await loop.run_in_executor(None,
                                                                partial(iam_admin_client.list_attached_role_policies,
                                                                        RoleName=role_name))

                        cred_resp = await loop.run_in_executor(None, partial(_create_managed_user,
                                                                             iam_client=iam_admin_client,
                                                                             username=username,
                                                                             policies=r_policies))
                        _logger.debug("The credentials create on aws for %s with role %s ", username, role_name)
                        access_key = cred_resp['AccessKey']
                        aws_cred.display_name = f"{aws_cred.display_name} Managed {key_lifespan}hr"
                        aws_cred.name = username
                        aws_cred.owner = CREDENTIALS_MANAGER_USER
                        aws_cred.account = access_key['AccessKeyId']
                        aws_cred.password = access_key['SecretAccessKey']
                        aws_cred.created = access_key['CreateDate']
                        aws_cred.modified = access_key['CreateDate']
                        aws_cred.session_token = None
                        aws_cred.temporary = False
                        aws_cred.managed = True
                        share = ShareImpl()
                        share.user = sub
                        share.permissions = [Permission.VIEWER, Permission.DELETER]
                        aws_cred.shares = [share]

                        aws_cred.expiration = now() + timedelta(hours=key_lifespan)
                        _logger.debug("aws_cred ready to post: %s " % aws_cred.to_json())

                    except ClientError as ce:
                        activity.status = Status.FAILED
                        code = ce.response['Error']['Code']
                        if code == 'EntityAlreadyExists':
                            return response.status_bad_request(
                                "Credential already exists. Please select another duration option.")
                        try:
                            # clean up
                            await loop.run_in_executor(None,
                                                       partial(_delete_managed_user, iam_client=iam_admin_client,
                                                               username=username,
                                                               policies=r_policies,
                                                               access_key_id=access_key[
                                                                   'AccessKeyId'] if access_key else None))
                        except ClientError as c:
                            return response.status_bad_request(str(c))
                        except Exception as e:
                            return response.status_bad_request(str(e))
                        return response.status_bad_request(str(ce))


                    try:
                        result = await client.post(app=req.app, url=URL(resource_url), data=aws_cred, headers=req.headers)
                    except ClientResponseError as e:
                        activity.status = Status.FAILED
                        # clean up
                        if username and r_policies and access_key:
                            try:
                                await loop.run_in_executor(None,
                                                           partial(_delete_managed_user, iam_client=iam_admin_client,
                                                                   username=username,
                                                                   policies=r_policies,
                                                                   access_key_id=access_key[
                                                                       'AccessKeyId'] if access_key else None))
                            except ClientError as c:
                                return response.status_bad_request(str(c))
                            except Exception as e:
                                return response.status_bad_request(str(e))
                        return response.status_bad_request("Managed credentials were not created")
            elif aws_cred.managed:
                try:
                    aws_cred.expiration = now() + timedelta(hours=key_lifespan)
                    assert aws_cred.id is not None, 'aws_cred.id cannot be None'
                    await client.put(app=req.app, url=URL(resource_url)/aws_cred.id, data=aws_cred, headers=req.headers)
                except ClientResponseError as e:
                    activity.status = Status.FAILED
                    return response.status_bad_request(
                        f"Failed to extend managed credential {display_name}")
            else:
                activity.status = Status.FAILED
                return response.status_bad_request(f"This type of credential cannot be managed {display_name}")


            data = ClipboardData()
            data.mime_type = 'text/plain;encoding=utf-8'
            data.created = now()
            data.display_name = f'AWS CLI credentials file for {aws_cred.display_name}'
            with StringIO() as credentials_file:
                exp_local = aws_cred.expiration.astimezone().strftime("%m/%d/%Y %I:%M:%S %p %Z")


                credentials_file.writelines([
                    f'# {display_name}, expires at  {exp_local}\n'
                    '[tmp]\n',
                    f'aws_access_key_id = {aws_cred.account}\n',
                    f'aws_secret_access_key = {aws_cred.password}\n',
                    f'aws_session_token = {aws_cred.session_token}\n' if aws_cred.temporary else ''
                ])
                data.data = credentials_file.getvalue()
            return await response.get(request, data.to_dict())


@routes.post('/credentials/{id}/awsclicredentialsfile')
async def post_cli_credentials_file_form(request: web.Request) -> web.Response:
    try:
        aws_cred = await _get_aws_cred(request)
        if aws_cred is None:
            return response.status_not_found("Could not get credential")

        async with DesktopObjectActionLifecycle(request=request,
                                                code='hea-update',
                                                description=f'Getting AWS CLI credentials file for {aws_cred.display_name}',
                                                activity_cb=publish_desktop_object) as activity:

            if not aws_cred.managed:
                # It is being used to refresh credentials, is there a better way to do this
                async with aws.IAMClientContext(request=request, credentials=aws_cred):
                    # get credentials if refreshed after obtaining client
                    aws_cred = await _get_aws_cred(request)
                    assert aws_cred is not None, 'aws_cred should not be None by the time we reach this statement'

            data = ClipboardData()
            data.mime_type = 'text/plain;encoding=utf-8'
            data.created = now()
            data.display_name = f'AWS CLI credentials file for {aws_cred.display_name}'
            with StringIO() as credentials_file:
                # We should have an expiration by this point because the credentials were refreshed above.
                assert aws_cred.expiration is not None, 'aws_cred is missing an expiration'
                exp_local = aws_cred.expiration.astimezone().strftime("%m/%d/%Y %I:%M:%S %p %Z")

                credentials_file.writelines([
                    f'# {aws_cred.display_name}, expires at  {exp_local}\n',
                    '[tmp]\n',
                    f'aws_access_key_id = {aws_cred.account}\n',
                    f'aws_secret_access_key = {aws_cred.password}\n',
                    f'aws_session_token = {aws_cred.session_token}\n' if aws_cred.temporary else ''
                ])
                data.data = credentials_file.getvalue()
    except Exception as e:
        if activity:
            activity.status = Status.FAILED
        return response.status_bad_request("Failed to retrieve credential")

    return await response.get(request, data.to_dict())


@routes.put('/credentials/{id}')
async def put_credentials(request: web.Request) -> web.Response:
    """
    Updates the credentials with the specified id.
    :param request: the HTTP request.
    :return: a Response object with a status of No Content or Not Found.
    ---
    summary: Credentials updates
    tags:
        - heaserver-keychain-put-credentials
    parameters:
        - $ref: '#/components/parameters/id'
    requestBody:
      description: An updated credentials object.
      required: true
      content:
        application/vnd.collection+json:
          schema:
            type: object
          examples:
            example:
              summary: Credentials
              value: {
                "template": {
                  "data": [
                    {
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
                      "name": "name",
                      "value": "reximus"
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
                      "name": "id",
                      "value": "666f6f2d6261722d71757578"
                    },
                    {
                      "name": "type",
                      "value": "heaobject.keychain.Credentials"
                    }
                  ]
                }
              }
        application/json:
          schema:
            type: object
          examples:
            example:
              summary: An updated credentials object
              value: {
                "created": None,
                "derived_by": None,
                "derived_from": [],
                "name": "reximus",
                "description": None,
                "display_name": "Reximus Max",
                "invites": [],
                "modified": None,
                "owner": NONE_USER,
                "shares": [],
                "source": None,
                "type": "heaobject.keychain.Credentials",
                "version": None,
                "id": "666f6f2d6261722d71757578"
              }
    responses:
      '204':
        $ref: '#/components/responses/204'
      '400':
        $ref: '#/components/responses/400'
      '404':
        $ref: '#/components/responses/404'
    """
    return await mongoservicelib.put(request, MONGODB_CREDENTIALS_COLLECTION, Credentials)


@routes.delete('/credentials/{id}')
async def delete_credentials(request: web.Request) -> web.Response:
    """
    Deletes the credentials with the specified id.
    
    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: Credentials deletion
    tags:
        - heaserver-keychain-delete-credentials
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    cred_dict = await mongoservicelib.get_dict(request, MONGODB_CREDENTIALS_COLLECTION)
    cred = desktop_object_from_dict(cred_dict) if cred_dict is not None else None
    if cred is None or type(cred) != Credentials:
        not_found = True
    else:
        not_found = False
    id_ = request.match_info['id']
    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-delete',
                                            description=f"Deleting credential {cred.display_name if cred else 'with id ' + id_}",
                                            activity_cb=publish_desktop_object) as activity:
        activity.old_object_id = id_
        activity.old_object_type_name = Credentials.get_type_name()
        activity.old_object_uri = f'credentials/{id_}'
        if not_found:
            raise response.status_not_found()
        resp = await mongoservicelib.delete(request, MONGODB_CREDENTIALS_COLLECTION)  # we do this first to make sure the user has delete permissions.
        if resp.status != 204:
            activity.status = Status.FAILED
        return resp


@routes.delete('/awscredentials/{id}')
async def delete_awscredentials(request: web.Request) -> web.Response:
    """
    Deletes the AWS credentials with the specified id.
    
    :param request: the HTTP request.
    :return: No Content or Not Found.
    ---
    summary: AWS Credentials deletion
    tags:
        - heaserver-keychain-delete-awscredentials
    parameters:
        - $ref: '#/components/parameters/id'
    responses:
      '204':
        $ref: '#/components/responses/204'
      '404':
        $ref: '#/components/responses/404'
    """
    id_ = request.match_info['id']
    aws_cred = await _get_aws_cred(request)
    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-delete',
                                            description=f"Deleting AWS credential {aws_cred.display_name if aws_cred else 'with id ' + id_}",
                                            activity_cb=publish_desktop_object) as activity:
        activity.old_object_id = id_
        activity.old_object_type_name = AWSCredentials.get_type_name()
        activity.old_object_uri = f'awscredentials/{id_}'
        if aws_cred is None:
            raise response.status_not_found()
        resp = await mongoservicelib.delete(request, MONGODB_CREDENTIALS_COLLECTION)  # we do this first to make sure the user has delete permissions.
        if resp.status == 204 and aws_cred.managed:
            try:
                await _cleanup_deleted_managed_aws_credential(request, aws_cred)
            except (ValueError, ClientError) as e:
                raise response.status_bad_request(f"Unable to delete AWS managed credentials: {e}")
        if resp.status != 204:
            activity.status = Status.FAILED
        return resp


async def _cleanup_deleted_managed_aws_credential(request: web.Request, aws_cred: AWSCredentials):
    """
    Deletes all the managed credentials that were generated using the AWS credentials with the given ID.

    :param request: the HTTP request (required).
    :param aws_cred: a managed AWS credentials object (required).
    :raises ValueError: if an error occurred 
    :raises ClientError: if an error occurred contacting AWS.
    """
    loop = asyncio.get_running_loop()
    assert aws_cred.role is not None, 'aws_cred cannot have a None role'
    r_index = aws_cred.role.rindex('/') + 1
    role_name = aws_cred.role[r_index:]
    admin_cred = await request.app[HEA_DB].elevate_privileges(request, aws_cred)
    async with aws.IAMClientContext(request=request, credentials=admin_cred) as iam_admin_client:
        r_policies = await loop.run_in_executor(None,
                                                partial(iam_admin_client.list_attached_role_policies,
                                                        RoleName=role_name))
        assert aws_cred.name is not None, 'aws_cred.name cannot be None'
        await loop.run_in_executor(None, partial(_delete_managed_user, iam_client=iam_admin_client,
                                                    username=aws_cred.name,
                                                    policies=r_policies,
                                                    access_key_id=aws_cred.account))


async def _get_aws_credential_form(request: web.Request, managed: bool = False) -> web.Response:

    cred_dict = await mongoservicelib.get_dict(request, MONGODB_CREDENTIALS_COLLECTION)
    sub = request.headers.get(SUB, None)
    if cred_dict is None:
        return response.status_not_found()
    aws_cred = AWSCredentials()
    try:
        aws_cred.from_dict(cred_dict)
        if managed:
            if share := [s for s in aws_cred.shares if s.user == sub]:
                u = share[0].user
                s = ShareImpl()
                s.user = u
                s.permissions = [Permission.EDITOR, Permission.VIEWER]
                aws_cred.shares = [s]
                _logger.debug("share %s" % aws_cred.to_json())


    except DeserializeException as e:
        return response.status_bad_request(str(e))
    return await response.get(request, aws_cred.to_dict())


async def _credential_opener(request: web.Request) -> web.Response:
    """
    Returns links for opening the bucket. The volume id must be in the volume_id entry of the request's
    match_info dictionary. The bucket id must be in the id entry of the request's match_info dictionary.

    :param request: the HTTP request (required).
    :return: the HTTP response with a 200 status code if the bucket exists and a Collection+JSON document in the body
    containing an heaobject.bucket.AWSBucket object and links, 403 if access was denied, 404 if the bucket
    was not found, or 500 if an internal error occurred.
    """
    try:
        credential_id = request.match_info['id']
    except KeyError as e:
        return response.status_bad_request(str(e))
    sub = request.headers.get(SUB, NONE_USER)


    async with DesktopObjectActionLifecycle(request=request,
                                            code='hea-get',
                                            description=f'Accessing credentials {credential_id}',
                                            activity_cb=publish_desktop_object) as activity:
        head_cache_key = (sub, None, credential_id, 'head')
        actual_cache_key = (sub, None, credential_id, 'actual')
        if head_cache_key not in request.app[HEA_CACHE] and actual_cache_key not in request.app[HEA_CACHE]:
            try:
                activity.new_object_id = credential_id
                activity.new_object_type_name = Credentials.get_type_name()
                activity.new_object_uri = f'/credentials/{id}'
                request.app[HEA_CACHE][head_cache_key] = credential_id
            except BotoClientError as e:
                raise awsservicelib.handle_client_error(e)
        return await response.get_multiple_choices(request)


def _create_managed_user(iam_client: IAMClient, username: str,
                         policies: ListAttachedRolePoliciesResponseTypeDef) \
        -> CreateAccessKeyResponseTypeDef:
    resp = iam_client.create_user(UserName=username)
    for policy in policies['AttachedPolicies']:
        iam_client.attach_user_policy(UserName=username, PolicyArn=policy['PolicyArn'])
    cred_resp = iam_client.create_access_key(UserName=username)
    return cred_resp


def _delete_managed_user(iam_client: IAMClient, username: str,
                         policies: ListAttachedRolePoliciesResponseTypeDef | None = None,
                         access_key_id: str | None = None) \
        -> EmptyResponseMetadataTypeDef:
    if policies:
        for policy in policies['AttachedPolicies']:
            iam_client.detach_user_policy(UserName=username, PolicyArn=policy['PolicyArn'])

    if access_key_id:
        iam_client.delete_access_key(UserName=username, AccessKeyId=access_key_id)
    cred_resp = iam_client.delete_user(UserName=username)

    return cred_resp




async def _delete_managed_coro(app: web.Application):
    session = app[appproperty.HEA_CLIENT_SESSION]
    if not session:
        _logger.debug("session does not exist ")
        return

    try:
        headers_ = {SUB: CREDENTIALS_MANAGER_USER}
        component = await client.get_component_by_name(app, 'heaserver-keychain', client_session=session)
        assert component is not None, 'registry entry for heaserver-keychain not found'
        assert component.base_url is not None, 'registry entry for heaserver-keychain has no base_url'
        
        exp_aws_creds: list[AWSCredentials] = []
        async for cred in client.get_all(app=app, url=URL(component.base_url) / 'credentials',
                                         type_=AWSCredentials, headers=headers_):
            if cred.managed and cred.has_expired():
                exp_aws_creds.append(cred)

        _logger.debug("Managed Credentials to be deleted: %s", exp_aws_creds)

        coros_to_gather = []
        for exp_cred in exp_aws_creds:
            assert exp_cred.id is not None, 'exp_cred.id cannot be None'
            coros_to_gather.append(client.delete(app, URL(component.base_url) / 'credentials' / exp_cred.id, headers_))
        await asyncio.gather(*coros_to_gather)
    except Exception as ex:
        _logger.debug("an exception occurred", exc_info=ex)


async def _get_aws_cred(request: web.Request) -> AWSCredentials | None:
    aws_cred = AWSCredentials()
    try:
        cred_dict = await mongoservicelib.get_dict(request, MONGODB_CREDENTIALS_COLLECTION)
        if cred_dict is None:
            raise Exception("Could not get credential")
        aws_cred.from_dict(cred_dict)
    except (DeserializeException, Exception) as e:
        return None
    return aws_cred


async def _extract_key_lifespan(body: dict[str, Any]) -> int:
    """
    Extracts the target URL and expiration time for a presigned URL request. It un-escapes them
    as needed.

    :param body: a Collection+JSON template dict.
    :return: a three-tuple containing the target URL and the un-escaped expiration time in seconds.
    :raises web.HTTPBadRequest: if the given body is invalid.
    """
    try:
        key_lifespan = next(
            int(item['value']) for item in body['template']['data'] if item['name'] == 'key_lifespan')
        if key_lifespan not in [12, 24, 36, 48, 72]:
            _logger.info(f"the key_lifespan : {key_lifespan}")
            raise ValueError("Invalid lifespan for key")
        return key_lifespan
    except (KeyError, ValueError, StopIteration) as e:
        raise web.HTTPBadRequest(body=f'Invalid template: {e}') from e


def main() -> None:
    config = init_cmd_line(description='a service for managing laboratory/user credentials',
                           default_port=8080)
    start(package_name='heaserver-keychain', db=aws.S3WithMongoManager,
          wstl_builder_factory=builder_factory(__package__),
          cleanup_ctx=[publisher_cleanup_context_factory(config),
                       scheduled_cleanup_ctx(coro=_delete_managed_coro, delay=3600)],
          config=config)
