location = """
fragment LocationFragment on Location {
    eventModule
    id
    name
    x
    y
}
"""

player_id = """
fragment PlayerFragment on Player {
    id
}
"""

nation = """
fragment NationFragment on Nation {
    country
    federation {
        ...FederationFragment
    }
    fifaCode
    id
    iocCode
}
"""

federation = """
fragment FederationFragment on Federation {
    id
    abbreviation
    confederation {
        ...ConfederationFragment
    }
    country
    englishName
    name
}
"""

confederation = """
fragment ConfederationFragment on Confederation {
    id
    abbreviation
    name
}
"""

player_full = """
fragment PlayerFullFragment on Player {
    id
    firstName
    lastName
    nickname
    dob
    preferredFoot
    height
    weight
    gender
    positionGroupType
    nationality{
        ...NationFragment
    }
    secondNationality{
        ...NationFragment
    }
    countryOfBirth{
        ...NationFragment
    }
}
"""

roster_short = """
fragment RosterShortFragment on Roster {
    id
    game {
        id
    }
    positionGroupType
    shirtNumber
    started
    team {
        ...TeamFragment
    }
}
"""

roster = """
fragment RosterFragment on Roster {
    id
    game {
        id
    }
    player {
        ...PlayerFullFragment
    }
    positionGroupType
    shirtNumber
    started
    team {
        ...TeamFragment
    }
}
"""

team = """
fragment TeamFragment on Team {
    id
    name
    shortName
}
"""

kit = """
fragment KitFragment on Kit {
    id
    name
    primaryColor
    primaryTextColor
    secondaryColor
    secondaryTextColor
}
"""

team_full = """
fragment TeamFullFragment on Team {
    id
    name
    shortName
    availableSeasons
    country
    fifaId
    internationalName
}
"""

game = """
fragment GameFragment on Game {
    id
    awayTeam {
        ...TeamFragment
    }
    awayTeamKit {
        id
        name
        primaryColor
        primaryTextColor
        secondaryColor
        secondaryTextColor
    }
    homeTeam {
        ...TeamFragment
    }
    homeTeamKit {
        id
        name
        primaryColor
        primaryTextColor
        secondaryColor
        secondaryTextColor
    }
    competition {
        id
        name
    }
    complete
    date
    startPeriod1
    endPeriod1
    startPeriod2
    endPeriod2
    season
    stadium {
        id
        name
        pitches {
          length
          width
          grassType
        }
    }
    allRosters {
        ...RosterFragment
    }
    inallRosters {
        ...RosterFragment
    }
    rosters {
        ...RosterFragment
    }
    week
    homeTeamStartLeft
    homeTeamStartLeftExtraTime
}
"""

possession_event = """
fragment PossessionEventFragment on PossessionEvent {
    id
    ballCarryEvent {
      ...BallCarryEventFragment
    }
    challengeEvent {
      ...ChallengeEventFragment
    }
    clearanceEvent {
      ...ClearanceEventFragment
    }
    crossEvent {
      ...CrossEventFragment
    }
    defenders {
      ...DefenderFragment
    }
    duration
    endTime
    formattedGameClock
    fouls {
      ...FoulFragment
    }
    game {
      id
    }
    gameClock
    gameEvent {
      id
    }
    insertedAt
    lastInGameEvent
    passingEvent {
      ...PassingEventFragment
    }
    possessionEventType
    reboundEvent {
      ...ReboundEventFragment
    }
    shootingEvent {
      ...ShootingEventFragment
    }
    startTime
    updatedAt
    videoUrl
}
"""

ball_carry_event = """
fragment BallCarryEventFragment on BallCarryEvent {
    additionalChallenger1 {
      ...PlayerFragment
    }
    additionalChallenger2 {
      ...PlayerFragment
    }
    additionalChallenger3 {
      ...PlayerFragment
    }
    ballCarrierPlayer {
      ...PlayerFragment
    }
    ballCarryEndPointX
    ballCarryEndPointY
    ballCarryStartPointX
    ballCarryStartPointY
    ballCarryType
    carryType
    challengerPlayer {
      ...PlayerFragment
    }
    createsSpace
    defenderPlayer {
      ...PlayerFragment
    }
    defenderPointX
    defenderPointY
    dribbleEndPointX
    dribbleEndPointY
    dribbleOutcomeType
    dribbleStartPointX
    dribbleStartPointY
    dribbleType
    game {
      id
    }
    gameEvent {
        id
    }
    id
    linesBrokenType
    missedTouchPlayer {
      ...PlayerFragment
    }
    missedTouchPointX
    missedTouchPointY
    missedTouchType
    opportunityType
    possessionEvent {
        id
    }
    pressurePlayer {
      ...PlayerFragment
    }
    tackleAttemptPointX
    tackleAttemptPointY
    tackleAttemptType
    touchOutcomePlayer {
      ...PlayerFragment
    }
    touchOutcomeType
    touchPointX
    touchPointY
    touchType
    trickType
}
"""

challenge_event = """
fragment ChallengeEventFragment on ChallengeEvent {
additionalChallenger1 {
      ...PlayerFragment
    }
    additionalChallenger2 {
      ...PlayerFragment
    }
    additionalChallenger3 {
      ...PlayerFragment
    }
    ballCarrierPlayer {
      ...PlayerFragment
    }
    carryType
    challengeOutcomeType
    challengePointX
    challengePointY
    challengeType
    challengeWinnerPlayer {
      ...PlayerFragment
    }
    challengerAwayPlayer {
      ...PlayerFragment
    }
    challengerHomePlayer {
      ...PlayerFragment
    }
    challengerPlayer {
      ...PlayerFragment
    }
    createsSpace
    dribbleEndPointX
    dribbleEndPointY
    dribbleStartPointX
    dribbleStartPointY
    dribbleType
    game {
      id
    }
    gameEvent {
      id
    }
    id
    insertedAt
    keeperPlayer {
      ...PlayerFragment
    }
    linesBrokenType
    missedTouchPlayer {
      ...PlayerFragment
    }
    missedTouchPointX
    missedTouchPointY
    missedTouchType
    opportunityType
    possessionEvent {
      id
    }
    pressurePlayer {
      ...PlayerFragment
    }
    tackleAttemptPointX
    tackleAttemptPointY
    tackleAttemptType
    trickType
}
"""

clearance_event = """
fragment ClearanceEventFragment on ClearanceEvent {
    ballHeightType
    ballHighPointType
    blockerPlayer {
      ...PlayerFragment
    }
    clearanceBodyType
    clearanceEndPointX
    clearanceEndPointY
    clearanceOutcomeType
    clearancePlayer {
      ...PlayerFragment
    }
    clearancePointX
    clearancePointY
    clearanceStartPointX
    clearanceStartPointY
    createsSpace
    defenderPlayer {
      ...PlayerFragment
    }
    failedInterventionPlayer {
      ...PlayerFragment
    }
    failedInterventionPlayer1 {
      ...PlayerFragment
    }
    failedInterventionPlayer2 {
      ...PlayerFragment
    }
    failedInterventionPlayer3 {
      ...PlayerFragment
    }
    game {
      id
    }
    gameEvent {
      id
    }
    id
    keeperPlayer {
      ...PlayerFragment
    }
    missedTouchPlayer {
      ...PlayerFragment
    }
    missedTouchPointX
    missedTouchPointY
    missedTouchType
    opportunityType
    possessionEvent {
      id
    }
    pressurePlayer {
      ...PlayerFragment
    }
    pressureType
    shotInitialHeightType
    shotOutcomeType
}
"""

cross_event = """
fragment CrossEventFragment on CrossEvent {
    ballHeightType
    blockerPlayer {
      ...PlayerFragment
    }
    clearerPlayer {
      ...PlayerFragment
    }
    completeToPlayer {
      ...PlayerFragment
    }
    createsSpace
    crossEndPointX
    crossEndPointY
    crossHighPointType
    crossOutcomeType
    crossPointX
    crossPointY
    crossStartPointX
    crossStartPointY
    crossType
    crossZoneType
    crosserBodyType
    crosserPlayer {
      ...PlayerFragment
    }
    defenderBallHeightType
    defenderBodyType
    defenderPlayer {
      ...PlayerFragment
    }
    deflectionPointX
    deflectionPointY
    deflectorBodyType
    deflectorPlayer {
      ...PlayerFragment
    }
    failedInterventionPlayer {
      ...PlayerFragment
    }
    failedInterventionPlayer1 {
      ...PlayerFragment
    }
    failedInterventionPlayer2 {
      ...PlayerFragment
    }
    failedInterventionPlayer3 {
      ...PlayerFragment
    }
    failedInterventionPointX
    failedInterventionPointY
    game {
      id
    }
    gameEvent {
      id
    }
    goalkeeperPointX
    goalkeeperPointY
    id
    incompletionReasonType
    intendedTargetPlayer {
      ...PlayerFragment
    }
    intendedTargetPointX
    intendedTargetPointY
    keeperPlayer {
      ...PlayerFragment
    }
    linesBrokenType
    missedTouchPlayer {
      ...PlayerFragment
    }
    missedTouchPointX
    missedTouchPointY
    missedTouchType
    noLook
    opportunityType
    possessionEvent {
      id
    }
    pressurePlayer {
      ...PlayerFragment
    }
    pressureType
    receiverBallHeightType
    receiverBodyType
    receiverPointX
    receiverPointY
    secondIncompletionReasonType
    shotInitialHeightType
    shotOutcomeType
    targetZonePointX
    targetZonePointY
}
"""

defender = """
fragment DefenderFragment on Defender {
    defenderPlayer {
      ...PlayerFragment
    }
    defenderPointX
    defenderPointY
    game {
      id
    }
    gameEvent {
      id
    }
    id
    possessionEvent {
      id
    }
}
"""

foul = """
fragment FoulFragment on Foul {
    badCall
    correctDecision
    culpritPlayer {
      ...PlayerFragment
    }
    foulOutcomeType
    foulPointX
    foulPointY
    foulType
    game {
      id
    }
    gameEvent {
      id
    }
    id
    possessionEvent {
      id
    }
    potentialOffenseType
    sequence
    tacticalFoul
    var
    varCulpritPlayer {
      ...PlayerFragment
    }
    varOutcomeType
    varPotentialOffenseType
    varReasonType
    victimPlayer {
      ...PlayerFragment
    }
}
"""

passing_event = """
fragment PassingEventFragment on PassingEvent {
    ballHeightType
    blockerPlayer {
      ...PlayerFragment
    }
    clearerPlayer {
      ...PlayerFragment
    }
    createsSpace
    defenderBodyType
    defenderHeightType
    defenderPlayer {
      ...PlayerFragment
    }
    defenderPointX
    defenderPointY
    deflectionPointX
    deflectionPointY
    deflectorBodyType
    deflectorPlayer {
      ...PlayerFragment
    }
    failedInterventionPlayer {
      ...PlayerFragment
    }
    failedInterventionPlayer1 {
      ...PlayerFragment
    }
    failedInterventionPlayer2 {
      ...PlayerFragment
    }
    failedInterventionPlayer3 {
      ...PlayerFragment
    }
    failedInterventionPointX
    failedInterventionPointY
    game {
      id
    }
    gameEvent {
      id
    }
    goalkeeperPointX
    goalkeeperPointY
    id
    incompletionReasonType
    keeperPlayer {
      ...PlayerFragment
    }
    linesBrokenType
    missedTouchPlayer {
      ...PlayerFragment
    }
    missedTouchPointX
    missedTouchPointY
    missedTouchType
    noLook
    onTarget
    opportunityType
    outOfPlayPointX
    outOfPlayPointY
    passAccuracyType
    passBodyType
    passHighPointType
    passOutcomeType
    passPointX
    passPointY
    passType
    passerPlayer {
      ...PlayerFragment
    }
    possessionEvent {
      id
    }
    pressurePlayer {
      ...PlayerFragment
    }
    pressureType
    receiverBodyType
    receiverFacingType
    receiverHeightType
    receiverPlayer {
      ...PlayerFragment
    }
    receiverPointX
    receiverPointY
    secondIncompletionReasonType
    shotInitialHeightType
    shotOutcomeType
    targetFacingType
    targetPlayer {
      ...PlayerFragment
    }
    targetPointX
    targetPointY
}
"""

rebound_event = """
fragment ReboundEventFragment on ReboundEvent {
    blockerPlayer {
      ...PlayerFragment
    }
    defenderPlayer {
      ...PlayerFragment
    }
    game {
      id
    }
    gameEvent {
      id
    }
    id
    missedTouchPlayer {
      ...PlayerFragment
    }
    missedTouchPointX
    missedTouchPointY
    missedTouchType
    originateType
    possessionEvent {
      id
    }
    reboundBodyType
    reboundEndPointX
    reboundEndPointY
    reboundHeightType
    reboundHighPointType
    reboundOutcomeType
    reboundPointX
    reboundPointY
    reboundStartPointX
    reboundStartPointY
    rebounderPlayer {
      ...PlayerFragment
    }
    shotInitialHeightType
    shotOutcomeType
}
"""

shooting_event = """
fragment ShootingEventFragment on ShootingEvent {
    badParry
    ballHeightType
    ballMoving
    blockerPlayer {
      ...PlayerFragment
    }
    bodyMovementType
    clearerPlayer {
      ...PlayerFragment
    }
    createsSpace
    defenderPointX
    defenderPointY
    deflectionPointX
    deflectionPointY
    deflectorBodyType
    deflectorPlayer {
      ...PlayerFragment
    }
    failedInterventionPlayer {
      ...PlayerFragment
    }
    failedInterventionPlayer1 {
      ...PlayerFragment
    }
    failedInterventionPlayer2 {
      ...PlayerFragment
    }
    failedInterventionPlayer3 {
      ...PlayerFragment
    }
    game {
      id
    }
    gameEvent {
      id
    }
    goalLineEndPointX
    goalLineEndPointY
    goalLineStartPointX
    goalLineStartPointY
    goalkeeperPointX
    goalkeeperPointY
    id
    keeperTouchPointX
    keeperTouchPointY
    keeperTouchType
    missedTouchPlayer {
      ...PlayerFragment
    }
    missedTouchPointX
    missedTouchPointY
    missedTouchType
    noLook
    possessionEvent {
      id
    }
    pressurePlayer {
      ...PlayerFragment
    }
    pressureType
    saveHeightType
    savePointX
    savePointY
    saveReboundType
    saveable
    saverPlayer {
      ...PlayerFragment
    }
    shooterPlayer {
      ...PlayerFragment
    }
    shotBodyType
    shotInitialHeightType
    shotNatureType
    shotOutcomeType
    shotPointX
    shotPointY
    shotTargetPointX
    shotTargetPointY
    shotType
}
"""

game_events = """
fragment GameEventFragment on GameEvent {
    id
    bodyType
    defenderLocations {
      ...LocationFragment
    }
    duration
    endTime
    endType
    startPointX
    startPointY
    endPointX
    endPointY
    formattedGameClock
    gameClock
    gameEventType
    heightType
    initialTouchType
    offenderLocations {
      ...LocationFragment
    }
    otherPlayer {
      ...PlayerFragment
    }
    outType
    player {
      ...PlayerFragment
    }
    playerOff {
      ...PlayerFragment
    }
    playerOffType
    playerOn {
      ...PlayerFragment
    }
    possessionEvents {
      ...PossessionEventFragment
    }
    pressurePlayer {
      ...PlayerFragment
    }
    pressureType
    period
    setpieceType
    startTime
    subType
    team {
      ...TeamFragment
    }
    scoreValue
    touches
    touchesInBox
    videoUrl
}
"""

competition_season = """
fragment CompetitionSeasonFragment on CompetitionSeason {
  end
  season
  start
}
"""

competition_game = """
fragment CompetitionGameFragment on Game {
    id
    awayTeam {
        ...TeamFragment
    }
    homeTeam {
        ...TeamFragment
    }
    date
    season
    stadium {
        id
        name
        pitches { 
            length
            width
            grassType
        }
        noiseLevel
        seatingType
        stadiumType
        yearBuilt
        elevation
        capacity
    }
    week
}
"""

route = """
fragment RouteFragment on Route {
    confidence
    gameClockTime
    homeTeam
    isBall
    jersey
    playerId
    point
    visibility
}
"""

dribble_metrics = """
fragment DribbleMetricsFragment on PlayerDribbleMetricsReport {
    drb
    drbP90
    drbcmp
    drbcmpP90
    drbcmpPct
    gameId
    min
    playerId
    pos
    teamId
    week
}
"""


fragments = {
    'LocationFragment': location,
    'PlayerFragment': player_id,
    'PlayerFullFragment': player_full,
    'RosterFragment': roster,
    'TeamFragment': team,
    'GameFragment': game,
    'PossessionEventFragment': possession_event,
    'BallCarryEventFragment': ball_carry_event,
    'ChallengeEventFragment': challenge_event,
    'ClearanceEventFragment': clearance_event,
    'CrossEventFragment': cross_event,
    'DefenderFragment': defender,
    'FoulFragment': foul,
    'PassingEventFragment': passing_event,
    'ReboundEventFragment': rebound_event,
    'ShootingEventFragment': shooting_event,
    'GameEventFragment': game_events,
    'CompetitionSeasonFragment': competition_season,
    'CompetitionGameFragment': competition_game,
    'NationFragment': nation,
    'FederationFragment': federation,
    'ConfederationFragment': confederation,
    'RosterShortFragment': roster_short,
    'RouteFragment': route,
    'TeamFullFragment': team_full,
    'DribbleMetricsFragment': dribble_metrics,
}
