from gql.transport.exceptions import TransportServerError

from ..providers.pff.api import auth

# TODO: Rename module to something else more descriptive, meta PFF FC API


def validate_api_key(api_key: str | None = None, *, api_url: str | None = None) -> bool:
    """Validates the provided PFF API key.

    :param api_key: The API key to validate.
    :return: True if the API key is valid, False otherwise.
    """
    try:
        response = auth.account_active(pff_api_key=api_key, pff_api_url=api_url)
        return response['accountActive']
    except TransportServerError:
        return False


def api_version(*, api_url: str | None = None, api_key: str | None = None) -> dict:
    """Retrieves the version of the API.

    :param api_url: The API URL to connect to.
    :param api_key: The API
    :return: The version of the API.
    """
    return auth.version(pff_api_key=api_key, pff_api_url=api_url)
