from typing import Optional

class MctAccountLostAccessException(Exception):
    """Raised when we cannot access to an account."""
    pass


class MerchantCenterServiceDownException(Exception):
    """Raised when we cannot access to MCC service """
    pass

def get_exception_message(merchant_id: int, creator_email: Optional[str] = None) -> str:
    if creator_email:
        return F"Micheline a perdu accès please fix it {merchant_id}. You, as as well as our email, need to have direct access to the account to link it" ## TODO mct: Je vais le changer dans la pr sur les checks access
    else:
        return F"We cannot access your Merchant Center account with the id: {merchant_id} from the Arcane account. Are you sure you granted access and gave the correct ID?"
