from pydantic import BaseModel, ValidationError, field_validator, model_validator

PFF_API_VERSION = '0.6.100'
PFF_FRAME_VERSION = '4.0.0'  # TODO: Get version num


class PFFResponse(BaseModel):
    _version: str


class PFFEventResponse(PFFResponse):
    _event_version: str = PFF_API_VERSION

    @model_validator(mode='before')
    def set_data_version(cls, values: dict):
        event_version = values.get('_event_version')
        if not event_version or not isinstance(event_version, str):
            raise ValidationError('`event version` tampered with')
        # TODO: Add format verification
        values['_version'] = event_version
        return values


class PFFFrameResponse(PFFResponse):
    _frame_version: str = PFF_FRAME_VERSION

    @model_validator(mode='before')
    def set_data_version(cls, values: dict):
        frame_version = values.get('_frame_version')
        if not frame_version or not isinstance(frame_version, str):
            raise ValidationError('`frame version` tampered with')
        # TODO: ADd format verification
        values['_version'] = frame_version
        return values


class AvailableCompetitions(PFFEventResponse):
    id: int
    name: str
    seasons: list[str]

    @field_validator('seasons', mode='before')
    def populate_seasons(cls, v):
        return [d['season'] for d in v]


class Competition(PFFEventResponse): ...


class Competitions(PFFEventResponse): ...
