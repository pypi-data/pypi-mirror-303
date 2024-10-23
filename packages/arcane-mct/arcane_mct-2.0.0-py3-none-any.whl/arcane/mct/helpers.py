from typing import Optional

from arcane.core import BaseAccount, BadRequestError, UserRightsEnum, RightsLevelEnum
from arcane.requests import call_get_route

def get_mct_account(
    base_account: BaseAccount,
    clients_service_url: Optional[str] = None,
    firebase_api_key: Optional[str] = None,
    gcp_service_account: Optional[str] = None,
    auth_enabled: bool = True
) -> dict:
    """Call get endpoint to retrieve mct account

    Args:
        base_account (BaseAccount): base account to get
        clients_service_url (Optional[str], optional): clients service url to call. Defaults to None.
        firebase_api_key (Optional[str], optional): needed for calling api. Defaults to None.
        gcp_service_account (Optional[str], optional): needed for calling api. Defaults to None.
        auth_enabled (bool, optional): Boolean to know if we should use token while calling api. Defaults to True.

    Raises:
        BadRequestError: The request does not comply function requirement. See error message for more info

    Returns:
        dict: mct account
    """
    if not (clients_service_url and firebase_api_key and gcp_service_account):
        raise BadRequestError('clients_service_url or firebase_api_key or gcp_service_account should not be None if mct account is not provided')
    url = f"{clients_service_url}/api/mct-account?account_id={base_account['id']}&client_id={base_account['client_id']}"
    accounts = call_get_route(
        url,
        firebase_api_key,
        claims={'features_rights': { UserRightsEnum.AMS_GTP: RightsLevelEnum.VIEWER }, 'authorized_clients': ['all']},
        auth_enabled=auth_enabled,
        credentials_path=gcp_service_account
    )
    if len(accounts) == 0:
        raise BadRequestError(f'Error while getting mct account with: {base_account}. No account corresponding.')
    elif len(accounts) > 1:
        raise BadRequestError(f'Error while getting mct account with: {base_account}. Several account corresponding: {accounts}')

    return accounts[0]
