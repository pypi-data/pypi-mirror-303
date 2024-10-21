from .api_client import execute_query, get_client
from .queries import queries


def account_active(
    pff_api_url: str | None = None, pff_api_key: str | None = None
) -> dict:
    query = queries['account_active']
    client = get_client(pff_api_url, pff_api_key)
    return execute_query(query, client=client)


def version(pff_api_url: str | None = None, pff_api_key: str | None = None) -> dict:
    query = queries['version']
    client = get_client(pff_api_url, pff_api_key)
    return execute_query(query, client=client)
