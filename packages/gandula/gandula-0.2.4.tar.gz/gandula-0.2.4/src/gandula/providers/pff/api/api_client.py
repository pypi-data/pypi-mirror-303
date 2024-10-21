import os
from typing import Any

from gql import Client, gql
from gql.transport.httpx import HTTPXTransport

PFF_API_URL = 'https://faraday.pff.com/api'
GQL_CLIENT_TIMEOUT = 60


def get_pff_api_url() -> str:
    """Retrieves the PFF API URL from the environment or defaults to the constant.

    :return: The PFF API URL.
    """
    return os.environ.get('PFF_API_URL', PFF_API_URL)


def get_pff_api_key() -> str:
    """Retrieves the PFF API key from the environment.

    :return: The PFF API key.
    :raises ValueError: If the API key is not found.
    """
    pff_api_key = os.environ.get('PFF_API_KEY')

    if not pff_api_key:
        raise ValueError(
            'A PFF API key is required. Please set it in your environment as'
            ' `PFF_API_KEY`. For example, `export PFF_API_KEY=your_api_key`.'
        )

    return pff_api_key


def build_headers(
    pff_api_key: str, additional_headers: dict[str, str] | None = None
) -> dict[str, str]:
    """Builds the header with the pff key for the GraphQL client.

    :param pff_api_key: The PFF API key for authentication.
    :param additional_headers: Additional headers to include in the request.
    :return: A dictionary containing the headers.
    """
    headers = {'x-api-key': pff_api_key}
    if additional_headers:
        headers.update(additional_headers)
    return headers


def get_client(
    pff_api_url: str | None = None,
    pff_api_key: str | None = None,
    *,
    headers: dict[str, str] | None = None,
    timeout: int = GQL_CLIENT_TIMEOUT,
) -> Client:
    """Creates and returns a configured GraphQL client.

    :param pff_api_url: The API URL to connect to. Defaults to the environment variable
        PFF_API_URL.
    :param pff_api_key: The API key for authentication. Defaults to env variable
        PFF_API_KEY.
    :param headers: Additional headers to include in the request.
    :param timeout: Timeout for GraphQL queries in seconds. Defaults to 60 seconds.
    :return: An instance of gql.Client configured with the provided settings.
    :raises ValueError: If the API key is not provided or is not a string.
    """
    pff_api_url = pff_api_url or get_pff_api_url()
    pff_api_key = pff_api_key or get_pff_api_key()

    headers = build_headers(pff_api_key, headers)
    transport = HTTPXTransport(url=pff_api_url, headers=headers, timeout=timeout)

    return Client(
        transport=transport, fetch_schema_from_transport=False, execute_timeout=timeout
    )


def execute_query(
    query: str, variables: dict[str, Any] | None = None, *, client: Client | None = None
) -> dict:
    """Executes a GraphQL query using the provided client.

    :param query: The query to execute.
    :param variables: Variables to include in the query.
    :param client: The GraphQL client to use for the query.
    :return: The result of the query.
    """
    if not client:
        client = get_client()

    try:
        return client.execute(
            gql(query),
            variable_values=variables,
            serialize_variables=True,
            parse_result=True,
        )
    except Exception as exc:
        raise Exception(
            f'There was an error trying to execute the following query:\n'
            f'Query: {query}\n'
            f'Variables: {variables}'
        ) from exc
