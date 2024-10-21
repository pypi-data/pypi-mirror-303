"""Provides a pitch for visualizing data on."""

from typing import cast

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from mplsoccer import Pitch

from ..config import PITCH_LENGTH, PITCH_WIDTH

default_pitch_options = {
    'line_alpha': 0.8,
    'goal_alpha': 0.8,
}


def get_pitch(
    ax: Axes | None = None,
    *,
    pitch_length=PITCH_LENGTH,
    pitch_width=PITCH_WIDTH,
    **pitch_options,
) -> tuple[Pitch, Figure, Axes]:
    """Gets a pitch to visualize data on.

    Params:
        ax: matplotlib.axes.Axes | None
            A matplotlib.axes.Axes to draw on. If an ax is specified the pitch is drawn
            on an existing axis. Otherwise, a new figure is created
        pitch_length: float
            Horizontal size of the pitch
        pitch_width: float
            Vertical size of the pitch

    Returns:
        pitch: mplsoccer.Pitch
        fig: matplotlib.Figure
        ax: matplotlib.axes.Axes
    """
    options = {**default_pitch_options, **pitch_options}
    pitch = Pitch(
        pitch_type='custom',
        pitch_length=pitch_length,
        pitch_width=pitch_width,
        **options,
    )

    if ax is None:
        fig, ax = pitch.draw(ax=None, figsize=(12, 8))  # type: ignore
        ax = cast(Axes, ax)
    else:
        pitch.draw(ax=ax)
        fig = ax.get_figure()

    fig = cast(Figure, fig)

    return pitch, fig, ax
