from .api_client import execute_query, get_client
from .queries import queries


def get_match_events(
    match_id: int, *, pff_api_url: str | None = None, pff_api_key: str | None = None
) -> dict:
    query = queries['game_events']
    variables = {'gameId': match_id}
    client = get_client(pff_api_url, pff_api_key)
    return execute_query(query, variables, client=client)


def get_match_event(
    event_id: int, *, pff_api_url: str | None = None, pff_api_key: str | None = None
) -> dict:
    query = queries['game_event']
    variables = {'id': event_id}
    client = get_client(pff_api_url, pff_api_key)
    return execute_query(query, variables, client=client)


def get_match(
    match_id: int, *, pff_api_url: str | None = None, pff_api_key: str | None = None
) -> dict:
    query = queries['game']
    variables = {'id': match_id}
    client = get_client(pff_api_url, pff_api_key)
    return execute_query(query, variables, client=client)
