"""Module for exporting frames as gif, png, etc."""

import io
from collections.abc import Callable
from pathlib import Path
from typing import Literal

import imageio
from matplotlib.pyplot import close, savefig
from pygifsicle import optimize

from ..providers.pff.schema.tracking import PFF_Frame
from ..visualization.frame import view_pff_frame


def _export_frame_sequence_as_gif(frames: list[PFF_Frame], path: str, fps=25) -> str:
    """
    Exports a sequence of frames as a GIF file.

    Args:
    ----------
    frames (list of dict): List of frames, each containing player and ball positions.
    gif_path : (str): Path to save the GIF.
    fps (int): Frames per second for the GIF.
    """
    images = []

    for frame in frames:
        ax = view_pff_frame(frame)

        fig = ax.get_figure()

        buf = io.BytesIO()
        savefig(buf, format='png')

        buf.seek(0)
        images.append(imageio.mimread(buf))

        close(fig)
        buf.close()

    if not path.endswith('.gif'):
        path = f'{path}.gif'

    with imageio.get_writer(path, fps=fps, mode='I') as writer:
        for img in images:
            writer.append_data(img)

    optimize(path)  # shrinks the gif size

    return Path(path).resolve().as_uri()


def _export_frame_sequence_as_png(
    frames: list[PFF_Frame], path: str, **kwargs
) -> list[str]:
    """Exports a sequence of frames as PNG files.

    Args:
    -----
    frames (list of dict): List of frames, each containing player and ball positions.
    path : (str): Path to save the PNG files.
    """
    paths = []

    if path.endswith('.png'):
        path = path[:-4]

    for index, frame in enumerate(frames):
        ax = view_pff_frame(frame)
        fig = ax.get_figure()
        filepath = f'{path}_{index}.png'
        savefig(filepath, bbox_inches='tight', dpi=100)
        paths.append(Path(filepath).resolve().as_uri())
        close(fig)

    return paths


ExportFormats = Literal['gif', 'png']


_exporters: dict[ExportFormats, Callable] = {
    'gif': _export_frame_sequence_as_gif,
    'png': _export_frame_sequence_as_png,
}


def export(
    frames: list[PFF_Frame] | PFF_Frame,
    *,
    fmt: ExportFormats,
    filename: str,
    fps=25,
    **kwargs,
) -> str | list[str]:
    """Exports a sequence of frames as a GIF or PNG files.

    Args:
    -----
    frames (list of dict): List of frames, each containing player and ball positions.
    fmt (str): Format to export the frames. Can be 'gif' or 'png'.
    filename (str): Path to save the file.
    fps (int): Frames per second for the GIF.
    """
    if isinstance(frames, PFF_Frame):
        frames = [frames]
    return _exporters[fmt](frames, filename, fps=fps, **kwargs)
