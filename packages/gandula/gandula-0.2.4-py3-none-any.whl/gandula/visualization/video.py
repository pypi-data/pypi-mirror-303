"""Implements functionality for watching videos of possession events."""

from typing import cast
from uuid import uuid4

from bs4 import Tag
from IPython import get_ipython  #  type: ignore
from IPython.display import HTML, display

from ..config import VIDEO_BUFFER_SEC
from ..jinja import env
from ..providers.pff.schema.event import PFF_PossessionEvent


def _scrape_playlist_from_pff_video(url: str) -> str:
    """Scrape PFF video details from a given URL.

    Parameters:
    -----------
    url : HttpUrl
        The URL we want to scrape.

    Returns:
    --------
    str
        The url to the m3u8 playlist.
    """
    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f'Failed to load video. status_code={response.status_code}')

    soup = BeautifulSoup(response.text, 'html.parser')
    video = soup.find('video')

    if not video:
        raise ValueError('Failed to find the <video> element in the page.')

    video = cast(Tag, video)

    return video.get('data-playlist-url')  # type: ignore


def video(
    event: PFF_PossessionEvent,
    *,
    width: int | str = '80%',
    height: int | str = 'auto',
    start_buffer_sec=VIDEO_BUFFER_SEC,
    end_buffer_sec=VIDEO_BUFFER_SEC,
) -> None:
    """Display a video for a PFF_PossessionEvent on IPython environments.

    Parameters
    ----------
    event : PFF_PossessionEvent
        The PossessionEvent we want to see.
    width : int, optional
        The width of the video, by default 80%.
    height : int, optional
        The height of the video, by default 'auto'.
    """
    if not get_ipython():
        raise RuntimeError('This function is only available on IPython environments')

    if not event.videoUrl:
        raise ValueError('No video URL found for this event.')

    # this is temporary fix as PFF is serving the url without the film_room
    split_url = event.videoUrl.split('/')
    event_path = '/'.join(split_url[1:])
    film_room_url = f'https://epitome-staging.pff.com/en/film_room/{event_path}'

    playlist_url = _scrape_playlist_from_pff_video(film_room_url)
    blob_url = f'blob:https://epitome-staging.pff.com/{split_url[1]}'

    video_vars = {
        'width': width,
        'height': height,
        'event_id': f'{event.id}-{uuid4()}',
        'start_position': float(event.startTime) - start_buffer_sec,  # type: ignore
        'end_position': float(event.endTime) + end_buffer_sec,  # type: ignore
        'playlist_url': playlist_url,
        'video_url': blob_url,
    }

    video_template = env.get_template('video.jinja2')

    display(HTML(video_template.render(video_vars)))
