"""Functions to visualize gandula objects."""

from typing import overload

from ..providers.pff.schema.event import PFF_Event, PFF_PossessionEvent
from ..providers.pff.schema.tracking import PFF_Frame
from ..schemas.atomic_spadl.types import SpadlAction
from .frame import view_frame_sequence, view_pff_frame

pydantic_dump_options = {
    'exclude_none': True,
    'exclude_defaults': True,
    'exclude_unset': True,
}


@overload
def _view_pff_event(events: PFF_Event | PFF_PossessionEvent, **kwargs) -> dict: ...


@overload
def _view_pff_event(
    events: list[PFF_Event | PFF_PossessionEvent], **kwargs
) -> list[dict]: ...


def _view_pff_event(
    events: PFF_Event | PFF_PossessionEvent | list[PFF_Event | PFF_PossessionEvent],
    **kwargs,
) -> dict | list[dict]:
    options = {**pydantic_dump_options, **kwargs}

    if isinstance(events, list):
        return [evt.model_dump(**options) for evt in events]

    return events.model_dump(**options)


def _view_spadl_action(action: SpadlAction | list[SpadlAction], **kwargs) -> dict: ...


def view(objs, **kwargs):
    """Single entry point for visualizing gandula objects.

    Parameters
    ----------
    objs : PFF_Event | PFF_PossessionEvent | PFF_Frame | SpadlAction
        The object to be visualized.
    kwargs : dict
        Options to be passed to the view function.
    """
    obj = objs[0] if isinstance(objs, list) else objs

    if isinstance(obj, PFF_Event) or isinstance(obj, PFF_PossessionEvent):
        return _view_pff_event(objs, **kwargs)
    if isinstance(obj, PFF_Frame):
        if isinstance(objs, list):
            return view_frame_sequence(objs, **kwargs)
        return view_pff_frame(objs, **kwargs)
    if isinstance(obj, SpadlAction):
        return _view_spadl_action(objs, **kwargs)

    if hasattr(obj, 'model_dump'):
        options = {**pydantic_dump_options, **kwargs}
        if isinstance(objs, list):
            return [o.model_dump(**options) for o in objs]
        return obj.model_dump(**options)

    raise ValueError(f'Cannot view object of type {type(obj)}')
