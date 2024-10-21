import ast
from collections.abc import Callable
from pathlib import Path

import structlog
from tqdm.auto import tqdm

from ..providers.pff.api import match
from ..providers.pff.local import loader as local_loader
from ..providers.pff.schema.event import PFF_Event, PFF_Game, PFF_Roster
from ..providers.pff.schema.tracking import PFF_Frame
from ..utils.pff_enhancer import (
    enhance_match,
    filter_frames_with_actionable_events,
    get_enhanceable_event_ids,
)

logger = structlog.get_logger()


def get_match_events(
    match_id: int, *, api_url: str | None = None, api_key: str | None = None
) -> list[PFF_Event]:
    try:
        events = match.get_match_events(
            match_id, pff_api_url=api_url, pff_api_key=api_key
        )
        return [PFF_Event.model_validate(event) for event in events['gameEvents']]
    except Exception as exc:
        raise Exception(f'Error getting match events for match_id={match_id}') from exc


def get_match(
    match_id: int,
    *,
    api_url: str | None = None,
    api_key: str | None = None,
    events_path: str | None = None,
) -> PFF_Game:
    try:
        if events_path is None:
            logger.debug(f'Getting match {match_id} from API')
            pff_match = match.get_match(
                match_id, pff_api_url=api_url, pff_api_key=api_key
            )
            logger.debug(f'Validating match {match_id}')
            valid_match = PFF_Game.model_validate(pff_match['game'])
            return valid_match

        # TODO: Refactor this section
        logger.debug(f'Getting match {match_id} from local path {events_path}')
        pff_events = local_loader.read_json(Path(events_path) / 'events.json')
        pff_events = [
            PFF_Event.model_validate(event)
            for event in pff_events
            if event['gameId'] == int(match_id)
        ]

        pff_rosters = local_loader.read_csv(Path(events_path) / 'rosters.csv')
        pff_rosters.rename(columns={'game_id': 'gameId'}, inplace=True)
        pff_rosters = pff_rosters[pff_rosters['gameId'] == int(match_id)]
        pff_rosters['player'] = pff_rosters['player'].apply(ast.literal_eval)
        pff_rosters['team'] = pff_rosters['team'].apply(ast.literal_eval)
        pff_rosters = pff_rosters.to_dict(orient='records')
        pff_rosters = [PFF_Roster.model_validate(roster) for roster in pff_rosters]

        pff_metadata = local_loader.read_csv(Path(events_path) / 'metadata.csv')
        pff_metadata = pff_metadata[pff_metadata['id'] == int(match_id)]
        columns_to_convert = [
            'awayTeam',
            'awayTeamKit',
            'competition',
            'homeTeam',
            'homeTeamKit',
            'stadium',
            'videos',
        ]
        for col in columns_to_convert:
            pff_metadata[col] = pff_metadata[col].apply(ast.literal_eval)
        pff_metadata = pff_metadata.to_dict(orient='records')[0]

        pff_match = {'game': pff_metadata}
        pff_match['game']['gameEvents'] = pff_events
        pff_match['game']['allRosters'] = pff_rosters

        return PFF_Game.model_validate(pff_match['game'])
    except Exception as exc:
        raise Exception(f'Error getting match for match_id={match_id}') from exc


def get_match_event(
    event_id: int, *, api_url: str | None = None, api_key: str | None = None
) -> PFF_Event:
    try:
        event = match.get_match_event(
            event_id, pff_api_url=api_url, pff_api_key=api_key
        )
        return PFF_Event.model_validate(event)
    except Exception as exc:
        raise Exception(f'Error getting match event for event_id={event_id}') from exc


def get_frames(
    data_dir: str,
    match_id: int,
    *,
    competition_name: str | None = None,
    season: str | None = None,
    record_filter: Callable | None = None,
) -> list[PFF_Frame]:
    try:
        frames = local_loader.get_frames(
            data_dir,
            match_id,
            competition_name=competition_name,
            season=season,
            record_filter=record_filter,
        )

        frames = [
            PFF_Frame.model_validate(frame)
            for frame in tqdm(
                frames, desc='Validating frames', unit=' frames', leave=False
            )
        ]

        return frames
    except Exception as exc:
        logger.error(f'Error getting frames for match_id={match_id}', exc_info=exc)
        raise Exception(f'Error getting frames for match_id={match_id}') from exc


def get_enhanced(
    match_id: int,
    data_dir: str,
    *,
    competition_name: str | None = None,
    season: str | None = None,
    events_path: str | None = None,
    record_filter: Callable[[dict], dict | None]
    | None = filter_frames_with_actionable_events,
) -> tuple[PFF_Game, list[PFF_Frame]]:
    pff_match = get_match(match_id, events_path=events_path)
    event_ids, possession_event_ids = get_enhanceable_event_ids(pff_match.gameEvents)

    frames = get_frames(
        data_dir,
        match_id,
        competition_name=competition_name,
        season=season,
        record_filter=record_filter,
    )

    updated_match = enhance_match(pff_match, frames)

    return updated_match, frames
