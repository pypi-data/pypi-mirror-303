from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class BallCarryType(Enum):
    CARRY = 'C'
    DRIBBLE = 'D'
    TOUCH = 'T'


class BetterOptionType(Enum):
    BALL_CARRY = 'B'
    CROSS = 'C'
    HOLD = 'H'
    CLEARANCE = 'L'
    CONTINUE = 'O'
    PASS = 'P'
    SHOT = 'S'


class BodyMovementType(Enum):
    AWAY_FROM_GOAL = 'AG'
    LATERALLY = 'LA'
    STATIC = 'ST'
    TOWARDS_GOAL = 'TG'


class PFF_BodyType(Enum):
    BACK = 'BA'
    BOTTOM = 'BO'
    TWO_HAND_CATCH = 'CA'
    CHEST = 'CH'
    HEAD = 'HE'
    LEFT_FOOT = 'L'
    LEFT_ARM = 'LA'
    LEFT_BACK_HEEL = 'LB'
    LEFT_SHOULDER = 'LC'
    LEFT_HAND = 'LH'
    LEFT_KNEE = 'LK'
    LEFT_SHIN = 'LS'
    LEFT_THIGH = 'LT'
    TWO_HAND_PALM = 'PA'
    TWO_HAND_PUNCH = 'PU'
    RIGHT_FOOT = 'R'
    RIGHT_ARM = 'RA'
    RIGHT_BACK_HEEL = 'RB'
    RIGHT_SHOULDER = 'RC'
    RIGHT_HAND = 'RH'
    RIGHT_KNEE = 'RK'
    RIGHT_SHIN = 'RS'
    RIGHT_THIGH = 'RT'
    TWO_HANDS = 'TWOHANDS'
    VIDEO_MISSING = 'VM'


class CarryType(Enum):
    LINE_BREAK = 'B'
    CHANGE_OF_DIRECTION = 'C'
    DRIVE_WITH_INTENT = 'D'
    LONG_CARRY = 'L'


class PFF_ChallengeOutcomeType(Enum):
    DISTRIBUTION_DISRUPTED = 'B'
    FORCED_OUT_OF_PLAY = 'C'
    DISTRIBUTES_BALL = 'D'  # tem um passe/clearance/shot/cross na hora do challenge
    FOUL = 'F'
    SHIELDS_IN_PLAY = 'I'
    KEEPS_BALL_WITH_CONTACT = 'K'
    ROLLS = 'L'  # girar em volta do marcador (geralmente tem pressao)
    BEATS_MAN_LOSES_BALL = 'M'
    NO_WIN_KEEP_BALL = 'N'  # tentou driblar, nao conseguiu passar e manteve a posse
    OUT_OF_PLAY = 'O'
    PLAYER = 'P'  # a bola vai para um jogador que nao tava envolvido (ex: espirrou)
    RETAIN = 'R'
    SHIELDS_OUT_OF_PLAY = 'S'


class PFF_ChallengeType(Enum):
    AERIAL_DUEL = 'A'
    FROM_BEHIND = 'B'
    DRIBBLE = 'D'
    FIFTY = 'FIFTY'
    GK_SMOTHERS = 'G'
    SHIELDING = 'H'
    HAND_TACKLE = 'K'
    SLIDE_TACKLE = 'L'
    SHOULDER_TO_SHOULDER = 'S'
    STANDING_TACKLE = 'T'


class ClearanceOutcomeType(Enum):
    LUCKY_SHOT_AT_GOAL = 'A'
    BLOCK = 'B'
    LUCKY_SHOT_OWN_GOAL = 'D'
    OWN_POST = 'N'
    OUT_OF_PLAY = 'O'
    PLAYER = 'P'
    STOPPAGE = 'S'
    POST = 'W'


class CrossOutcomeType(Enum):
    BLOCKED = 'B'
    COMPLETE = 'C'
    DEFENSIVE_INTERCEPTION = 'D'
    LUCKY_SHOT_AT_GOAL = 'I'
    OUT_OF_PLAY = 'O'
    STOPPAGE = 'S'
    UNTOUCHED = 'U'


class CrossType(Enum):
    DRILLED = 'D'
    FLOATED = 'F'
    SWING_IN = 'I'
    SWING_OUT = 'O'
    PLACED = 'P'


class CrossZoneType(Enum):
    CENTRAL = 'C'
    FAR_POST = 'F'
    NEAR_POST = 'N'
    SIX_YARD_BOX = 'S'


class DribbleOutcomeType(Enum):
    KEEPS_BALL_WITH_CONTACT = 'B'
    FOUL = 'F'
    MISHIT = 'H'
    KEEPS_BALL = 'K'
    BEATS_MAN_LOSES_BALL = 'L'
    MISSED_FOUL = 'M'
    FORCED_OUT_OF_PLAY = 'O'
    SUCCESSFUL_TACKLE = 'S'


class DribbleType(Enum):
    BETWEEN_TWO_DEFENDERS = 'B'
    INSIDE = 'I'
    KNOCKS_IN_FRONT = 'K'
    OUTSIDE = 'O'
    TRICK = 'T'


class EndType(Enum):
    EXTRA_1 = 'F'
    FIRST = 'FIRST'
    GAME = 'G'
    EXTRA_2 = 'S'
    SECOND = 'SECOND'
    Z_TEST_9 = 'Z'


class FacingType(Enum):
    BACK_TO_GOAL = 'B'
    GOAL = 'G'
    LATERAL = 'L'


class PFF_FoulOutcomeType(Enum):
    NO_FOUL = 'F'
    NO_WARNING = 'N'
    RED_CARD = 'R'
    SECOND_YELLOW = 'S'
    WARNING = 'W'
    YELLOW_CARD = 'Y'


class PFF_FoulType(Enum):
    ADVANTAGE = 'A'
    INFRINGEMENT = 'I'
    MISSED_INFRINGEMENT = 'M'


class PFF_EventType(Enum):
    FIRST_HALF_KICKOFF = 'FIRSTKICKOFF'
    SECOND_HALF_KICKOFF = 'SECONDKICKOFF'
    EXTRA_1_KICKOFF = 'THIRDKICKOFF'
    EXTRA_2_KICKOFF = 'FOURTHKICKOFF'
    GAME_CLOCK_OBSERVATION = 'CLK'
    END_OF_HALF = 'END'
    GROUND = 'G'  # trave!!! travessao ou bandeira de escanteio. O evento eh vazio.
    PLAYER_OFF = 'OFF'
    PLAYER_ON = 'ON'
    POSSESSION = 'OTB'
    BALL_OUT_OF_PLAY = 'OUT'
    PAUSE_OF_GAME_TIME = 'PAU'
    SUB = 'SUB'
    VIDEO = 'VID'
    # Might not need below.
    FIRST_HALF_KICKOFF_OLD = '1KO'
    SECOND_HALF_KICKOFF_OLD = '2KO'
    EXTRA_1_KICKOFF_OLD = '3KO'
    EXTRA_2_KICKOFF_OLD = '4KO'


class HeightType(Enum):
    ABOVE_HEAD = 'A'
    GROUND = 'G'
    BETWEEN_WAIST_AND_HEAD = 'H'
    OFF_GROUND_BELOW_WAIST = 'L'
    VIDEO_MISSING = 'M'
    HALF_VOLLEY = 'V'  # Bola quica e ta subindo


class IncompletionReasonType(Enum):
    BEHIND = 'BH'
    BLOCKED = 'BL'
    CAUGHT = 'CA'
    DEFENSIVE_CONTACT = 'CO'
    DELIBERATE = 'DB'
    DEFENSIVE_CHALLENGE = 'DC'
    DEFLECTED = 'DF'
    DEFENDER_INTERCEPTION = 'DI'
    FOUL = 'FO'
    HIGH = 'HI'
    HIT_OFFICIAL = 'HO'
    IN_FRONT = 'IF'
    RECEIVER_LETS_BALL_RUN = 'LB'
    MISCOMMUNICATION = 'MC'
    MISS_HIT = 'MH'
    PASSER_SLIPPED = 'PS'
    RECEIVER_DIDNT_RETURN_TO_BALL = 'RB'
    RECEIVER_SLIPPED = 'RF'
    RECEIVER_MISSES_BALL = 'RM'
    RECEIVER_STOPPED = 'RS'
    REFEREE_IN_WAY = 'RW'
    SPECULATIVE = 'SP'
    UNDERHIT = 'UH'


class InitialTouchType(Enum):
    H2C_BAD = 'B'
    H2C_GOOD = 'G'
    MISCONTROL = 'M'
    STANDARD = 'S'


class LinesBrokenType(Enum):
    ATT = 'A'
    ATT_MID = 'AM'
    ATT_MID_DEF = 'AMD'
    DEF = 'D'
    MID = 'M'
    MID_DEF = 'MD'


class MissedTouchType(Enum):
    DUMMY = 'D'  # deixa a bola passar pra outro
    MISSED_TOUCH = 'M'
    SLIP = 'S'


class PFF_OpportunityType(Enum):
    CHANCE_CREATED = 'C'
    DANGEROUS_POSITION = 'D'
    HALF_CHANCE = 'H'
    SPACE_TO_CLEAR = 'L'
    NEGATIVE_CHANCE_CREATED = 'N'
    NEGATIVE_DANGEROUS_POSITION = 'P'
    SPACE_TO_CROSS = 'R'
    SPACE_TO_SHOOT = 'S'


class OriginateType(Enum):
    CORNER_FLAG = 'C'
    MISCELLANEOUS = 'M'
    PLAYER = 'P'
    POST = 'W'


class OutType(Enum):
    AWAY_SCORE = 'A'
    HOME_SCORE = 'H'
    TOUCH = 'T'
    WHISTLE = 'W'


class PassAccuracyType(Enum):
    CHECKS_MOVEMENT = 'C'
    HEAVY = 'H'
    LIGHT = 'L'
    PRECISE = 'P'
    REDIRECTS = 'R'
    STANDARD = 'S'


class PFF_PassOutcomeType(Enum):
    BLOCKED = 'B'
    COMPLETE = 'C'
    DEFENSIVE_INTERCEPTION = 'D'
    LUCKY_SHOT_OWN_GOAL = 'G'
    LUCKY_SHOT_GOAL = 'I'
    OUT_OF_PLAY = 'O'
    STOPPAGE = 'S'


class PFF_PassType(Enum):
    CUTBACK = 'B'
    CREATE_CONTEST = 'C'
    FLICK_ON = 'F'
    LONG_PASS = 'L'
    MISS_HIT = 'M'
    BALL_OVER_THE_TOP = 'O'
    STANDARD_PASS = 'S'
    THROUGH_BALL = 'T'


class PlayerOffType(Enum):
    INJURY = 'I'
    RED_CARD = 'R'
    YELLOW_CARD = 'Y'


class PositionGroupType(Enum):
    ATTACK_MID = 'AM'
    CENTER_FORWARD = 'CF'
    CENTER_MID = 'CM'
    DEFENDER = 'D'
    DEFENSIVE_MID = 'DM'
    FORWARD = 'F'
    GK = 'GK'
    LEFT_BACK = 'LB'
    LEFT_CENTER_BACK = 'LCB'
    LEFT_MID = 'LM'
    LEFT_WINGER = 'LW'
    LEFT_WING_BACK = 'LWB'
    MIDFIELDER = 'M'
    MID_CENTER_BACK = 'MCB'
    RIGHT_BACK = 'RB'
    RIGHT_CENTER_BACK = 'RCB'
    CENTER_BACK = 'CB'
    RIGHT_MID = 'RM'
    RIGHT_WINGER = 'RW'
    RIGHT_WING_BACK = 'RWB'


class PFF_PossessionEventType(Enum):
    BALL_CARRY = 'BC'
    CHALLENGE = 'CH'
    CLEARANCE = 'CL'
    CROSS = 'CR'
    PASS = 'PA'
    REBOUND = 'RE'
    SHOT = 'SH'


class PFF_PotentialOffenseType(Enum):
    DISSENT = 'D'
    OFF_THE_BALL = 'F'
    HAND_BALL = 'H'
    ON_THE_BALL = 'N'
    OFFSIDE = 'O'
    TECHNICAL = 'T'
    DIVA = 'V'


class PressureType(Enum):
    ATTEMPTED = 'A'
    PASSING_LANE = 'L'
    PRESSURED = 'P'


# Rebound: a bola bateu no jogador
class ReboundOutcomeType(Enum):
    LUCKY_SHOT_GOAL = 'A'
    LUCKY_SHOT_OWN_GOAL = 'D'
    PLAYER = 'P'
    RETAIN = 'R'
    OUT_OF_TOUCH = 'T'


class SaveReboundType(Enum):
    CROSSBAR = 'CB'
    LEFT_BEHIND_GOAL = 'GL'
    RIGHT_BEHIND_GOAL = 'GR'
    LEFT_BEHIND_GOAL_HIGH = 'HL'
    RIGHT_BEHIND_GOAL_HIGH = 'HR'
    LEFT_SIX_YARD_BOX = 'L6'
    LEFT_AREA = 'LA'
    LEFT_OUT_OF_BOX = 'LO'
    LEFT_POST = 'LP'
    MIDDLE_SIX_YARD_BOX = 'M6'
    MIDDLE_AREA = 'MA'
    MIDDLE_OUT_OF_BOX = 'MO'
    CROSSBAR_OVER = 'OC'
    RIGHT_SIX_YARD_BOX = 'R6'
    RIGHT_AREA = 'RA'
    RIGHT_OUT_OF_BOX = 'RO'
    RIGHT_POST = 'RP'


class PFF_SetpieceType(Enum):
    CORNER = 'C'
    DROP_BALL = 'D'
    FREE_KICK = 'F'
    GOAL_KICK = 'G'
    KICKOFF = 'K'
    PENALTY = 'P'
    THROW_IN = 'T'


class ShotHeightType(Enum):
    BOTTOM_THIRD = 'BOTTOMTHIRD'
    CROSSBAR = 'C'
    SHORT = 'F'
    GROUND = 'G'
    MIDDLE_THIRD = 'MIDDLETHIRD'
    CROSSBAR_NARROW_OVER = 'N'
    OVER = 'O'
    TOP_THIRD = 'TOPTHIRD'
    CROSSBAR_NARROW_UNDER = 'U'


class ShotNatureType(Enum):
    PLACEMENT = 'A'
    FLICK = 'F'
    LACES = 'L'
    POWER = 'P'
    SCUFF = 'S'
    TOE_PUNT = 'T'


class PFF_ShotOutcomeType(Enum):
    ON_TARGET_BLOCK = 'B'
    OFF_TARGET_BLOCK = 'C'
    SAVE_OFF_TARGET = 'F'
    GOAL = 'G'
    GOALLINE_CLEARANCE = 'L'
    OFF_TARGET = 'O'
    ON_TARGET = 'S'


class PFF_ShotType(Enum):
    BICYCLE = 'B'
    DIVING = 'D'
    SIDE_FOOT = 'F'
    SLIDING = 'I'
    LOB = 'L'
    OUTSIDE_FOOT = 'O'
    STANDARD = 'S'
    STUDS = 'T'
    VOLLEY = 'V'


class PFF_StadiumGrassType(Enum):
    ASTRO_TURF = 'A'
    FIELD_TURF = 'F'
    REAL = 'R'
    NATURAL = 'N'


class PFF_StadiumType(Enum):
    CONVERSION = 'C'
    DOMED = 'D'
    INDOOR = 'I'
    OUTDOOR = 'O'


class SubType(Enum):
    BLOOD = 'B'
    SIN_BIN_COVER = 'C'
    HEAD = 'H'
    RETURN_FROM_HIA = 'R'
    STANDARD = 'S'


class TackleAttemptType(Enum):
    DELIBERATE_FOUL = 'D'
    NO_TACKLE_FAKE_EVENT = 'F'
    GO_FOR_BALL = 'G'
    NO_TACKLE = 'T'


class TouchOutcomeType(Enum):
    CHALLENGE = 'C'
    GOAL = 'G'
    OUT_OF_PLAY = 'O'
    PLAYER = 'P'
    OWN_GOAL = 'W'


class TouchType(Enum):
    BALL_IN_HAND = 'B'
    FAILED_CROSS = 'C'
    HAND_BALL = 'D'
    FAILED_TRAP = 'F'
    FAILED_CATCH = 'G'
    HEAVY_TOUCH = 'H'
    FAILED_CLEARANCE = 'L'
    FAILED_PASS = 'P'
    FAILED_SHOT = 'S'
    TAKE_OVER = 'T'


class VarReasonType(Enum):
    MISSED = 'I'
    OVERTURN = 'O'


class VideoAngleType(Enum):
    BAD_ANGLE = 'B'
    MISSING = 'M'


class _ID(BaseModel):
    id: str | None = None


class PFF_BallCarryEvent(BaseModel):
    id: str | None = None
    additionalChallenger1: Player | None = None
    additionalChallenger2: Player | None = None
    additionalChallenger3: Player | None = None
    ballCarrierPlayer: Player | None = None
    ballCarryEndPointX: float | None = None
    ballCarryEndPointY: float | None = None
    ballCarryStartPointX: float | None = None
    ballCarryStartPointY: float | None = None
    ballCarryType: BallCarryType | None = None
    carryType: CarryType | None = None
    challengerPlayer: Player | None = None
    createsSpace: bool | None = None
    defenderPlayer: Player | None = None
    defenderPointX: float | None = None
    defenderPointY: float | None = None
    dribbleEndPointX: float | None = None
    dribbleEndPointY: float | None = None
    dribbleOutcomeType: DribbleOutcomeType | None = None
    dribbleStartPointX: float | None = None
    dribbleStartPointY: float | None = None
    dribbleType: DribbleType | None = None
    game: PFF_Game | None = None
    gameEvent: PFF_Event | None = None
    linesBrokenType: LinesBrokenType | None = None
    opportunityType: PFF_OpportunityType | None = None
    period: str | int | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    pressurePlayer: Player | None = None
    tackleAttemptPointX: float | None = None
    tackleAttemptPointY: float | None = None
    tackleAttemptType: TackleAttemptType | None = None
    touchOutcomePlayer: Player | None = None
    touchOutcomeType: TouchOutcomeType | None = None
    touchPointX: float | None = None
    touchPointY: float | None = None
    touchType: TouchType | None = None
    trickType: str | None = None


class CacheStats(BaseModel):
    hitRate: float | None = None
    name: str | None = None


class PFF_ChallengeEvent(BaseModel):
    id: str | None = None
    additionalChallenger1: Player | None = None
    additionalChallenger2: Player | None = None
    additionalChallenger3: Player | None = None
    ballCarrierPlayer: Player | None = None
    challengeOutcomeType: PFF_ChallengeOutcomeType | None = None
    challengePointX: float | None = None
    challengePointY: float | None = None
    challengeType: PFF_ChallengeType | None = None
    challengeWinnerPlayer: Player | None = None
    challengerAwayPlayer: Player | None = None
    challengerHomePlayer: Player | None = None
    challengerPlayer: Player | None = None
    createsSpace: bool | None = None
    dribbleEndPointX: float | None = None
    dribbleEndPointY: float | None = None
    dribbleStartPointX: float | None = None
    dribbleStartPointY: float | None = None
    dribbleType: DribbleType | None = None
    game: PFF_Game | None = None
    gameEvent: PFF_Event | None = None
    keeperPlayer: Player | None = None
    linesBrokenType: LinesBrokenType | None = None
    opportunityType: PFF_OpportunityType | None = None
    period: str | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    pressurePlayer: Player | None = None
    tackleAttemptPointX: float | None = None
    tackleAttemptPointY: float | None = None
    tackleAttemptType: TackleAttemptType | None = None
    trickType: str | None = None


class PFF_ClearanceEvent(BaseModel):
    ballHeightType: str | None = None
    ballHighPointType: str | None = None
    blockerPlayer: Player | None = None
    clearanceBodyType: PFF_BodyType
    clearanceEndPointX: float | None = None
    clearanceEndPointY: float | None = None
    clearanceOutcomeType: ClearanceOutcomeType
    clearancePlayer: Player
    clearancePointX: float | None = None
    clearancePointY: float | None = None
    clearanceStartPointX: float | None = None
    clearanceStartPointY: float | None = None
    createsSpace: bool | None = None
    defenderPlayer: Player | None = None
    failedInterventionPlayer: Player | None = None
    failedInterventionPlayer1: Player | None = None
    failedInterventionPlayer2: Player | None = None
    failedInterventionPlayer3: Player | None = None
    game: PFF_Game | None = None
    gameEvent: PFF_Event | None = None
    id: str | None = None
    keeperPlayer: Player | None = None
    opportunityType: PFF_OpportunityType | None = None
    period: str | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    pressurePlayer: Player | None = None
    pressureType: PressureType | None = None
    shotInitialHeightType: ShotHeightType | None = None
    shotOutcomeType: PFF_ShotOutcomeType | None = None


class PFF_Competition(BaseModel):
    availableSeasons: list[PFF_CompetitionSeason] | None = Field(default_factory=list)
    id: str
    games: list[PFF_Game] | None = Field(default_factory=list)
    name: str | None = None
    seasonGames: list[PFF_Game] | None = Field(default_factory=list)
    teams: list[PFF_Team] | None = Field(default_factory=list)


class PFF_CompetitionSeason(BaseModel):
    season: str | None = None
    start: str | None = None
    end: str | None = None


class Confederation(BaseModel):
    id: str | None = None
    abbreviation: str | None = None
    name: str | None = None


class PFF_CrossEvent(BaseModel):
    ballHeightType: HeightType | None = None
    blockerPlayer: Player | None = None
    clearerPlayer: Player | None = None
    completeToPlayer: Player | None = None
    createsSpace: bool | None = None
    crossEndPointX: float | None = None
    crossEndPointY: float | None = None
    crossHighPointType: str | None = None
    crossOutcomeType: CrossOutcomeType | None = None
    crossPointX: float | None = None
    crossPointY: float | None = None
    crossStartPointX: float | None = None
    crossStartPointY: float | None = None
    crossType: CrossType | None = None
    crossZoneType: CrossZoneType | None = None
    crosserBodyType: PFF_BodyType | None = None
    crosserPlayer: Player | None = None
    defenderBallHeightType: HeightType | None = None
    defenderBodyType: PFF_BodyType | None = None
    defenderPlayer: Player | None = None
    deflectionPointX: float | None = None
    deflectionPointY: float | None = None
    deflectorBodyType: PFF_BodyType | None = None
    deflectorPlayer: Player | None = None
    failedInterventionPlayer: Player | None = None
    failedInterventionPlayer1: Player | None = None
    failedInterventionPlayer2: Player | None = None
    failedInterventionPlayer3: Player | None = None
    failedInterventionPointX: float | None = None
    failedInterventionPointY: float | None = None
    game: PFF_Game | None = None
    gameEvent: PFF_Event | None = None
    goalkeeperPointX: float | None = None
    goalkeeperPointY: float | None = None
    id: str | None = None
    incompletionReasonType: IncompletionReasonType | None = None
    intendedTargetPlayer: Player | None = None
    intendedTargetPointX: float | None = None
    intendedTargetPointY: float | None = None
    keeperPlayer: Player | None = None
    linesBrokenType: LinesBrokenType | None = None
    opportunityType: PFF_OpportunityType | None = None
    period: str | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    pressurePlayer: Player | None = None
    pressureType: PressureType | None = None
    receiverBallHeightType: HeightType | None = None
    receiverBodyType: PFF_BodyType | None = None
    receiverPointX: float | None = None
    receiverPointY: float | None = None
    secondIncompletionReasonType: IncompletionReasonType | None = None
    shotInitialHeightType: ShotHeightType | None = None
    shotOutcomeType: PFF_ShotOutcomeType | None = None
    targetZonePointX: float | None = None
    targetZonePointY: float | None = None


class Defender(BaseModel):
    id: str | None = None
    defenderPlayer: Player | None = None
    defenderPointX: float | None = None
    defenderPointY: float | None = None
    game: PFF_Game | None = None
    gameEvent: PFF_Event | None = None
    possessionEvent: PFF_PossessionEvent | None = None


class Federation(BaseModel):
    id: str | None = None
    name: str | None = None
    englishName: str | None = None
    abbreviation: str | None = None
    confederation: Confederation | None = None
    country: str | None = None


class PFF_Foul(BaseModel):
    id: str
    badCall: bool | None = None
    correctDecision: bool | None = None
    culpritPlayer: Player | None = None
    foulOutcomeType: PFF_FoulOutcomeType | None = None
    foulPointX: float | None = None
    foulPointY: float | None = None
    foulType: PFF_FoulType | None = None
    game: PFF_Game | None = None
    gameEvent: PFF_Event | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    potentialOffenseType: PFF_PotentialOffenseType | None = None
    sequence: int | None = None
    tacticalFoul: bool | None = None
    var: bool | None = None
    varCulpritPlayer: Player | None = None
    varOutcomeType: PFF_FoulOutcomeType | None = (
        None  # VAR OutcomeType | PFF_FoulOutcomeType
    )
    varPotentialOffenseType: PFF_PotentialOffenseType | None = None
    varReasonType: VarReasonType | None = None
    victimPlayer: Player | None = None


class Location(BaseModel):
    id: str | None = None
    ballCarryEvent: PFF_BallCarryEvent | None = None
    challengeEvent: PFF_ChallengeEvent | None = None
    clearanceEvent: PFF_ClearanceEvent | None = None
    crossEvent: PFF_CrossEvent | None = None
    gameEvent: PFF_Event | None = None
    name: str | None = None
    passingEvent: PFF_PassingEvent | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    reboundEvent: PFF_ReboundEvent | None = None
    shootingEvent: PFF_ShootingEvent | None = None
    x: float | None = None
    y: float | None = None


class Nation(BaseModel):
    country: str | None = None
    federation: Federation | None = None
    fifaCode: str | None = None
    id: str | None = None
    iocCode: str | None = None


class PFF_PassingEvent(BaseModel):
    ballHeightType: HeightType | None = None
    blockerPlayer: Player | None = None
    clearerPlayer: Player | None = None
    defenderBodyType: PFF_BodyType | None = None
    defenderHeightType: HeightType | None = None
    defenderPlayer: Player | None = None
    defenderPointX: float | None = None
    defenderPointY: float | None = None
    deflectionPointX: float | None = None
    deflectionPointY: float | None = None
    deflectorBodyType: PFF_BodyType | None = None
    deflectorPlayer: Player | None = None
    failedInterventionPlayer: Player | None = None
    failedInterventionPlayer1: Player | None = None
    failedInterventionPlayer2: Player | None = None
    failedInterventionPlayer3: Player | None = None
    failedInterventionPointX: float | None = None
    failedInterventionPointY: float | None = None
    game: PFF_Game | None = None
    gameEvent: PFF_Event | None = None
    goalkeeperPointX: float | None = None
    goalkeeperPointY: float | None = None
    id: str | None = None
    incompletionReasonType: IncompletionReasonType | None = None
    keeperPlayer: Player | None = None
    linesBrokenType: LinesBrokenType | None = None
    missedTouchPlayer: Player | None = None
    missedTouchPointX: float | None = None
    missedTouchPointY: float | None = None
    missedTouchType: MissedTouchType | None = None
    noLook: bool | None = None
    onTarget: bool | None = None
    opportunityType: PFF_OpportunityType | None = None
    outOfPlayPointX: float | None = None
    outOfPlayPointY: float | None = None
    passAccuracyType: PassAccuracyType | None = None
    passBodyType: PFF_BodyType
    passHighPointType: HeightType | None = None
    passOutcomeType: PFF_PassOutcomeType
    passPointX: float | None = None
    passPointY: float | None = None
    passType: PFF_PassType | None = None
    passerPlayer: Player
    period: str | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    pressurePlayer: Player | None = None
    pressureType: PressureType | None = None
    receiverBodyType: PFF_BodyType | None = None
    receiverFacingType: FacingType | None = None
    receiverHeightType: HeightType | None = None
    receiverPlayer: Player | None = None
    receiverPointX: float | None = None
    receiverPointY: float | None = None
    secondIncompletionReasonType: IncompletionReasonType | None = None
    shotInitialHeightType: ShotHeightType | None = None
    shotOutcomeType: PFF_ShotOutcomeType | None = None
    targetFacingType: FacingType | None = None
    targetPlayer: Player | None = None
    targetPointX: float | None = None
    targetPointY: float | None = None


class Player(BaseModel):
    id: str
    dob: str | None = None
    firstName: str | None = None
    gender: str | None = None
    height: float | None = None  # in cm
    lastName: str | None = None
    nickname: str | None = None
    preferredFoot: str | None = None
    weight: float | None = None
    positionGroupType: PositionGroupType | None = None
    nationality: Nation | None = None
    secondNationality: Nation | None = None
    countryOfBirth: Nation | None = None
    # rosters: list[PFF_Roster] | None = Field(default_factory=list)


class PFF_PossessionEvent(BaseModel):
    id: str
    ballCarryEvent: PFF_BallCarryEvent | None = None
    challengeEvent: PFF_ChallengeEvent | None = None
    clearanceEvent: PFF_ClearanceEvent | None = None
    crossEvent: PFF_CrossEvent | None = None
    defenders: list[Defender] | None = Field(default_factory=list)
    duration: float | None = None
    endTime: float | None = None
    formattedGameClock: str | None = None
    fouls: list[PFF_Foul] | None = Field(default_factory=list)
    game: PFF_Game | None = None
    gameClock: float | None = None
    gameEvent: PFF_Event | None = None
    lastInGameEvent: int | None = None
    passingEvent: PFF_PassingEvent | None = None
    period: str | None = None
    possessionEventType: PFF_PossessionEventType | None = None
    reboundEvent: PFF_ReboundEvent | None = None
    shootingEvent: PFF_ShootingEvent | None = None
    startTime: float | None = None
    videoUrl: str | None = None  # Field(default=None, exclude=True)

    def __repr__(self) -> str:
        return f'{self.possessionEventType}={self.id}'


class PFF_ReboundEvent(BaseModel):
    id: str | None = None
    game: PFF_Game | None = None
    gameEvent: PFF_Event | None = None
    period: str | None = None
    originateType: OriginateType | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    reboundBodyType: PFF_BodyType | None = None
    reboundEndPointX: float | None = None
    reboundEndPointY: float | None = None
    reboundHeightType: HeightType | None = None
    reboundHighPointType: HeightType | None = None
    reboundOutcomeType: ReboundOutcomeType | None = None
    reboundPointX: float | None = None
    reboundPointY: float | None = None
    reboundStartPointX: float | None = None
    reboundStartPointY: float | None = None
    rebounderPlayer: Player | None = None
    shotInitialHeightType: ShotHeightType | None = None
    shotOutcomeType: PFF_ShotOutcomeType | None = None


class PFF_Roster(BaseModel):
    id: str | None = None
    game: dict | None = None
    player: Player
    positionGroupType: PositionGroupType
    shirtNumber: str | int
    started: bool | None = None
    team: PFF_Team


class PFF_ShootingEvent(BaseModel):
    advantageType: str | None = None
    badParry: bool | None = None
    ballHeightType: HeightType | None = None
    ballMoving: bool | None = None
    betterOption: str | None = None
    betterOptionPlayer: Player | None = None
    betterOptionTime: str | None = None
    betterOptionType: BetterOptionType | None = None
    blockerPlayer: Player | None = None
    bodyMovementType: BodyMovementType | None = None
    clearerPlayer: Player | None = None
    createsSpace: bool | None = None
    defenderPointX: float | None = None
    defenderPointY: float | None = None
    deflectionPointX: float | None = None
    deflectionPointY: float | None = None
    deflectorBodyType: PFF_BodyType | None = None
    deflectorPlayer: Player | None = None
    goalLineEndPointX: float | None = None
    goalLineEndPointY: float | None = None
    goalLineStartPointX: float | None = None
    goalLineStartPointY: float | None = None
    goalkeeperPointX: float | None = None
    goalkeeperPointY: float | None = None
    id: str | None = None
    keeperTouchPointX: float | None = None
    keeperTouchPointY: float | None = None
    keeperTouchType: PFF_BodyType | None = None
    failedInterventionPlayer: Player | None = None
    missedTouchPlayer: Player | None = None
    noLook: bool | None = None
    period: str | None = None
    possessionEvent: PFF_PossessionEvent | None = None
    pressurePlayer: Player | None = None
    pressureType: PressureType | None = None
    saveHeightType: ShotHeightType | None = None
    savePointX: float | None = None
    savePointY: float | None = None
    saveReboundType: SaveReboundType | None = None
    saverPlayer: Player | None = None
    shooterPlayer: Player
    shotBodyType: PFF_BodyType
    shotInitialHeightType: ShotHeightType | None = None
    shotNatureType: ShotNatureType | None = None
    shotOutcomeType: PFF_ShotOutcomeType
    shotPointX: float | None = None
    shotPointY: float | None = None
    shotTargetPointX: float | None = None
    shotTargetPointY: float | None = None
    shotType: PFF_ShotType


class PFF_Pitch(BaseModel):
    length: float
    width: float
    grassType: PFF_StadiumGrassType


class PFF_Stadium(BaseModel):
    id: str
    name: str
    pitches: list[PFF_Pitch] = Field(default_factory=list)


class PFF_Team(BaseModel):
    id: str
    name: str | None = None
    shortName: str | None = None


class PFF_Kit(BaseModel):
    id: str
    name: str
    primaryColor: str
    primaryTextColor: str
    secondaryColor: str
    secondaryTextColor: str


class PFF_Game(BaseModel):
    id: str
    allRosters: list[PFF_Roster] = Field(default_factory=list)
    awayTeam: PFF_Team | None = None
    homeTeam: PFF_Team | None = None
    awayTeamKit: PFF_Kit | None = None
    homeTeamKit: PFF_Kit | None = None
    competition: PFF_Competition | None = None
    complete: bool | None = None
    date: str | None = None
    endPeriod1: float | None = None
    endPeriod2: float | None = None
    gameEvents: list[PFF_Event] | None = Field(default_factory=list)
    rosters: list[PFF_Roster] | None = Field(default_factory=list)
    home_started_left: bool | None = Field(None, alias='homeTeamStartLeft')
    home_started_left_et: bool | None = Field(None, alias='homeTeamStartLeftExtraTime')
    season: str | int | None = None
    stadium: PFF_Stadium | None = None
    startPeriod1: float | None = None
    startPeriod2: float | None = None
    week: int | None = None

    def get_by_event_type(self, event_type: PFF_EventType) -> list[PFF_Event]:
        if not self.gameEvents:
            return []

        return [evt for evt in self.gameEvents if evt.gameEventType == event_type]

    def get_by_possession_event_type(
        self, possession_event_type: PFF_PossessionEventType
    ) -> list[PFF_Event]:
        if not self.gameEvents:
            return []

        return [
            evt
            for evt in self.gameEvents
            if evt.possessionEvents
            and any(
                (p_evt.possessionEventType == possession_event_type)
                for p_evt in evt.possessionEvents
            )
        ]


class PFF_Event(BaseModel):
    # model_config = ConfigDict(use_enum_values=False)
    id: str
    bodyType: PFF_BodyType | None = None
    defenderLocations: list[Location] | None = Field(default_factory=list)
    duration: float | None = None
    endPointX: float | None = None
    endPointY: float | None = None
    endTime: float | None = None
    endType: EndType | None = None
    formattedGameClock: str | None = None
    game: PFF_Game | None = None
    gameClock: float | None = None
    gameEventType: PFF_EventType | None = None
    heightType: HeightType | None = None
    initialTouchType: InitialTouchType | None = None
    offenderLocations: list[Location] | None = Field(default_factory=list)
    otherPlayer: Player | None = None
    outType: OutType | None = None
    period: str | int | None = None
    player: Player | None = None
    playerOff: Player | None = None
    playerOffType: PlayerOffType | None = None
    playerOn: Player | None = None
    possessionEvents: list[PFF_PossessionEvent] = Field(default_factory=list)
    pressurePlayer: Player | None = None
    pressureType: PressureType | None = None
    setpieceType: PFF_SetpieceType | None = None
    scoreValue: int | None = None
    startPointX: float | None = None
    startPointY: float | None = None
    startTime: float | None = None
    subType: SubType | None = None
    team: PFF_Team | None = None
    touches: int | None = None
    touchesInBox: int | None = None

    def get_by_possession_event_type(
        self, possession_event_type: PFF_PossessionEventType
    ) -> list[PFF_PossessionEvent]:
        if not self.possessionEvents:
            return []

        return [
            evt
            for evt in self.possessionEvents
            if evt.possessionEventType == possession_event_type
        ]

    def get_by_possession_event_id(
        self, possession_event_id: str
    ) -> list[PFF_PossessionEvent]:
        if not self.possessionEvents:
            return []

        return [evt for evt in self.possessionEvents if evt.id == possession_event_id]

    def get_possession_events(self) -> list[PFF_PossessionEvent]:
        if not self.possessionEvents:
            return []

        return self.possessionEvents

    def __repr__(self) -> str:
        return f'PFF_Event({self.id}) {self.possessionEvents}'


class PassingEvent(PFF_PassingEvent): ...


class PassOutcomeType(Enum):
    BLOCKED = 'B'
    COMPLETE = 'C'
    DEFENSIVE_INTERCEPTION = 'D'
    LUCKY_SHOT_OWN_GOAL = 'G'
    LUCKY_SHOT_GOAL = 'I'
    OUT_OF_PLAY = 'O'
    STOPPAGE = 'S'


class SetpieceType(Enum):
    CORNER = 'C'
    DROP_BALL = 'D'
    FREE_KICK = 'F'
    GOAL_KICK = 'G'
    KICKOFF = 'K'
    PENALTY = 'P'
    THROW_IN = 'T'


class PotentialOffenseType(Enum):
    DISSENT = 'D'
    OFF_THE_BALL = 'F'
    HAND_BALL = 'H'
    ON_THE_BALL = 'N'
    OFFSIDE = 'O'
    TECHNICAL = 'T'
    DIVA = 'V'


class PassType(Enum):
    CUTBACK = 'B'
    CREATE_CONTEST = 'C'
    FLICK_ON = 'F'
    LONG_PASS = 'L'
    MISS_HIT = 'M'
    BALL_OVER_THE_TOP = 'O'
    STANDARD_PASS = 'S'
    THROUGH_BALL = 'T'


class OpportunityType(Enum):
    CHANCE_CREATED = 'C'
    DANGEROUS_POSITION = 'D'
    HALF_CHANCE = 'H'
    SPACE_TO_CLEAR = 'L'
    NEGATIVE_CHANCE_CREATED = 'N'
    NEGATIVE_DANGEROUS_POSITION = 'P'
    SPACE_TO_CROSS = 'R'
    SPACE_TO_SHOOT = 'S'


class ShootingEvent(PFF_ShootingEvent): ...


class ShotOutcomeType(Enum):
    ON_TARGET_BLOCK = 'B'
    OFF_TARGET_BLOCK = 'C'
    SAVE_OFF_TARGET = 'F'
    GOAL = 'G'
    GOALLINE_CLEARANCE = 'L'
    OFF_TARGET = 'O'
    ON_TARGET = 'S'


class ShotType(Enum):
    BICYCLE = 'B'
    DIVING = 'D'
    SIDE_FOOT = 'F'
    SLIDING = 'I'
    LOB = 'L'
    OUTSIDE_FOOT = 'O'
    STANDARD = 'S'
    STUDS = 'T'
    VOLLEY = 'V'
