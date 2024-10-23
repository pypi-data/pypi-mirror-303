from typing import Optional, cast
import backoff
import socket

from arcane.datastore import Client as DatastoreClient
from arcane.core import BaseAccount, BadRequestError
from arcane.credentials import get_user_decrypted_credentials

from googleapiclient.errors import HttpError
from google.auth.exceptions import RefreshError
from google.oauth2 import service_account
from googleapiclient import discovery

from .helpers import get_mct_account
from .exception import MctAccountLostAccessException, MerchantCenterServiceDownException, get_exception_message


class MctClient:
    def __init__(
        self,
        gcp_service_account: str,
        base_account: Optional[BaseAccount] = None,
        mct_account: Optional[dict] = None,
        datastore_client: Optional[DatastoreClient] = None,
        gcp_project: Optional[str] = None,
        secret_key_file: Optional[str] = None,
        firebase_api_key: Optional[str] = None,
        auth_enabled: bool = True,
        clients_service_url: Optional[str] = None,
        user_email: Optional[str] = None
    ):
        scopes = ['https://www.googleapis.com/auth/content']
        creator_email = None
        if gcp_service_account and (mct_account or base_account or user_email):
            if user_email:
                creator_email = user_email
            else:
                if mct_account is None:
                    base_account = cast(BaseAccount, base_account)
                    mct_account = get_mct_account(
                        base_account=base_account,
                        clients_service_url=clients_service_url,
                        firebase_api_key=firebase_api_key,
                        gcp_service_account=gcp_service_account,
                        auth_enabled=auth_enabled
                    )

                creator_email = cast(str, mct_account['creator_email'])

            if creator_email is not None:
                if not secret_key_file:
                    raise BadRequestError('secret_key_file should not be None while using user access protocol')

                credentials = get_user_decrypted_credentials(
                    user_email=creator_email,
                    secret_key_file=secret_key_file,
                    gcp_credentials_path=gcp_service_account,
                    gcp_project=gcp_project,
                    datastore_client=datastore_client
                )
            else:
                credentials = service_account.Credentials.from_service_account_file(gcp_service_account, scopes=scopes)
        elif gcp_service_account:
            ## Used when posting an account using our credential (it is not yet in our database)
            credentials = service_account.Credentials.from_service_account_file(gcp_service_account, scopes=scopes)
        else:
            raise BadRequestError('one of the following arguments must be specified: gcp_service_account and (mct_account or base_account or user_email)')
        self.creator_email = creator_email
        self.service = discovery.build('content', 'v2.1', credentials=credentials, cache_discovery=False)

    @backoff.on_exception(backoff.expo, (socket.timeout), max_tries=3)
    def get_mct_account_details(
        self,
        merchant_id: int
    ):
        """
            From mct id check if user has access to it.
        """
        try:
            # Get account status alerts from MCT
            request_account_statuses = self.service.accounts().get(merchantId=merchant_id,
                                                            accountId=merchant_id)
            response_account_statuses = request_account_statuses.execute()
        # RefreshError is raised when we have invalid merchant_id or we don't have access to the account
        except RefreshError as err:
            raise MctAccountLostAccessException(get_exception_message(merchant_id, self.creator_email))
        except HttpError as err:
            if err.resp.status >= 400 and err.resp.status < 500:
                raise MctAccountLostAccessException(get_exception_message(merchant_id, self.creator_email))
            else:
                raise MerchantCenterServiceDownException(f"The Merchent Center API does not respond. Thus, we cannot check if we can access your Merchant Center account with the id: {merchant_id}. Please try later" )
        return response_account_statuses['name']

    @backoff.on_exception(backoff.expo, (socket.timeout), max_tries=3)
    def check_if_multi_client_account(
        self,
        merchant_id: int,
    ):
        """
            Sends an error if the account is a MCA
        """
        try:
            # This API method is only available to sub-accounts, thus it will fail if the merchant id is a MCA
            request_account_products = self.service.products().list(merchantId=merchant_id)
            response_account_statuses = request_account_products.execute()
        # RefreshError is raised when we have invalid merchant_id or we don't have access to the account
        except RefreshError as err:
            raise MctAccountLostAccessException(get_exception_message(merchant_id, self.creator_email))
        except HttpError as err:
            if err.resp.status >= 400 and err.resp.status < 500:
                raise MctAccountLostAccessException(f"This merchant id ({merchant_id} is for multi acccounts. You can only link sub-accounts.")
            else:
                raise MerchantCenterServiceDownException(f"The Merchent Center API does not respond. Thus, we cannot check if we can access your Merchant Center account with the id: {merchant_id}. Please try later" )
        return response_account_statuses


