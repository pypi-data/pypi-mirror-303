from ..providers.pff.api import competitions
from ..providers.pff.api.response_types import AvailableCompetitions
from ..utils.formatter import Format, ResponseType, format_response


def get_competitions(*, api_url: str | None = None, api_key: str | None = None) -> dict:
    """Retrieves all competitions, in full (long).

    :param api_url: The API URL to connect to.
    :param api_key: The API key for authentication.
    :return: A dictionary containing all competitions.
    """
    return competitions.get_competitions(pff_api_url=api_url, pff_api_key=api_key)


def get_available_competitions(
    *, api_url: str | None = None, api_key: str | None = None, fmt: Format = 'dict'
) -> ResponseType:
    """Retrieves only the available competitions for these credentials.

    :param api_url: The API URL to connect to.
    :param api_key: The API key for authentication.
    :return: A dictionary containing available competitions.
    """
    raw = competitions.get_available_competitions(
        pff_api_url=api_url, pff_api_key=api_key
    )
    response = [
        AvailableCompetitions.model_validate(competition)
        for competition in raw['competitions']
    ]
    return format_response(response, fmt)


def get_competition(
    competition_id: int, *, api_url: str | None = None, api_key: str | None = None
) -> dict:
    """Retrieves a specific competition by its ID.

    :param competition_id: The ID of the competition to retrieve.
    :param api_url: The API URL to connect to.
    :param api_key: The API key for authentication.
    :return: A dictionary containing the competition data.
    """
    return competitions.get_competition(
        competition_id, pff_api_url=api_url, pff_api_key=api_key
    )
