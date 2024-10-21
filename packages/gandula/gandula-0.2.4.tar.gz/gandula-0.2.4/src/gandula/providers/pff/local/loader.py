import bz2
import pickle
from pathlib import Path
from typing import Callable, Generator

import orjson
import pandas as pd
import structlog
from tqdm.auto import tqdm

logger = structlog.get_logger()


def check_path(path: str | Path):
    """Ensures that the path exists.

    :param data_dir: The path to the data directory.
    :raises FileNotFoundError: If the data directory does not exist.
    """
    if not Path(path).exists():
        raise FileNotFoundError(f'Path {path} does not exist')


def read_json(file_path: str | Path) -> list[dict]:
    """Loads a JSON file from `file_path`.

    :param file_path: The path to the JSON file.
    :return: The file contents
    """
    try:
        path = Path(file_path)
        with path.open('rb') as file:
            return orjson.loads(file.read())
    except Exception as exc:
        raise IOError(f'Failed to parse data from {file_path}') from exc


def read_jsonl(
    file_path: str | Path, *, record_filter: Callable | None
) -> Generator[list[dict], None, None]:
    """Loads a jsonl file and returns its contents as a list of dictionaries.

    :param file_path: The path to the .jsonl file.
    :param filter: A function to filter the records as they are read.
    :return: A list of dictionaries, where each dictionary corresponds to a JSON object
    from an entire line in the file.
    :raises FileNotFoundError: If the file does not exist.
    :raises IOError: If the file cannot be read or parsed.
    """
    try:
        path = Path(file_path)
        with path.open('rb') as file:
            for line in file:
                record = orjson.loads(line)
                if record_filter and record_filter(record) is False:
                    continue
                yield record
    except Exception as exc:
        raise IOError(f'Failed to parse data from {file_path}') from exc


def read_bz2(
    file_path: str | Path, encoding: str = 'utf-8', *, record_filter: Callable | None
) -> Generator[list[dict], None, None]:
    """Loads and decompresses a .bz2 file. The expected contents are jsonl files with
    tracking data from PFF.

    :param file_path: The path to the .bz2 file.
    :param encoding: The encoding to use when decoding the bytes. Defaults to 'utf-8'.
    :return: The decompressed content as bytes if decode is False, otherwise as string.
    :raises IOError: If the file cannot be read or decompressed.
    """
    try:
        path = Path(file_path)
        with bz2.open(path, 'rb') as file:
            file_contents = file.read()
        decoded_jsonl = file_contents.decode(encoding)
        lines = filter(None, decoded_jsonl.strip().split('\n'))
        for line in lines:
            record = orjson.loads(line)
            if record_filter and record_filter(record) is False:
                continue
            yield record
    except Exception as exc:
        raise IOError(f'Failed to read or decompress {file_path}') from exc


def read_csv(file_path: str | Path) -> pd.DataFrame:
    """Loads a CSV file from `file_path`.

    :param file_path: The path to the CSV file.
    :return: The file contents
    """
    try:
        path = Path(file_path)
        return pd.read_csv(path)
    except Exception as exc:
        raise IOError('Failed to parse data from {file_path}') from exc


def read_pickle(file_path: str | Path) -> pd.DataFrame:
    """Loads a pickle file from `file_path`.

    :param file_path: The path to the pickle file.
    :return: The file contents
    """
    try:
        path = Path(file_path)
        with path.open('rb') as file:
            return pickle.load(file)
    except Exception as exc:
        raise IOError('Failed to parse data from {file_path}') from exc


def build_path(data_dir: str, competition_name: str | None, season: str | None) -> Path:
    """Builds the path to the data file for a given match.
    :param data_dir: The base directory where the data is stored.
    :param competition_name: The name of the competition.
    :param season: The season of the competition.
    :param match_id: The ID of the match.
    :return: The path to the data file.
    """
    if (not competition_name and season) or (competition_name and not season):
        print(
            f'Both competition_name and season must be provided; fallback to {data_dir}'
        )

    path = Path(data_dir)
    if competition_name and season:
        path = path / competition_name / season

    check_path(path)
    return path


def get_filetype(directory: Path, match_id: int) -> str:
    """Searches for the file type for match `match_id`, either .jsonl or .bz2.

    :param directory: The directory to search in.
    :param match_id: The match ID to search for in the filename.
    :return: The filename if found, otherwise raises a FileNotFoundError.
    :raises FileNotFoundError: If no file with the specified match_id and suffix exists.
    """
    for file in Path(directory).iterdir():
        if (
            file.is_file()
            and (file.stem == str(match_id) or file.stem == str(match_id) + '.jsonl')
            and file.suffix in ['.jsonl', '.bz2']
        ):
            return file.name

    raise FileNotFoundError(
        f'No file found for match {match_id} with .jsonl or .bz2 in {directory}'
    )


def get_path(
    data_dir: str,
    match_id: int,
    competition_name: str | None = None,
    season: str | None = None,
) -> Path:
    """Combines building the directory path and checking if the file exists.

    :param data_dir: The base directory where the data is stored.
    :param match_id: The match ID to search for.
    :param competition_name: The name of the competition.
    :param season: The season of the competition.
    :return: A Path object representing the file.
    :raises FileNotFoundError: If the directory or file does not exist.
    """
    dirname = build_path(data_dir, competition_name, season)
    filename = get_filetype(dirname, match_id)
    return dirname / filename


def find_available_matches(
    data_dir: str, competition_name: str | None = None, season: str | None = None
) -> list[str]:
    """Returns a list of available matches for `competition_name` for a given season.

    :param data_dir: The base directory where the data is stored.
    :param competition_name: The name of the competition.
    :param season: The season of the competition.
    """
    path = build_path(data_dir, competition_name, season)

    return [
        file.name
        for file in path.iterdir()
        if file.is_file() and file.suffix in ['.jsonl', '.bz2']
    ]


def get_frames(
    data_dir: str,
    match_id: int,
    *,
    competition_name: str | None = None,
    season: str | None = None,
    record_filter: Callable | None = None,
) -> list[dict]:
    """Local client function to retrieve match data for a given match_id.

    :param data_dir: The base directory where the data is stored.
    :param competition_name: The name of the competition (optional).
    :param season: The season of the competition (optional).
    :param match_id: The ID of the match to retrieve data for.
    :return: A list of dictionaries containing the frames from PFF.
    """
    file_path = get_path(data_dir, match_id, competition_name, season)

    records = []

    if file_path.suffix == '.jsonl':
        file_data = read_jsonl(file_path, record_filter=record_filter)
    elif file_path.suffix == '.bz2':
        file_data = read_bz2(file_path, record_filter=record_filter)
    else:
        raise Exception(f'File type {file_path.suffix} not supported')

    for line in tqdm(
        file_data,
        unit=' frames',
        desc=f'Loading frames from match {match_id}',
        leave=False,
    ):
        records.append(line)

    return records
