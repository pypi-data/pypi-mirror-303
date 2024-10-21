from .api_client import execute_query, get_client
from .queries import queries


def get_available_competitions(
    *, pff_api_url: str | None = None, pff_api_key: str | None = None
) -> dict:
    query = queries['available_competitions']
    client = get_client(pff_api_url, pff_api_key)
    return execute_query(query, client=client)


def get_competitions(
    *, pff_api_url: str | None = None, pff_api_key: str | None = None
) -> dict:
    query = queries['competitions']
    client = get_client(pff_api_url, pff_api_key)
    return execute_query(query, client=client)


def get_competition(
    competition_id: int,
    *,
    pff_api_url: str | None = None,
    pff_api_key: str | None = None,
) -> dict:
    query = queries['competition']
    variables = {'id': competition_id}
    client = get_client(pff_api_url, pff_api_key)
    return execute_query(query, variables, client=client)
