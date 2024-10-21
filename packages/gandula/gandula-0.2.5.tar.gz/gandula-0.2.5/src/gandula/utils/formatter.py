from typing import Callable, Literal, TypeVar

import pandas as pd

from ..providers.pff.api.response_types import PFFResponse

# TODO: Add Gandula
# TODO: Fix DataType typing
ResponseT = TypeVar('ResponseT', bound=PFFResponse)

Format = Literal['dict', 'json', 'dataframe', 'gandula', 'typed']
DataType = ResponseT | list[ResponseT]
ResponseType = dict | str | pd.DataFrame | DataType


default_view_options = {
    'exclude_none': True,
    'exclude_defaults': True,
    'exclude_unset': True,
}


def process_dict(response: DataType, **options) -> dict | list:
    if isinstance(response, list):
        return [item.model_dump(**options) for item in response]
    return response.model_dump(**options)


def process_json(response: DataType, **options) -> str:
    if isinstance(response, list):
        return str([item.model_dump(**options) for item in response])
    return response.model_dump_json(**options)


def process_dataframe(response: DataType, **options) -> pd.DataFrame:
    if isinstance(response, list):
        return pd.DataFrame([item.model_dump(**options) for item in response])
    return pd.DataFrame(response.model_dump(**options))


def process_typed(response: DataType) -> DataType:
    return response


def process_gandula(response: DataType, **options) -> DataType:
    return response


# TODO: Fix Callable args
formatter_dispatcher: dict[Format, Callable[[DataType], ResponseType]] = {
    'dict': process_dict,
    'json': process_json,
    'dataframe': process_dataframe,
    'gandula': process_gandula,
    'typed': process_typed,
}


def format_response(response: DataType, fmt: Format = 'dict') -> ResponseType:
    """Function to process responses based on the given formatter.

    :param rseponse: The response to be processed.
    :param fmt: The type of formatter to use.
    :return: The result of the processing function corresponding to the formatter.
    """
    if fmt in formatter_dispatcher:
        return formatter_dispatcher[fmt](response, **default_view_options)
    else:
        raise ValueError(f'Unsupported formatter: {fmt}')
