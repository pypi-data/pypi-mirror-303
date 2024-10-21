from functools import lru_cache

from .query_utils import build_full_query

game = """
query game($id: ID!) {
    game(id: $id) {
        ...GameFragment
        gameEvents {
            ...GameEventFragment
        }
    }
}
"""

game_events = """
query gameEvents(
    $gameId: ID!,
    $otherPlayerId: ID,
    $playerId: ID,
    $playerOffId: ID,
    $playerOnId: ID,
    $pressurePlayerId: ID,
    $sortField: GameEventSortFields,
    $sortOrder: SortOrder
) {
    gameEvents(
        gameId: $gameId,
        otherPlayerId: $otherPlayerId,
        playerId: $playerId,
        playerOffId: $playerOffId,
        playerOnId: $playerOnId,
        pressurePlayerId: $pressurePlayerId,
        sortField: $sortField,
        sortOrder: $sortOrder
    ) {
        ...GameEventFragment
    }
}
"""

game_event = """
query gameEvent($id: ID!) {
    gameEvent(id: $id) {
       ...GameEventFragment 
    }
}
"""

pass_event = """
query passingEvent($id: ID!) {
    passingEvent(id: $id) {
        ...PassingEventFragment
    }
}
"""

available_competitions = """
query competitions(
    $sortField: CompetitionSortFields,
    $sortOrder: SortOrder
) {
    competitions(
        sortField: $sortField,
        sortOrder: $sortOrder
    ) {
        id
        name
        seasons: availableSeasons {
            ...CompetitionSeasonFragment
        }
    }
}
"""

competitions = """
query competitions(
  $sortField: CompetitionSortFields,
  $sortOrder: SortOrder
) {
  competitions(
    sortField: $sortField,
    sortOrder: $sortOrder
  ) {
    availableSeasons {
      ...CompetitionSeasonFragment
    }
    id
    insertedAt
    games {
      ...CompetitionGameFragment
    }
    lastSeason {
      ...CompetitionSeasonFragment
    }
    logoIcon
    name
    teams {
      ...TeamFragment
    }
    updatedAt
  }
}
"""

competition = """
query competition($id: ID!) {
  competition(id: $id) {
    availableSeasons {
      ...CompetitionSeasonFragment
    }
    id
    insertedAt
    games {
      ...CompetitionGameFragment
    }
    lastSeason {
      ...CompetitionSeasonFragment
    }
    logoIcon
    name
    teams {
      ...TeamFragment
    }
    updatedAt
  }
}
"""

players_by_competition = """
query competition ($id: ID!) {
  competition (id: $id) {
    games {
      rosters {
        player {
          ...PlayerFullFragment
        }
        shirtNumber
        game {
          id
        }
      }
    }
  } 
}
"""

player = """
query player($id: ID!) {
  player(id: $id) {
    ...PlayerFullFragment
    rosters {
      ...RosterShortFragment
    }
  }
}
"""

player_dribble_metrics = """
query playerDribbleMetricsReport(
  $competitionId: ID!,
  $playerId: Int!,
  $season: String!
) {
    playerDribbleMetricsReport(
        competitionId: $competitionId,
        playerId: $playerId,
        season: $season
    ) {
        ...DribbleMetricsFragment
    }
}
"""

account_active = """
query accountActive {
  accountActive
}
"""

version = """
query version {
  version
}
"""


@lru_cache()
def get_queries() -> dict[str, str]:
    queries = {
        'game': game,
        'game_events': game_events,
        'game_event': game_event,
        'pass_event': pass_event,
        'competitions': competitions,
        'competition': competition,
        'players_by_competition': players_by_competition,
        'player': player,
        'account_active': account_active,
        'version': version,
        'player_dribble_metrics': player_dribble_metrics,
        'available_competitions': available_competitions,
    }

    for query_name, query in queries.items():
        queries[query_name] = build_full_query(query)

    return queries


queries = get_queries()
