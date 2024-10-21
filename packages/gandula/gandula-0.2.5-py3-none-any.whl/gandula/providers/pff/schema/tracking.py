from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class JerseyConfidence(Enum):
    HIGH = 'HIGH'
    MEDIUM = 'MEDIUM'
    LOW = 'LOW'


class Visibility(Enum):
    VISIBLE = 'VISIBLE'
    ESTIMATED = 'ESTIMATED'


class Frame_Player(BaseModel):
    shirt: int = Field(alias='jerseyNum')
    shirt_confidence: JerseyConfidence = Field(alias='confidence')
    visibility: Visibility
    x: float
    y: float


class Ball(BaseModel):
    visibility: Visibility
    x: float | None
    y: float | None
    z: float | None


class PFF_Frame_GameEventType(Enum):
    FIRST_KICK_OFF = 'FIRSTKICKOFF'
    SECOND_KICK_OFF = 'SECONDKICKOFF'
    THIRD_KICK_OFF = 'THIRDKICKOFF'
    FOURTH_KICK_OFF = 'FOURTHKICKOFF'
    FIRST_HALF_KICKOFF = '1KO'
    SECOND_HALF_KICKOFF = '2KO'
    END_OF_HALF = 'END'
    PBC_IN_PLAY = 'G'
    PLAYER_ON = 'ON'
    PLAYER_OFF = 'OFF'
    ON_THE_BALL = 'OTB'
    OUT_OF_PLAY = 'OUT'
    SUB = 'SUB'
    VIDEO_MISSING = 'VID'
    CLOCK = 'CLK'  # TODO: Check if this is correct


class SetPieceType(Enum):
    CORNER = 'C'
    DROP_BALL = 'D'
    FREE_KICK = 'F'
    GOAL_KICK = 'G'
    KICK_OFF = 'K'
    PENALTY = 'P'
    THROW_IN = 'T'


class Frame_Event(BaseModel):
    game_id: int
    game_event_type: PFF_Frame_GameEventType
    competition_id: int | None = None
    season: str | int | None = None
    clock: str | None = Field(alias='formatted_game_clock')
    player_id: int | None
    team_id: int | None
    setpiece_type: SetPieceType | None = None
    touches: int | None = Field(
        None, description='Number of touches taken by player on-the-ball'
    )
    touches_in_box: int | None = Field(
        None, description='Number of touches taken by player on-the-ball in the box'
    )
    start_time_seconds: float = Field(alias='start_time')
    end_time_seconds: float | None = Field(alias='end_time', default=None)
    duration_seconds: float | None = Field(alias='duration', default=None)
    video_missing: bool | None = Field(default=False)
    inserted_at: datetime
    updated_at: datetime
    start_frame: int = Field(description='The frame at which this GameEventType starts')
    end_frame: int | None = Field(
        None, description='The frame at which this GameEventType starts'
    )


class Frame_PossessionEventType(Enum):
    BALL_CARRY = 'BC'
    CHALLENGE = 'CH'  # includes dribbles
    CLEARANCE = 'CL'
    CROSS = 'CR'
    PASS = 'PA'
    REBOUND = 'RE'
    SHOT = 'SH'


class Frame_Possession(BaseModel):
    duration_seconds: float | None = Field(alias='duration', default=None)
    end_time_seconds: float | None = Field(alias='end_time', default=None)
    game_clock: str | None = Field(alias='formatted_game_clock')
    game_event_id: int
    game_id: int
    inserted_at: datetime
    possession_event_type: Frame_PossessionEventType
    start_time_seconds: float = Field(alias='start_time')
    updated_at: datetime
    start_frame: int
    end_frame: int | None = None


class PFF_Frame(BaseModel):
    model_config = ConfigDict(populate_by_name=True, arbitrary_types_allowed=True)

    away_players: list[Frame_Player] | None = Field(
        default_factory=list, alias='awayPlayers'
    )
    away_players_with_kalman: list[Frame_Player] | None = Field(
        default_factory=list, alias='awayPlayersSmoothed'
    )
    ball: list[Ball] | None = Field(default_factory=list, alias='balls')
    ball_with_kalman: Ball | None = Field(alias='ballsSmoothed')
    elapsed_seconds: float = Field(alias='periodElapsedTime')
    event: Frame_Event | None = Field(None, alias='game_event')
    event_id: int | None = Field(None, alias='game_event_id')
    frame_id: int = Field(alias='frameNum')
    game_clock_seconds: float = Field(alias='periodGameClockTime')
    match_id: int | None = Field(None, alias='gameRefId')
    generated_time: datetime | None = Field(alias='generatedTime')
    home_ball: int | None = None
    home_players: list[Frame_Player] | None = Field(
        default_factory=list, alias='homePlayers'
    )
    home_players_with_kalman: list[Frame_Player] | None = Field(
        default_factory=list, alias='homePlayersSmoothed'
    )
    period: int = Field(alias='period')
    possession: Frame_Possession | None = Field(None, alias='possession_event')
    possession_id: int | None = Field(None, alias='possession_event_id')
    sequence: int | None = None
    version: str | None
    video_time_milli: float = Field(alias='videoTimeMs')

    def __repr__(self):
        return f'Frame {self.frame_id} - {self.game_clock_seconds}'
