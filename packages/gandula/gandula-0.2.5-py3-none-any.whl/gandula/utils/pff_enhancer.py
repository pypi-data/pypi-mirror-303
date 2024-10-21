"""Enhances raw PFF event data with data from frames."""

from typing import TypeAlias

from ..providers.pff.schema.event import (
    PFF_BallCarryEvent,
    PFF_ChallengeEvent,
    PFF_ChallengeType,
    PFF_ClearanceEvent,
    PFF_CrossEvent,
    PFF_Event,
    PFF_EventType,
    PFF_Game,
    PFF_PassingEvent,
    PFF_PassOutcomeType,
    PFF_PossessionEvent,
    PFF_Roster,
    PFF_ShootingEvent,
)
from ..providers.pff.schema.tracking import (
    PFF_Frame,
    PFF_Frame_GameEventType,
)

PlayerIdShirt: TypeAlias = dict[str, tuple[int, bool]]


def get_enhanceable_event_ids(
    events: list[PFF_Event],
) -> tuple[list[int], list[int]]:
    """Returns the list of enhanceable events.

    Args:
        events: A list of PFF_Event objects.

    Returns:
        A tuple containing two lists:
            - A list of PFF_Event ids that are enhanceable.
            - A list of PFF_PossessionEvent ids that are enhanceable.
    """
    event_ids = [
        int(event.id)
        for event in events
        if event.gameEventType == PFF_EventType.BALL_OUT_OF_PLAY
    ]

    possession_event_ids = [
        int(pevt.id) for event in events for pevt in event.possessionEvents
    ]

    return event_ids, possession_event_ids


def enhance_match(match: PFF_Game, frames: list[PFF_Frame]) -> PFF_Game:
    """Enhances a PFF match events with frame data."""
    player_id_shirt = _map_player_id_shirt(match.rosters, match.homeTeam.id)
    match.gameEvents = enhance(match.gameEvents, frames, player_id_shirt)
    return match


def enhance(
    events: list[PFF_Event],
    frames: list[PFF_Frame],
    player_id_shirt: PlayerIdShirt,
) -> list[PFF_Event]:
    """Enhances PFF events with frame data."""
    events_copy = [e.model_copy(deep=True) for e in events]
    possession_events = _map_possession_events_by_id(events_copy)
    pevt_frames = _match_possession_events_and_frames(possession_events, frames)

    modified_events = _add_coordinates_to_events(pevt_frames, frames, player_id_shirt)
    updated_events = _update_events_with_modified_possessions(
        events_copy, modified_events
    )
    updated_events = _update_out_events(updated_events, frames)
    return sorted(updated_events, key=lambda e: float(e.startTime))


def _map_player_id_shirt(rosters: list[PFF_Roster], home_team_id: str) -> PlayerIdShirt:
    """Maps player id to shirt number and if the player belongs to the home team."""
    return {
        roster.player.id: (int(roster.shirtNumber), roster.team.id == home_team_id)
        for roster in rosters
    }


def _map_possession_events_by_id(
    events: list[PFF_Event],
) -> dict[str, PFF_PossessionEvent]:
    """Extracts possession events from events."""
    return {pevt.id: pevt for event in events for pevt in event.possessionEvents}


def _match_possession_events_and_frames(
    pevents: dict[str, PFF_PossessionEvent], frames: list[PFF_Frame]
) -> dict[str, tuple[PFF_PossessionEvent, PFF_Frame]]:
    """Matches possession events with frames."""
    pevt_frames = {}

    for frame in frames:
        poss_id = str(frame.possession_id)
        if poss_id and poss_id in pevents:
            pevt_frames[poss_id] = (pevents[poss_id], frame)

    return pevt_frames


def _add_coordinates_to_events(
    pevt_frames: dict[str, tuple[PFF_PossessionEvent, PFF_Frame]],
    frames: list[PFF_Frame],
    player_id_shirt: PlayerIdShirt,
) -> dict[str, PFF_PossessionEvent]:
    """Adds coordinates to events based on frame data."""
    modified_events = {}

    for pevt_id, (event, frame) in pevt_frames.items():
        event_with_coords = _add_coordinates((event, frame), player_id_shirt)
        if event_with_coords and isinstance(event_with_coords, PFF_PossessionEvent):
            event_with_coords = _look_ahead_and_add_coordinates(
                event_with_coords, frames, player_id_shirt
            )
        if event_with_coords:
            modified_events[pevt_id] = event_with_coords

    return modified_events


def _update_out_events(
    events: list[PFF_Event], frames: list[PFF_Frame]
) -> list[PFF_Event]:
    for event in events:
        if event.gameEventType == PFF_EventType.BALL_OUT_OF_PLAY:
            frame = next((f for f in frames if f.event_id == int(event.id)), None)
            if frame and frame.ball:
                event.endPointX = frame.ball[0].x
                event.endPointY = frame.ball[0].y
    return events


def _add_coordinates(
    event_frame: tuple[PFF_PossessionEvent, PFF_Frame],
    player_id_shirt: PlayerIdShirt,
) -> PFF_Event | PFF_PossessionEvent | None:
    """Adds coordinates to an event."""
    event, frame = event_frame

    if isinstance(event, PFF_PossessionEvent):
        if event.fouls:
            _add_coordinates_to_fouls(event.fouls, frame, player_id_shirt)
        if event.shootingEvent:
            _add_coordinates_to_shooting_event(
                event.shootingEvent, frame, player_id_shirt
            )
        if event.crossEvent:
            _add_coordinates_to_cross_event(event.crossEvent, frame, player_id_shirt)
        if event.passingEvent:
            _add_coordinates_to_passing_event(
                event.passingEvent, frame, player_id_shirt
            )
        if event.clearanceEvent:
            _add_coordinates_to_clearance_event(
                event.clearanceEvent, frame, player_id_shirt
            )
        if event.challengeEvent:
            _add_coordinates_to_challenge_event(
                event.challengeEvent, frame, player_id_shirt
            )
        if event.ballCarryEvent:
            _add_coordinates_to_ball_carry_event(
                event.ballCarryEvent, frame, player_id_shirt
            )
        return event

    return None


def _add_coordinates_to_fouls(
    fouls: list, frame: PFF_Frame, player_id_shirt: PlayerIdShirt
):
    """Adds coordinates to foul events."""
    for foul in fouls:
        coords = _get_player_coordinates(foul.culpritPlayer.id, frame, player_id_shirt)
        if coords:
            foul.foulPointX, foul.foulPointY = coords


def _add_coordinates_to_shooting_event(
    evt: PFF_ShootingEvent, frame: PFF_Frame, player_id_shirt: PlayerIdShirt
):
    """Adds coordinates to shooting events."""
    coords = _get_player_coordinates(evt.shooterPlayer.id, frame, player_id_shirt)
    if coords:
        evt.shotPointX, evt.shotPointY = coords

    if evt.blockerPlayer:
        coords = _get_player_coordinates(evt.blockerPlayer.id, frame, player_id_shirt)
        if coords:
            evt.defenderPointX, evt.defenderPointY = coords

    if evt.saverPlayer:
        coords = _get_player_coordinates(evt.saverPlayer.id, frame, player_id_shirt)
        if coords:
            evt.savePointX, evt.savePointY = coords

    if evt.clearerPlayer:
        coords = _get_player_coordinates(evt.clearerPlayer.id, frame, player_id_shirt)
        if coords:
            evt.defenderPointX, evt.defenderPointY = coords


def _add_coordinates_to_cross_event(
    evt: PFF_CrossEvent, frame: PFF_Frame, player_id_shirt: PlayerIdShirt
):
    """Adds coordinates to cross events."""
    coords = _get_player_coordinates(evt.crosserPlayer.id, frame, player_id_shirt)
    if coords:
        evt.crossPointX, evt.crossPointY = coords


def _add_coordinates_to_passing_event(
    evt: PFF_PassingEvent, frame: PFF_Frame, player_id_shirt: PlayerIdShirt
):
    """Adds coordinates to passing events."""
    coords = _get_player_coordinates(evt.passerPlayer.id, frame, player_id_shirt)
    if coords:
        evt.passPointX, evt.passPointY = coords


def _add_coordinates_to_clearance_event(
    evt: PFF_ClearanceEvent, frame: PFF_Frame, player_id_shirt: PlayerIdShirt
):
    """Adds coordinates to clearance events."""
    coords = _get_player_coordinates(evt.clearancePlayer.id, frame, player_id_shirt)
    if coords:
        evt.clearanceStartPointX, evt.clearanceStartPointY = coords


def _add_coordinates_to_challenge_event(
    evt: PFF_ChallengeEvent, frame: PFF_Frame, player_id_shirt: PlayerIdShirt
):
    """Adds coordinates to challenge events."""
    if evt.challengeWinnerPlayer:
        coords = _get_player_coordinates(
            evt.challengeWinnerPlayer.id, frame, player_id_shirt
        )
        if coords:
            evt.challengePointX, evt.challengePointY = coords

    if evt.challengeType == PFF_ChallengeType.DRIBBLE:
        player = evt.ballCarrierPlayer
        coords = _get_player_coordinates(player.id, frame, player_id_shirt)
        if coords:
            evt.dribbleStartPointX, evt.dribbleEndPointY = coords

        if evt.challengerPlayer:
            player = evt.challengerPlayer
            coords = _get_player_coordinates(player.id, frame, player_id_shirt)
            if coords:
                evt.tackleAttemptPointX, evt.tackleAttemptPointY = coords


def _add_coordinates_to_ball_carry_event(
    evt: PFF_BallCarryEvent, frame: PFF_Frame, player_id_shirt: PlayerIdShirt
):
    """Adds coordinates to ball carry events."""
    player = evt.ballCarrierPlayer
    coords = _get_player_coordinates(player.id, frame, player_id_shirt)
    if coords:
        evt.ballCarryStartPointX, evt.ballCarryStartPointY = coords


def _look_ahead_and_add_coordinates(
    possession_event: PFF_PossessionEvent,
    frames: list[PFF_Frame],
    player_id_shirt: PlayerIdShirt,
) -> PFF_PossessionEvent:
    """Looks ahead to add coordinates to events that require future frame data."""
    event_id = int(possession_event.gameEvent.id)
    p_id = int(possession_event.id)
    frames_sorted = sorted(frames, key=lambda f: f.frame_id)

    curr_frame = next((f for f in frames_sorted if f.possession_id == p_id), None)
    next_frame = next(
        (f for f in frames_sorted if f.event_id and f.event_id > event_id),
        None,
    )

    if possession_event.ballCarryEvent and curr_frame:
        _add_ball_carry_end_coordinates(
            possession_event.ballCarryEvent,
            frames_sorted,
            curr_frame,
            player_id_shirt,
        )

    if next_frame and next_frame.event:
        if next_frame.event.game_event_type == PFF_Frame_GameEventType.END_OF_HALF:
            return possession_event

    if next_frame:
        if possession_event.passingEvent:
            _add_passing_event_next_frame_coords(
                possession_event.passingEvent, next_frame, player_id_shirt
            )
        if possession_event.crossEvent:
            _add_cross_event_next_frame_coords(possession_event.crossEvent, next_frame)
        if possession_event.clearanceEvent:
            _add_clearance_event_next_frame_coords(
                possession_event.clearanceEvent, next_frame
            )

    return possession_event


def _get_frame_by_id(frames: list[PFF_Frame], frame_id: int) -> PFF_Frame | None:
    return next((f for f in frames if f.frame_id == frame_id), None)


def _add_ball_carry_end_coordinates(evt, frames, curr_frame, player_id_shirt):
    """Adds end coordinates to ball carry events."""
    start_frame = _get_frame_by_id(frames, curr_frame.event.start_frame)
    end_frame = _get_frame_by_id(frames, curr_frame.event.end_frame)

    if start_frame:
        player = evt.ballCarrierPlayer
        coords = _get_player_coordinates(player.id, start_frame, player_id_shirt)
        if coords:
            evt.ballCarryStartPointX, evt.ballCarryStartPointY = coords
    if end_frame:
        player = evt.ballCarrierPlayer
        coords = _get_player_coordinates(player.id, end_frame, player_id_shirt)
        if coords:
            evt.ballCarryEndPointX, evt.ballCarryEndPointY = coords


def _add_passing_event_next_frame_coords(evt, next_frame, player_id_shirt):
    """Adds coordinates to passing events from the next frame."""
    if evt.receiverPlayer:
        player = evt.receiverPlayer
        coords = _get_player_coordinates(player.id, next_frame, player_id_shirt)
        if coords:
            evt.receiverPointX, evt.receiverPointY = coords
    elif (
        evt.defenderPlayer
        and evt.passOutcomeType == PFF_PassOutcomeType.DEFENSIVE_INTERCEPTION
    ):
        player = evt.defenderPlayer
        coords = _get_player_coordinates(player.id, next_frame, player_id_shirt)
        if coords:
            evt.defenderPointX, evt.defenderPointY = coords
    elif evt.passOutcomeType == PFF_PassOutcomeType.OUT_OF_PLAY:
        if next_frame.ball:
            ball = next_frame.ball[0]
            evt.outOfPlayPointX, evt.outOfPlayPointY = ball.x, ball.y


def _add_cross_event_next_frame_coords(evt, next_frame):
    """Adds end coordinates to cross events from the next frame."""
    if next_frame.ball:
        ball = next_frame.ball[0]
        evt.crossEndPointX, evt.crossEndPointY = ball.x, ball.y


def _add_clearance_event_next_frame_coords(evt, next_frame):
    """Adds end coordinates to clearance events from the next frame."""
    if next_frame.ball:
        ball = next_frame.ball[0]
        evt.clearanceEndPointX, evt.clearanceEndPointY = ball.x, ball.y


def _get_player_coordinates(
    player_id: str, frame: PFF_Frame, player_id_shirt: PlayerIdShirt
) -> tuple[float, float] | None:
    """Gets the coordinates of a player in a frame."""
    player_info = player_id_shirt.get(player_id)

    if not player_info:
        return None

    shirt, is_home = player_info
    players = frame.home_players if is_home else frame.away_players
    player = next((p for p in players if p.shirt == shirt), None)

    if not player:
        return None

    return player.x, player.y


def _update_events_with_modified_possessions(
    events: list[PFF_Event],
    modified_events: dict[str, PFF_PossessionEvent],
) -> list[PFF_Event]:
    """Updates events with modified possession events."""
    for event in events:
        updated_p_events = []
        for p_event in event.possessionEvents:
            updated_p_events.append(modified_events.get(p_event.id, p_event))
        event.possessionEvents = updated_p_events

    return events


def filter_frames_with_actionable_events(raw_frame: dict) -> dict | None:
    """Filter frames that have actionable events."""
    if raw_frame.get('possession_event_id'):
        return raw_frame

    if raw_frame.get('game_event_id'):
        return raw_frame
        # if raw_frame.get('game_event_type') in [
        #     PFF_Frame_GameEventType.OUT_OF_PLAY.value,
        #     PFF_Frame_GameEventType.END_OF_HALF.value,
        # ]:
        #     return raw_frame
        # if raw_frame.get('frameNum') == raw_frame['game_event']['start_frame']:
        #     return raw_frame

    return None
