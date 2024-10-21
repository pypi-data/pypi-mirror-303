"""Schema for Atomic SPADL."""

from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from .types import SpadlAction, SpadlBodyPart


class AtomicSpadl(BaseModel):
    match_id: int
    event_id: int
    period_id: int
    player_id: int
    team_id: int
    time_seconds: Annotated[float, Field(strict=True, gt=0)]
    x: Annotated[float, Field(strict=True, ge=0, le=105)]
    y: Annotated[float, Field(strict=True, ge=0, le=68)]
    dx: Annotated[float, Field(strict=True, ge=-105, le=105)]
    dy: Annotated[float, Field(strict=True, ge=-68, le=68)]
    action_type: SpadlAction
    bodypart: SpadlBodyPart

    model_config = ConfigDict(use_enum_values=True)

    def __eq__(self, other):
        return self.match_id == other.match_id and self.event_id == other.event_id


#     def __repr__(self):
#         return (
#             f'{self.action_type.name}'
#             f' by player {self.player_id} ({self.team_id})'
#             f' at {self.time_seconds}s'
#         )
