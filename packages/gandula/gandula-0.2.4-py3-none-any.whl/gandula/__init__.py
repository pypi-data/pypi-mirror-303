from . import logging as logging
from .api.auth import api_version as api_version
from .api.auth import validate_api_key as validate_api_key
from .api.competition import get_available_competitions as get_available_competitions
from .api.competition import get_competition as get_competition
from .api.competition import get_competitions as get_competitions
from .api.match import get_enhanced as get_enhanced
from .api.match import get_frames as get_frames
from .api.match import get_match as get_match
from .api.match import get_match_event as get_match_event
from .api.match import get_match_events as get_match_events
from .providers.pff.local import loader as loader
from .providers.pff.schema.event import PFF_Game as PFF_Game
from .providers.pff.schema.tracking import Frame_Event as Frame_Event
from .visualization.video import video as video
from .visualization.view import view as view

# def _repr_html_() -> str:
#     # TODO: Switch to jinja template
#     return ''

# If there is a connection, try to fetch api_version.
# Match it with provder.response_type.PFF_EVENT_VERSION
