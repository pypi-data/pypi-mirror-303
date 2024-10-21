"""Client for Luchtmeetnet.nl."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Coroutine, TypeVar

from .api import LuchtmeetNetApi
from .cache import STATION_COORDINATES
from .util import get_approximate_distance

if TYPE_CHECKING:
    from .models import (
        ComponentsData,
        LkiValuesData,
        MeasurementData,
        OrganisationsData,
        PagedResult,
        StationMeasurementData,
        StationsData,
    )

T = TypeVar("T")


class LuchtmeetNetClient(LuchtmeetNetApi):
    """Client for LuchtmeetNetApi."""

    async def get_closest_station(
        self, latitude: float, longitude: float, use_cache: bool = True
    ) -> str | None:
        """Get closest station by coordinate."""
        stations = await self.get_all_stations()

        coord = (longitude, latitude)
        closest_station = None
        closest_distance = float("inf")
        for station in stations:
            station_coord = await self.get_station_coordinate(station.number, use_cache)
            station_distance = get_approximate_distance(coord, station_coord)
            if station_distance < closest_distance:
                closest_station = station.number
                closest_distance = station_distance
        return closest_station

    async def get_station_coordinate(
        self, station_number: str, use_cache: bool = True
    ) -> tuple[float, float]:
        """Get station coordinate by station number."""
        if use_cache and station_number in STATION_COORDINATES:
            return STATION_COORDINATES[station_number]

        station = await self.get_station(station_number)
        return (
            station.data.geometry.coordinates[0],
            station.data.geometry.coordinates[1],
        )

    async def get_all_components(self) -> list[ComponentsData]:
        """Get all components."""
        return await self._get_all(lambda page: self.get_components(page=page))

    async def get_all_organisations(self) -> list[OrganisationsData]:
        """Get all organisations."""
        return await self._get_all(lambda page: self.get_organisations(page=page))

    async def get_all_stations(
        self,
        organisation_id: str | None = None,
    ) -> list[StationsData]:
        """Get all stations."""
        return await self._get_all(
            lambda page: self.get_stations(page=page, organisation_id=organisation_id)
        )

    async def get_all_station_measurements(
        self,
        station_number: str,
        formula: str | None = None,
    ) -> list[StationMeasurementData]:
        """Get all station measurements."""
        return await self._get_all(
            lambda page: self.get_station_measurements(
                page=page, station_number=station_number, formula=formula
            )
        )

    async def get_all_measurements(
        self,
        start: str | None = None,
        end: str | None = None,
        station_number: str | None = None,
        formula: str | None = None,
    ) -> list[MeasurementData]:
        """Get all measurements."""
        return await self._get_all(
            lambda page: self.get_measurements(
                page=page,
                station_number=station_number,
                formula=formula,
                start=start,
                end=end,
            )
        )

    async def get_all_lki(
        self,
        start: str | None = None,
        end: str | None = None,
        station_number: str | None = None,
    ) -> list[LkiValuesData]:
        """Get all lki."""
        return await self._get_all(
            lambda page: self.get_lki(
                page=page,
                station_number=station_number,
                start=start,
                end=end,
            )
        )

    async def _get_all(
        self, get_func: Callable[[int], Coroutine[Any, Any, PagedResult[T]]]
    ) -> list[T]:
        """Get all data from all pages."""
        items = []
        page: int | None = 1
        while page is not None:
            result = await get_func(page)
            items.extend(result.data)
            page = result.pagination.get_next_page()
        return items
