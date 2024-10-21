from matplotlib.axes import Axes
from mplsoccer.pitch import Pitch

from ..config import PITCH_LENGTH, PITCH_WIDTH
from ..providers.pff.schema.event import PFF_ShootingEvent
from .pitch import get_pitch

shot_plot_options = {
    'ms': 8,
    'alpha': 1,
    'mec': '#000000',
    'mew': 1,
    'linewidth': 2,
    'fillstyle': None,
    'marker': 'o',
}

shot_arrows_options = {
    'width': 0.5,
    'headwidth': 10,
    'headlength': 10,
    'color': 'black',
}


def shot(
    shot_event: PFF_ShootingEvent, *, ax: Axes | None = None, pitch: Pitch | None = None
) -> Axes:
    _pitch, _, _ax = get_pitch()
    if not pitch:
        pitch = _pitch
    if not ax:
        ax = _ax
    pitch.draw(ax=ax)

    if shot_event.shotPointX and shot_event.shotPointY:
        x = shot_event.shotPointX + PITCH_LENGTH / 2
        y = shot_event.shotPointY + PITCH_WIDTH / 2
        pitch.arrows(x, y, PITCH_LENGTH, PITCH_WIDTH / 2, **shot_arrows_options, ax=ax)
        ax.plot(x, y, mfc=None, **shot_plot_options)
    return ax
