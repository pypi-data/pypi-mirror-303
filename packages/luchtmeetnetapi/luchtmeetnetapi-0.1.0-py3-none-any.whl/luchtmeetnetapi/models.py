"""Models for LuchtmeetNetApi."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

from mashumaro.mixins.orjson import DataClassORJSONMixin

T = TypeVar("T")


@dataclass
class PagedResult(DataClassORJSONMixin, Generic[T]):
    """Paged result."""

    pagination: Pagination
    data: list[T]


@dataclass
class Component(DataClassORJSONMixin):
    """Component model."""

    data: ComponentData


@dataclass
class Station(DataClassORJSONMixin):
    """Station model."""

    data: StationData


@dataclass
class Concentrations(DataClassORJSONMixin):
    """Concentrations model."""

    data: list[ConcentrationsData]


@dataclass
class ComponentsData:
    """Components data model."""

    name: MultiLanguageString
    formula: str


@dataclass
class OrganisationsData:
    """Organisations data model."""

    name: MultiLanguageString
    id: int


@dataclass
class StationsData:
    """Stations data model."""

    number: str
    location: str


@dataclass
class StationData:
    """Station data model."""

    type: str
    components: list[str]
    geometry: Geometry
    municipality: str
    url: str
    province: str
    organisation: str
    location: str
    year_start: str
    description: MultiLanguageString


@dataclass
class StationMeasurementData:
    """Station measurement data model."""

    value: float
    formula: str
    timestamp_measured: str


@dataclass
class MeasurementData:
    """Measurement data model."""

    station_number: str
    value: float
    timestamp_measured: str
    formula: str


@dataclass
class LkiValuesData:
    """Lki values data model."""

    station_number: str
    value: float
    timestamp_measured: str
    formula: str


@dataclass
class ConcentrationsData:
    """Concentrations data model."""

    formula: str
    value: float
    timestamp_measured: str


@dataclass
class Geometry:
    """Geometry model."""

    type: str
    coordinates: list[float]


@dataclass
class ComponentData:
    """Component data model."""

    name: MultiLanguageString
    description: MultiLanguageString
    formula: str
    limits: list[ComponentLimit]


@dataclass
class MultiLanguageString:
    """Multi language string model."""

    EN: str  # pylint: disable=invalid-name
    NL: str  # pylint: disable=invalid-name


@dataclass
class ComponentLimit(DataClassORJSONMixin):
    """ComponentLimit model."""

    lowerband: int | None
    upperband: int | None
    color: str
    rating: int
    type: str


@dataclass
class Pagination(DataClassORJSONMixin):
    """Pagination model."""

    current_page: int
    next_page: int
    prev_page: int
    page_list: list[int]
    first_page: int
    last_page: int

    def get_next_page(self) -> int | None:
        """Get next page number."""
        if self.next_page <= self.current_page:
            return None
        return self.next_page


@dataclass
class Components(PagedResult[ComponentsData]):
    """Components model."""


@dataclass
class Organisations(PagedResult[OrganisationsData]):
    """Organisations model."""


@dataclass
class Stations(PagedResult[StationsData]):
    """Stations model."""


@dataclass
class StationMeasurements(PagedResult[StationMeasurementData]):
    """Station measurements model."""


@dataclass
class Measurements(PagedResult[MeasurementData]):
    """Measurements model."""


@dataclass
class LkiValues(PagedResult[LkiValuesData]):
    """Lki values model."""
