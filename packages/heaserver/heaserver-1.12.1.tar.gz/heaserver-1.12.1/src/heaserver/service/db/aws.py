from abc import ABC, abstractmethod
from functools import partial
from aiohttp.web import Request
from aiohttp import ClientResponseError
import boto3
import botocore
from aiohttp import hdrs, web
from botocore.exceptions import ClientError, ParamValidationError
from mypy_boto3_iam import IAMClient
from mypy_boto3_s3 import S3Client, S3ServiceResource
from mypy_boto3_sts import STSClient
from mypy_boto3_account import AccountClient
from mypy_boto3_organizations import OrganizationsClient
from botocore.client import BaseClient
from ..appproperty import HEA_DB
from .database import DatabaseContextManager, MicroserviceDatabaseManager, get_credentials_from_volume, Database
from .mongo import Mongo
from ..oidcclaimhdrs import SUB
from ..sources import AWS as AWS_SOURCE
from heaobject.root import Permission
from heaobject.aws import S3Object, AWSDesktopObject
from heaobject.account import AWSAccount
from heaobject.keychain import AWSCredentials, Credentials
from heaobject.registry import Property
from heaobject.volume import AWSFileSystem, FileSystem
from heaobject.user import AWS_USER, CREDENTIALS_MANAGER_USER, NONE_USER
from heaobject.person import Person, AccessToken
from ..heaobjectsupport import type_to_resource_url, HEAServerPermissionContext
from ..util import async_retry, now, LockManager
from .. import client
from yarl import URL
from typing import Optional, TypeVar, cast, overload, Literal, Generic, TypedDict, NotRequired, Unpack
from configparser import ConfigParser
import asyncio
from threading import Lock
from collections.abc import Callable, Sequence, AsyncGenerator
from copy import copy, deepcopy
from .awsaction import *
from cachetools import TTLCache
from datetime import timedelta
from base64 import urlsafe_b64encode
from cachetools import TTLCache
import logging

CLIENT_ERROR_NO_SUCH_BUCKET = 'NoSuchBucket'
CLIENT_ERROR_ACCESS_DENIED = 'AccessDenied'
CLIENT_ERROR_ACCESS_DENIED2 = 'AccessDeniedException'
CLIENT_ERROR_FORBIDDEN = '403'
CLIENT_ERROR_404 = '404'
CLIENT_ERROR_ALL_ACCESS_DISABLED = 'AllAccessDisabled'
CLIENT_ERROR_NO_SUCH_KEY = 'NoSuchKey'
CLIENT_ERROR_INVALID_OBJECT_STATE = 'InvalidObjectState'

ServiceName = Literal['s3', 'iam', 'sts', 'account', 'organizations']

_boto3_client_lock = Lock()
_boto3_resource_lock = Lock()
_boto3_client_config = botocore.config.Config(max_pool_connections=25)

_permission_for = {
    S3_GET_OBJECT: Permission.VIEWER,
    S3_PUT_OBJECT: Permission.EDITOR,
    S3_DELETE_OBJECT: Permission.DELETER,
    S3_GET_OBJECT_TAGGING: Permission.VIEWER,
    S3_PUT_OBJECT_TAGGING: Permission.EDITOR,
    S3_LIST_BUCKET: Permission.VIEWER,
    S3_CREATE_BUCKET: Permission.EDITOR,
    S3_DELETE_BUCKET: Permission.DELETER,
    S3_GET_BUCKET_TAGGING: Permission.VIEWER,
    S3_PUT_BUCKET_TAGGING: Permission.EDITOR
}

class CreatorKwargs(TypedDict):
    region_name: NotRequired[str | None]
    aws_access_key_id: NotRequired[str | None]
    aws_secret_access_key: NotRequired[str | None]
    aws_session_token: NotRequired[str | None]

_S3Service = TypeVar('_S3Service', bound=BaseClient, covariant=True)
_ServiceNameTypeVar = TypeVar('_ServiceNameTypeVar', bound=ServiceName)

class S3(Database):
    """
    Connectivity to AWS (not just S3!) for HEA microservices.
    """
    # this is the buffer we give to refresh credentials in minutes on our end before they expire on aws
    MAX_EXPIRATION_LIMIT = 540
    MIN_EXPIRATION_LIMIT = 11

    # Min and max durations for assuming a role, such as in privilege elevation.
    MAX_DURATION_SECONDS = 43200
    MIN_DURATION_SECONDS = 900

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__locks: LockManager[str | None] = LockManager()
        self.__admin_creds: TTLCache[tuple[str, str], AWSCredentials] = TTLCache(maxsize=128, ttl=self.MIN_DURATION_SECONDS)  # (sub, role arn) -> AWSCredentials.
        self.__account_cache: TTLCache[tuple[str, str], AWSAccount] = TTLCache(maxsize=128, ttl=30)  # (sub, volume_id) -> AWSAccount.
        self.__sts_client: STSClient | None = None  # Global STS client for assuming roles.
        self.__sts_client_asyncio_lock = asyncio.Lock()
        self.__temp_cred_session_cache: TTLCache[str, boto3.session.Session] = TTLCache(maxsize=128, ttl=30)

    @property
    def file_system_type(self) -> type[FileSystem]:
        return AWSFileSystem

    async def update_credentials(self, request: Request, credentials: AWSCredentials) -> None:
        """
        Obtains the keychain microservice's url from the registry and executes a PUT call to update the credentials
        object. It executes the PUT call as the system|awscredentialsmanager user.

        :param request: the HTTP request (required).
        :param credentials: the AWS credentials to update (required). It must have been previously persisted.
        :raises ValueError: if there was a problem accessing the registry service or the credentials service was not
        found.
        :raises ClientResponseError: if there was a problem making the PUT request.
        """
        if credentials.id is None:
            raise ValueError(f'credentials must have a non-None id attribute')
        resource_url = await type_to_resource_url(request, Credentials)
        headers = {SUB: CREDENTIALS_MANAGER_USER}
        try:
            await client.put(app=request.app, url=URL(resource_url) / credentials.id, data=credentials,
                            headers=headers)
        except ClientResponseError as e:
            raise ValueError(f'Updating credentials failed: {e}') from e

    async def get_property(self, app: web.Application, name: str) -> Optional[Property]:
        """
        This is a wrapper function to be extended by tests
        Gets the Property with the given name from the HEA registry service.

        :param app: the aiohttp app.
        :param name: the property's name.
        :return: a Property instance or None (if not found).
        """
        return await client.get_property(app=app, name=name)

    @overload
    async def get_client(self, request: Request, service_name: Literal['s3'], volume_id: str | None = None,
                         credentials: AWSCredentials | None = None) -> S3Client:
        ...

    @overload
    async def get_client(self, request: Request, service_name: Literal['iam'], volume_id: str | None = None,
                         credentials: AWSCredentials | None = None) -> IAMClient:
        ...

    @overload
    async def get_client(self, request: Request, service_name: Literal['sts'], volume_id: str | None = None,
                         credentials: AWSCredentials | None = None) -> STSClient:
        ...

    @overload
    async def get_client(self, request: Request, service_name: Literal['account'], volume_id: str | None = None,
                         credentials: AWSCredentials | None = None) -> AccountClient:
        ...

    @overload
    async def get_client(self, request: Request, service_name: Literal['organizations'], volume_id: str | None = None,
                         credentials: AWSCredentials | None = None) -> OrganizationsClient:
        ...

    async def get_client(self, request: Request, service_name: ServiceName, volume_id: str | None = None,
                         credentials: AWSCredentials | None = None) -> S3Client | IAMClient | STSClient | AccountClient | OrganizationsClient:
        """
        Gets an AWS service client.  If the volume has no credentials, it uses the boto3 library to try and find them.
        This method is not designed to be overridden.

        :param request: the HTTP request (required).
        :param service_name: AWS service name (required).
        :param volume_id: the id string of a volume (required unless you pass a credentials object or you intend for
        boto3 to look up credentials information).
        :return: a Mongo client for the file system specified by the volume's file_system_name attribute. If no volume_id
        was provided, the return value will be the "default" Mongo client for the microservice found in the HEA_DB
        application-level property.
        :param credentials: optional AWSCredentials. If none is provided, boto3 will be used to look up credentials
        information.
        :raise ValueError: if there is no volume with the provided volume id, the volume's file system does not exist,
        the volume's credentials were not found, or a necessary service is not registered.

        TODO: need a separate exception thrown for when a service is not registered (so that the server can respond with a 500 error).
        TODO: need to lock around client creation because it's not threadsafe, manifested by sporadic KeyError: 'endpoint_resolver'.
        """
        if credentials is None and volume_id is not None:
            credentials = await self.get_credentials_from_volume(request, volume_id)
        match service_name:
            case 's3':
                return await self.__get_resource_or_client(request, 's3', create_client, credentials)
            case 'iam':
                return await self.__get_resource_or_client(request, 'iam', create_client, credentials)
            case 'sts':
                return await self.__get_resource_or_client(request, 'sts', create_client, credentials)
            case 'account':
                return await self.__get_resource_or_client(request, 'account', create_client, credentials)
            case 'organizations':
                return await self.__get_resource_or_client(request, 'organizations', create_client, credentials)
            case _:
                raise ValueError(f'Unexpected service_name {service_name}')

    # async def get_resource(self, request: Request, service_name: Literal['s3'], volume_id: str | None = None,
    #                        credentials: AWSCredentials | None = None) -> S3ServiceResource:
    #     """
    #     Gets an AWS resource. If the volume has no credentials, it uses the boto3 library to try and find them. This
    #     method is not designed to be overridden.

    #     :param request: the HTTP request (required).
    #     :param service_name: AWS service name (required).
    #     :param volume_id: the id string of a volume (required if a credentials object is not passed).
    #     :param credentials: optional AWSCredentials. If none is provided, boto3 will be used to look up credentials
    #     information.
    #     :return: a Mongo client for the file system specified by the volume's file_system_name attribute. If no volume_id
    #     was provided, the return value will be the "default" Mongo client for the microservice found in the HEA_DB
    #     application-level property.
    #     :raise ValueError: if there is no volume with the provided volume id, the volume's file system does not exist,
    #     the volume's credentials were not found, or a necessary service is not registered.

    #     TODO: need to lock around resource creation because it's not threadsafe, manifested by sporadic KeyError: 'endpoint_resolver'.
    #     """
    #     if credentials is None:
    #         if volume_id is None:
    #             raise ValueError('volume_id is required if credentials is None')
    #         credentials = await self.get_credentials_from_volume(request, volume_id)
    #     return await self.__get_resource_or_client(request, service_name, create_resource, credentials)

    async def has_account(self, request: Request, volume_id: str) -> bool:
        """
        Return whether the current user can access the AWS accounts associated with the provided volume_id.

        :param request: the HTTP request object (required).
        :param volume_id: the volume id (required).
        :return: True or False.
        :raises ValueError: if an error occured getting account information.
        """
        sub = request.headers.get(SUB, NONE_USER)
        key = (sub, volume_id)
        account = self.__account_cache.get(key)
        if account is None:
            try:
                async with STSClientContext(request, volume_id=volume_id) as sts_client:
                    account = await self._get_basic_account_info(sts_client)
            except ClientError as e:
                raise ValueError(f'Unexpected error getting account information for volume {volume_id}') from e
        return account is not None

    async def get_account(self, request: Request, volume_id: str) -> AWSAccount | None:
        """
        Gets the current user's AWS account associated with the provided volume_id.

        :param request: the HTTP request object (required).
        :param volume_id: the volume id (required).
        :return: the AWS account, or None if not found.
        :raises ValueError: if an error occurred getting account information.
        """
        logger = logging.getLogger(__name__)
        loop = asyncio.get_running_loop()
        credentials = await self.get_credentials_from_volume(request, volume_id)
        logger.debug('Got credentials %s for volume %s', credentials, volume_id)
        sub = request.headers.get(SUB, NONE_USER)
        key = (sub, volume_id)
        account = self.__account_cache.get(key)

        if account is None:
            try:
                async with STSClientContext(request, volume_id=volume_id, credentials=credentials) as sts_client:
                    account = await self._get_basic_account_info(sts_client)
                    self.__account_cache[key] = account
                    aid = account.id
            except ClientError:
                logger.debug(f'Error getting account for volume {volume_id}', exc_info=True)
                return None
        else:
            return deepcopy(account)

        async def populate_contact_info():
            try:
                async with AccountClientContext(request, credentials=credentials) as account_client:
                    contact_info = await loop.run_in_executor(None, partial(account_client.get_contact_information, AccountId=aid))
                    account.full_name = contact_info.get('FullName')
                    account.phone_number = contact_info.get('PhoneNumber')
            except ClientError as e:
                code = e.response['Error']['Code']
                if code != 'AccessDeniedException':
                    logger.exception('Client error %s', code)
                    raise ValueError(f'Unexpected error getting contact information for account {aid}') from e
                logger.debug('Account %s is not authorized to access contact information', aid, exc_info=True)

        async def populate_organization_info():
            try:
                async with OrganizationsClientContext(request, credentials=credentials) as org_client:
                    account_info = await loop.run_in_executor(None, partial(org_client.describe_account, AccountId=aid))
                    account_info_ = account_info['Account']
                    account.name = account_info_.get('Name')
                    account.email_address = account_info_.get('Email')
            except ParamValidationError:
                logger.debug('Account %s is not part of an organization', aid, exc_info=True)
            except ClientError as e:
                code = e.response['Error']['Code']
                if code != 'AccessDeniedException':
                    logger.exception('Client error %s', code)
                    raise ValueError(f'Unexpected error getting organization-level information for account {aid}') from e
                logger.debug('Account %s is not authorized to access organization-level account information',
                            aid, exc_info=True)

        await asyncio.gather(populate_contact_info(), populate_organization_info())

        # account.created = user['CreateDate']
        # FIXME this info coming from Alternate Contact(below) gets 'permission denied' with IAMUser even with admin level access
        # not sure if only root account user can access. This is useful info need to investigate different strategy
        # alt_contact_resp = account_client.get_alternate_contact(AccountId=account.id, AlternateContactType='BILLING' )
        # alt_contact =  alt_contact_resp.get("AlternateContact ", None)
        # if alt_contact:
        # account.full_name = alt_contact.get("Name", None)

        return account

    async def get_accounts(self, request: Request, volume_ids: Sequence[str]) -> AsyncGenerator[
        tuple[AWSAccount, str], None]:
        """
        Gets the AWS accounts associated with the provided volume ids.

        :param request: the HTTP request object (required).
        :param volume_ids: the volume ids (required).
        :return: an async generator of tuples containing the AWS accounts and corresponding volume ids.
        """
        logger = logging.getLogger(__name__)

        async def execute(volume_id: str) -> tuple[AWSAccount | None, str]:
            return await self.get_account(request, volume_id), volume_id

        for i, acct_vol in enumerate(await asyncio.gather(*(execute(volume_id) for volume_id in volume_ids),
                                                                return_exceptions=True)):
            if not isinstance(acct_vol, tuple):
                if isinstance(acct_vol, ValueError):
                    logger.error('Error getting account for volume %s', volume_ids[i], exc_info=acct_vol)
                    continue
                else:
                    raise acct_vol
            acct, vol = acct_vol
            if acct is not None:
                yield acct, vol

    async def generate_cloud_credentials(self, request: Request, arn: str, session_name: str,
                                         duration: int | None = None) -> AWSCredentials:
        """
        Create temporary credentials and return a newly created AWSCredentials object. If the user who made the request
        is system|credentialsmanager, which can only happen in internal calls between microservices where the only
        available Authorization header would be from the logged-in user, a token is requested from the people service
        to use for assuming an AWS role. Otherwise, the Bearer token passed in the request in the Authorization header
        or the access_token query parameter is used to assume the role.

        :param request: the HTTP request (required).
        :param arn: The aws role arn that to be assumed (required).
        :param session_name: the session name to pass into AWS (required; typically is the user sub).
        :param duration: the time in seconds to assume the role. If None, it uses a default value, MIN_DURATION_SECONDS
        if the user is system|credentialsmanager, otherwise MAX_DURATION_SECONDS. The minimum is MIN_DURATION_SECONDS.
        :returns: an AWSCredentials object with the generated credentials.
        :raises ValueError: if an error occurs generating cloud credentials.
        """
        logger = logging.getLogger(__name__)
        sub = request.headers.get(SUB, None)
        if duration is None:
            duration = self.MIN_DURATION_SECONDS if sub == CREDENTIALS_MANAGER_USER else self.MAX_DURATION_SECONDS

        logger.debug("In generate_credentials sub is %s" % sub)
        if sub is None:
            raise ValueError('OIDC SUB header is required')
        if not arn:
            raise ValueError('Cannot get credentials arn which is required')

        logger.debug('Getting credentials for user %s with role %s...', sub, arn)
        try:
            if sub == CREDENTIALS_MANAGER_USER:
                resource_url = await type_to_resource_url(request, Person)
                logger.debug("url for token for people: %s" % (URL(resource_url) / 'internal' / 'token'))
                token_obj = await client.get(app=request.app, type_or_obj=AccessToken,
                                            url=URL(resource_url) / 'internal' / 'token',
                                            headers=request.headers)
                if token_obj is None:
                    raise ValueError('Internal token not found')
                if token_obj.auth_scheme is None:
                    raise ValueError("Internal token's auth_scheme cannot be None")
                if token_obj.id is None:
                    raise ValueError("Internal token's id cannot be None")
                auth_token = [token_obj.auth_scheme, token_obj.id]
            else:
                auth = request.headers.get(hdrs.AUTHORIZATION, '')
                auth_token = auth.split(' ')
                if len(auth_token) != 2:
                    access_token = request.query.get('access_token')
                    if access_token:
                        auth_token = ['Bearer', access_token]

            if len(auth_token) != 2:
                raise ValueError(f"Authorization token is required but was {auth_token}")

            logger.debug('User %s has role %s', sub, arn)
            loop = asyncio.get_running_loop()

            @async_retry(ClientError)
            async def call_assume_role_with_web_identity():
                sts_client = await self.__get_sts_client(loop)
                logger.debug('Assuming role %s for duration %s', arn, duration)
                return await loop.run_in_executor(None, partial(sts_client.assume_role_with_web_identity,
                                                                WebIdentityToken=auth_token[1],
                                                                RoleArn=arn,
                                                                RoleSessionName=urlsafe_b64encode(session_name.encode('utf-8')).decode('utf-8'),
                                                                DurationSeconds=duration))
            assumed_role_object = await call_assume_role_with_web_identity()
        except ClientError as ce:
            raise ValueError(f'User {sub} does not have role {arn}') from ce
        except ClientResponseError as cre:
            raise ValueError('Token cannot be obtained') from cre
        except Exception as e:
            raise ValueError('Error generating cloud credentials') from e
        creds_dict = assumed_role_object.get('Credentials')
        if not creds_dict:
            raise ValueError('No credentials returned from AWS')
        creds = AWSCredentials()
        creds.account = creds_dict['AccessKeyId']
        creds.password = creds_dict['SecretAccessKey']
        creds.session_token = creds_dict['SessionToken']
        creds.role = arn
        creds.temporary = True
        creds.expiration = creds_dict['Expiration']

        return creds

    def close(self):
        super().close()
        if self.__sts_client is not None:
            self.__sts_client.close()

    async def get_credentials_from_volume(self, request: web.Request, volume_id: str) -> AWSCredentials | None:
        """
        Gets the volume's credentials.

        :param request: the HTTP request (required).
        :param volume_id: the volume id (required).
        :return a Credentials object, or None if no credentials were found.
        :raises ValueError: if no volume with that id exists
        """
        return await get_credentials_from_volume(request, volume_id, credential_type=AWSCredentials)

    async def elevate_privileges(self, request: web.Request, credentials: AWSCredentials,
                                 lifespan: int | None = None) -> AWSCredentials:
        """
        Returns an ephemeral credentials object with admin-level privileges for the same account as the given user
        credentials object. It relies on the registry service's AWS_ADMIN_ROLE property being set to the AWS admin
        role, otherwise this method will raise a ValueError. After generating the credentials, it will return the same
        credentials until close to its expiration.

        If the user who made the request is system|credentialsmanager, which can only happen in internal calls between
        microservices where the only available Authorization header would be from the logged-in user, a token is
        requested from the people service to use for assuming an AWS role. Otherwise, the Bearer token passed in the
        request in the Authorization header or the access_token query parameter is used to assume the role.

        :param request: the HTTP request (required).
        :param aws_cred: the user's AWS credentials.
        :param lifespan: the length of privilege elevation in seconds. If None, a default value is used,
        MIN_DURATION_SECONDS. The minimum value is MIN_DURATION_SECONDS.
        :return: the account id and an ephemeral credentials object. The credentials object's role attribute cannot be
        None.
        :raises ValueError: if privilege elevation failed.
        """
        sub = request.headers.get(SUB, NONE_USER)
        if lifespan is None:
            lifespan = self.MIN_DURATION_SECONDS
        assert credentials.role is not None, 'credentials.role cannot be None'
        admin_role = await self.__get_admin_aws_role_arn(request, credentials.role)
        key = (sub, admin_role)
        admin_cred = self.__admin_creds.get(key)
        if admin_cred is None or admin_cred.has_expired(1):
            admin_cred = await self.generate_cloud_credentials(request, admin_role, sub, duration=lifespan)
            self.__admin_creds[key] = admin_cred
            admin_cred.expiration = now() + timedelta(seconds=lifespan)
        return deepcopy(admin_cred)

    @staticmethod
    async def _get_basic_account_info(sts_client: STSClient) -> AWSAccount:
        """
        Gets basic account info from AWS.

        :param sts_client: the STS client to use.
        :return: the AWS account.
        :raises ClientError: if there was an error getting the account info.
        """
        loop = asyncio.get_running_loop()
        identity = await loop.run_in_executor(None, sts_client.get_caller_identity)
        logger = logging.getLogger(__name__)
        logger.debug('Caller identity: %s', identity)
        # user_future = loop.run_in_executor(None, iam_client.get_user)
        # await asyncio.wait([identity_future])  # , user_future])
        aid = identity['Account']
        # aws_object_dict['alias'] = next(iam_client.list_account_aliases()['AccountAliases'], None)  # Only exists for IAM accounts.
        # user = user_future.result()['User']
        # aws_object_dict['account_name'] = user.get('UserName')  # Only exists for IAM accounts.
        account = AWSAccount()
        account.id = aid
        account.name = aid
        account.display_name = aid
        account.owner = AWS_USER
        account.source = AWS_SOURCE
        account.source_detail = AWS_SOURCE
        account.type_display_name
        account.file_system_type = AWSFileSystem.get_type_name()
        account.credential_type_name = AWSCredentials.get_type_name()
        return account

    async def __get_resource_or_client(self, request: Request, service_name: _ServiceNameTypeVar,
                                       creator: Callable[[_ServiceNameTypeVar, Unpack[CreatorKwargs]], _S3Service],
                                       credentials: AWSCredentials | None) -> _S3Service:
        """
        Gets an S3 resource or client.

        :param request: the HTTP request (required).
        :param service_name: the name of the S3 service (required).
        :param creator: the function for creating the resource or client (create_resource or create_client).
        :param credentials: the AWSCredentials object, or None to let boto3 find the credentials.

        :raises ValueError: if updating temporary credentials failed.
        """
        logger = logging.getLogger(__name__)
        logger.debug("credentials retrieved from database checking if expired: %r", credentials)
        loop = asyncio.get_running_loop()
        if not credentials:  # delegate to boto3 to find the credentials
            return await loop.run_in_executor(None, creator, service_name)
        elif credentials.temporary:
            return await self.__get_temporary_credentials(request=request,
                                                            credentials=credentials,
                                                            creator=creator,
                                                            service_name=service_name)
        else:  # for permanent credentials
            return await loop.run_in_executor(None, partial(creator, service_name,
                                                            region_name=credentials.where,
                                                            aws_access_key_id=credentials.account,
                                                            aws_secret_access_key=credentials.password))


    async def __get_temporary_credentials(self, request: web.Request, credentials: AWSCredentials,
                                          creator: Callable[[_ServiceNameTypeVar, Unpack[CreatorKwargs]], _S3Service],
                                          service_name: _ServiceNameTypeVar) -> _S3Service:
        """
        Assumes the provided temporary credentials' role and returns an AWS client. If the temporary credentials have
        expired, it updates them. If the temporary credentials were previously persisted, it persists the updates.

        If the user who made the request is system|credentialsmanager, which can only happen in internal calls between
        microservices where the only available Authorization header would be from the logged-in user, a token is
        requested from the people service to use for assuming an AWS role. Otherwise, the Bearer token passed in the
        request in the Authorization header or the access_token query parameter is used to assume the role.

        :param request: the aiohttp request
        :param credentials: the aws credentials.
        :param creator: a callable that invokes either the boto3.get_client or boto3.get_resource functions and returns
        the client.
        :param service_name: The type of client to return
        :return: the boto3 client provided with credentials
        :raise ValueError if no previously saved credentials it raises ValueError
        """
        logger = logging.getLogger(__name__)
        assert credentials.role is not None, 'credentials must have a non-None role attribute'
        loop = asyncio.get_running_loop()
        sub = request.headers.get(SUB, NONE_USER)

        async with self.__locks.lock(credentials.id):
            logger.debug("checking if credentials for service %s %r for user %s need to be refreshed, right before", service_name, credentials, sub)
            if credentials.has_expired(1):
                logger.debug("credentials for service %s %r need to be refreshed", service_name, credentials)
                cloud_creds = await self.generate_cloud_credentials(request, credentials.role, sub)
                logger.debug("Credentials for service %s successfully obtained from cloud: %r", service_name, cloud_creds)
                credentials.account = cloud_creds.account
                credentials.password = cloud_creds.password
                credentials.session_token = cloud_creds.session_token
                credentials.expiration = cloud_creds.expiration
                if credentials.id is not None:
                    update_task: asyncio.Task[None] | None = asyncio.create_task(self.update_credentials(request=request, credentials=credentials))
                else:
                    update_task = None
                logger.debug("Credentials %r updated in the database", credentials)
            else:
                update_task = None
            assert credentials.account is not None, 'credentials.account is None unexpectedly'
            if (session := self.__temp_cred_session_cache.get(credentials.account)) is None:
                session = boto3.session.Session(region_name=credentials.where, aws_access_key_id=credentials.account,
                                                aws_secret_access_key=credentials.password,
                                                aws_session_token=credentials.session_token)
                self.__temp_cred_session_cache[credentials.account] = session
            if creator == create_client:
                client_ = await loop.run_in_executor(None, partial(session.client, service_name, config=_boto3_client_config))
            else:
                client_ = await loop.run_in_executor(None, partial(session.resource, service_name, config=_boto3_client_config))
            if update_task is not None:
                await update_task
            return client_

    async def __get_admin_aws_role_arn(self, request: web.Request, arn: str) -> str:
        """
        Generates an admin role ARN from the current user's role ARN, replacing the role part of the ARN with the value of
        the AWS_ADMIN_ROLE property in the heaserver-registry service.

        :param request: the HTTP request.
        :param arn: the current user's role ARN.
        :return: an admin role ARN for that account.
        :raises ValueError: if no AWS_ADMIN_ROLE property was found.
        :raises IndexError: if the input arn is malformed.
        """
        admin_role_prop: Optional[Property] = await self.get_property(app=request.app, name="AWS_ADMIN_ROLE")
        if not admin_role_prop or not admin_role_prop.value:
            raise ValueError("Admin role property not found")
        admin_role_name = admin_role_prop.value
        r_index = arn.rindex('/') + 1
        arn_prefix = arn[:r_index]

        return f"{arn_prefix}{admin_role_name}"

    async def __get_sts_client(self, loop: asyncio.AbstractEventLoop | None = None):
        logger = logging.getLogger(__name__)
        logger.debug('Getting sts client')
        async with self.__sts_client_asyncio_lock:
            logger.debug('Passed asyncio lock')
            try:
                if self.__sts_client is None:
                    logger.debug('Attempting to get sts client')
                    loop_ = asyncio.get_running_loop() if loop is None else loop
                    def get_client():
                        with _boto3_client_lock:
                            return boto3.client('sts', config=_boto3_client_config)
                    self.__sts_client = await loop_.run_in_executor(None, get_client)
                logger.debug('Returning sts client')
                return self.__sts_client
            except ClientError as e:
                self.__sts_client = None
                raise e
            except:
                logger.exception('Got exception attempting to create sts client')
                raise


class S3WithMongo(S3, Mongo):
    def __init__(self, config: Optional[ConfigParser], **kwargs):
        super().__init__(config, **kwargs)


class S3Manager(MicroserviceDatabaseManager):
    """
    Database manager for mock Amazon Web Services S3 buckets. It will not make any calls to actual S3 buckets. This
    class is not designed to be subclassed.
    """

    def get_database(self) -> Database:
        return S3(self.config)

    @classmethod
    def database_types(self) -> list[str]:
        return ['system|awss3']


class S3WithMongoManager(S3Manager):

    def get_database(self) -> S3:
        return S3WithMongo(self.config)


class S3ClientContext(DatabaseContextManager[S3Client, AWSCredentials]):  # Go into db package?
    """
    Provides an S3 client.
    """

    def __init__(self, request: web.Request, volume_id: str | None = None, credentials: AWSCredentials | None = None):
        """
        Creates an object for getting an S3 client. Either a volume_id or a credentials object must be provided. If a
        volume_id is provided but not a credentials object, the credentials object will be retrieved from the keychain
        microservice.

        :param request: the HTTP request (required).
        :param volume_id: a volume id. Either a volume id or a credentials object must be provided.
        :param credentials: an AWS credentials object. Either a volume_id or a credentials object must be provided.
        """
        super().__init__(request, volume_id, credentials)

    async def connection(self) -> S3Client:
        return await cast(S3, self.request.app[HEA_DB]).get_client(self.request, 's3', self.volume_id, self.credentials)


class IAMClientContext(DatabaseContextManager[IAMClient, AWSCredentials]):  # Go into db package?
    """
    Provides an IAM client.
    """

    def __init__(self, request: web.Request, volume_id: str | None = None, credentials: AWSCredentials | None = None):
        """
        Creates an object for getting an IAM client. Either a volume_id or a credentials object must be provided. If a
        volume_id is provided but not a credentials object, the credentials object will be retrieved from the keychain
        microservice.

        :param request: the HTTP request (required).
        :param volume_id: a volume id. Either a volume id or a credentials object must be provided.
        :param credentials: an AWS credentials object. Either a volume_id or a credentials object must be provided.
        """
        super().__init__(request, volume_id, credentials)

    async def connection(self) -> IAMClient:
        """
        Returns an IAM client.

        :return: an IAM client.
        """
        return await cast(S3, self.request.app[HEA_DB]).get_client(self.request, 'iam', self.volume_id, self.credentials)


class STSClientContext(DatabaseContextManager[STSClient, AWSCredentials]):  # Go into db package?
    """
    Provides an STS client.
    """

    def __init__(self, request: web.Request, volume_id: str | None = None, credentials: AWSCredentials | None = None):
        """
        Creates an object for getting an STS client. Either a volume_id or a credentials object must be provided. If a
        volume_id is provided but not a credentials object, the credentials object will be retrieved from the keychain
        microservice.

        :param request: the HTTP request (required).
        :param volume_id: a volume id. Either a volume id or a credentials object must be provided.
        :param credentials: an AWS credentials object. Either a volume_id or a credentials object must be provided.
        """
        super().__init__(request, volume_id, credentials)

    async def connection(self) -> STSClient:
        """
        Returns an STS client.

        :return: an STS client.
        """
        return await cast(S3, self.request.app[HEA_DB]).get_client(self.request, 'sts', self.volume_id, self.credentials)


class AccountClientContext(DatabaseContextManager[AccountClient, AWSCredentials]):
    """
    Provides an Account client.
    """

    def __init__(self, request: web.Request, volume_id: str | None = None, credentials: AWSCredentials | None = None):
        """
        Creates an object for getting an Account client. Either a volume_id or a credentials object must be provided.
        If a volume_id is provided but not a credentials object, the credentials object will be retrieved from the
        keychain microservice.

        :param request: the HTTP request (required).
        :param volume_id: a volume id. Either a volume id or a credentials object must be provided.
        :param credentials: an AWS credentials object. Either a volume_id or a credentials object must be provided.
        """
        super().__init__(request, volume_id, credentials)

    async def connection(self) -> AccountClient:
        """
        Returns an Account client.

        :return: an Account client.
        """
        return await cast(S3, self.request.app[HEA_DB]).get_client(self.request, 'account', self.volume_id, self.credentials)


class OrganizationsClientContext(DatabaseContextManager[OrganizationsClient, AWSCredentials]):
    """
    Provides an Organizations client.
    """

    def __init__(self, request: web.Request, volume_id: str | None = None, credentials: AWSCredentials | None = None):
        """
        Creates an object for getting an Organization client. Either a volume_id or a credentials object must be
        provided. If a volume_id is provided but not a credentials object, the credentials object will be retrieved
        from the keychain microservice.

        :param request: the HTTP request (required).
        :param volume_id: a volume id. Either a volume id or a credentials object must be provided.
        :param credentials: an AWS credentials object. Either a volume_id or a credentials object must be provided.
        """
        super().__init__(request, volume_id, credentials)

    async def connection(self) -> OrganizationsClient:
        """
        Returns an Organization client.

        :return: an Organization client.
        """
        return await cast(S3, self.request.app[HEA_DB]).get_client(self.request, 'organizations', self.volume_id, self.credentials)


@overload
def create_client(service_name: Literal['s3'],
                  **kwargs: Unpack[CreatorKwargs]) -> S3Client:
    ...

@overload
def create_client(service_name: Literal['iam'],
                  **kwargs: Unpack[CreatorKwargs]) -> IAMClient:
    ...

@overload
def create_client(service_name: Literal['sts'],
                  **kwargs: Unpack[CreatorKwargs]) -> STSClient:
    ...


@overload
def create_client(service_name: Literal['account'],
                  **kwargs: Unpack[CreatorKwargs]) -> AccountClient:
    ...


@overload
def create_client(service_name: Literal['organizations'],
                  **kwargs: Unpack[CreatorKwargs]) -> OrganizationsClient:
    ...


def create_client(service_name: ServiceName,
                  **kwargs: Unpack[CreatorKwargs]) -> S3Client | IAMClient | STSClient | AccountClient | OrganizationsClient:
    """
    Thread-safe boto client creation. Once created, clients are generally thread-safe.

    :raises ValueError: if an error occurred getting the S3 client.
    """
    with _boto3_client_lock:
        return boto3.client(service_name,
                            region_name=kwargs.get('region_name'),
                            aws_access_key_id=kwargs.get('aws_access_key_id'),
                            aws_secret_access_key=kwargs.get('aws_secret_access_key'),
                            aws_session_token=kwargs.get('aws_session_token'),
                            config=_boto3_client_config)


def create_resource(service_name: Literal['s3'],
                    **kwargs: Unpack[CreatorKwargs]) -> S3ServiceResource:
    """
    Thread-safe boto resource creation. Resources are generally NOT thread-safe!

    :raises ValueError: if an error occurred getting the S3 resource.
    """
    with _boto3_resource_lock:
        return boto3.resource(service_name,
                              region_name=kwargs.get('region_name'),
                              aws_access_key_id=kwargs.get('aws_access_key_id'),
                              aws_secret_access_key=kwargs.get('aws_secret_access_key'),
                              aws_session_token=kwargs.get('aws_session_token'),
                              config=_boto3_client_config)


AWSDesktopObjectTypeVar = TypeVar('AWSDesktopObjectTypeVar', bound=AWSDesktopObject)

class AWSPermissionContext(HEAServerPermissionContext[AWSDesktopObjectTypeVar], ABC, Generic[AWSDesktopObjectTypeVar]):
    """
    Helper class for desktop objects' permissions-related methods that require external information, such as the
    current user.
    """
    _logger = logging.getLogger(__name__)

    def __init__(self, request: Request, volume_id: str, actions: Sequence[str], **kwargs):
        """
        Accepts an HTTP Request, a volume id, and actions to check. Any additional keyword
        arguments will be passed onto the next class in the method resolution order.
        """
        if request is None:
            raise ValueError('request is required')
        sub = request.headers.get(SUB, NONE_USER)
        super().__init__(sub=sub, request=request, **kwargs)
        self.__volume_id = str(volume_id)
        self.__actions = copy(actions)
        self.__credentials: AWSCredentials | None = None
        self.__is_account_owner: bool | None = None
        self.__cache: TTLCache[str, list[Permission]] = TTLCache(maxsize=128, ttl=30)
        self.__credentials_lock = asyncio.Lock()
        self.__get_perms_locks: LockManager[str] = LockManager()

    @property
    def volume_id(self) -> str:
        """The id of the volume."""
        return self.__volume_id

    async def credentials(self) -> AWSCredentials:
        async with self.__credentials_lock:
            if self.__credentials is None:
                self._logger.debug('Getting credentials to check permissions')
                self.__credentials = cast(AWSCredentials,
                            await cast(S3, self.request.app[HEA_DB]).get_credentials_from_volume(self.request, self.volume_id))
            return deepcopy(self.__credentials)

    async def is_account_owner(self) -> bool:
        """
        Returns whether the user who submitted the request is the owner of the AWS account associated with the volume.
        """
        if self.__is_account_owner is None:
            self.__is_account_owner = await is_account_owner(self.request, credentials=await self.credentials())
        return self.__is_account_owner

    async def get_permissions(self, obj: AWSDesktopObjectTypeVar) -> list[Permission]:
        """
        Gets the user's permissions for a desktop object. This default implementation delegates to the object's
        _default_get_permissions() method.

        :param obj: the desktop object (required).
        :return: a list of Permissions, or the empty list if there is none.
        """
        logger = logging.getLogger(__name__)
        logger.debug('Getting permissions for desktop object %r', obj)
        obj_str = repr(obj)
        async with self.__get_perms_locks.lock(obj_str):  # don't need to cache on sub because the sub can't be changed.
            perms = self.__cache.get(obj_str)
            if perms is None:
                if not await self.is_account_owner():
                    perms = await self._simulate_perms(obj, self.__actions)
                else:
                    perms = [Permission.COOWNER]
                self.__cache[obj_str] = perms
            logger.debug('Got permissions %s for desktop object %r', perms, obj)
            return copy(perms)

    async def _simulate_perms(self, obj: AWSDesktopObjectTypeVar, actions: Sequence[str]) -> list[Permission]:
        logger = logging.getLogger(__name__)
        credentials = await self.credentials()
        try:
            logger.debug('Elevating privileges to check permissions for desktop object %r', obj)
            admin_credentials = await self.request.app[HEA_DB].elevate_privileges(self.request, credentials)
        except ValueError:
            logger.exception("Error getting elevated privileges, will fall back to the user's privileges")
            admin_credentials = credentials
        logger.debug('Privileges for simulating permissions are %r for desktop object %r', admin_credentials, obj)
        perms: list[Permission] = []
        async with IAMClientContext(request=self.request, credentials=admin_credentials) as iam_client:
            loop = asyncio.get_running_loop()
            try:
                assert credentials.role is not None, 'role attribute cannot be None'
                logger.debug('Checking permissions')
                response_ = await loop.run_in_executor(None, partial(iam_client.simulate_principal_policy,
                                                                     PolicySourceArn=credentials.role,
                                                                     ActionNames=actions,
                                                                     CallerArn=self._caller_arn(obj)))
                logger.debug('Response for checking %s: %s', actions, response_)
                for results in response_['EvaluationResults']:
                    if results['EvalDecision'] == 'allowed':
                        if perm := _permission_for.get(results['EvalActionName']):
                            perms.append(perm)
            except ClientError as e:
                status, _ = client_error_status(e)
                if status == 403:
                    logger.exception("Access denied simulating the user's privileges; falling back to pretending the user has full access "
                                     "(AWS will deny them when they try to do something they lack permission to do)")
                    perms.extend([Permission.VIEWER, Permission.EDITOR, Permission.DELETER])
                else:
                    raise e
        return perms

    @abstractmethod
    def _caller_arn(self, obj: AWSDesktopObjectTypeVar) -> str:
        pass

class S3ObjectPermissionContext(AWSPermissionContext[S3Object]):
    def __init__(self, request: Request, volume_id: str, **kwargs):
        actions = [S3_GET_OBJECT, S3_PUT_OBJECT, S3_DELETE_OBJECT]
        super().__init__(request=request, volume_id=volume_id, actions=actions, **kwargs)

    async def get_attribute_permissions(self, obj: S3Object, attr: str) -> list[Permission]:
        if attr == 'tags' and not await self.is_account_owner():
            return await self._simulate_perms(obj, [S3_GET_OBJECT_TAGGING, S3_PUT_OBJECT_TAGGING])
        else:
            return await super().get_attribute_permissions(obj, attr)

    def _caller_arn(self, obj: S3Object):
        return f'arn:aws:s3:::{obj.bucket_id}/{obj.key}'


async def is_account_owner(request: Request, volume_id: str | None = None, credentials: AWSCredentials | None = None) -> bool:
    logger = logging.getLogger(__name__)
    async with STSClientContext(request=request, volume_id=volume_id, credentials=credentials) as sts_client:
        caller_identity_resp = sts_client.get_caller_identity()
        logger.debug('caller identity: %s', caller_identity_resp)
        caller_identity_arn = caller_identity_resp['Arn']
        caller_identity_arn_split = caller_identity_arn.split(':')
        return not caller_identity_arn_split[5].startswith('assumed-role')


def client_error_status(e: ClientError) -> tuple[int, str]:
    """
    Translates a boto3 client error into an appropriate HTTP response status code.

    :param e: a boto3 client error (required).
    :return: a HTTP status code and a message.
    """
    logger = logging.getLogger(__name__)
    error_code = e.response['Error']['Code']
    if error_code in (CLIENT_ERROR_404, CLIENT_ERROR_NO_SUCH_BUCKET, CLIENT_ERROR_NO_SUCH_KEY):  # folder doesn't exist
        return 404, ''
    elif error_code in (CLIENT_ERROR_ACCESS_DENIED, CLIENT_ERROR_ACCESS_DENIED2, CLIENT_ERROR_FORBIDDEN, CLIENT_ERROR_ALL_ACCESS_DISABLED):
        return 403, ''
    elif error_code == CLIENT_ERROR_INVALID_OBJECT_STATE:
        return 400, str(e)
    else:
        logger.exception('Unexpected boto3 client error %s', error_code)
        return 500, str(e)


