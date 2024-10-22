"""Base endpoint for the Luchtmeetnet API."""

from __future__ import annotations

from .const import (
    COMPONENT_API,
    COMPONENTS_API,
    CONCENTRATIONS_API,
    LKI_API,
    MEASUREMENTS_API,
    ORGANISATIONS_API,
    STATION_API,
    STATION_MEASUREMENTS_API,
    STATIONS_API,
)
from .models import (
    Component,
    Components,
    Concentrations,
    LkiValues,
    Measurements,
    Organisations,
    Station,
    StationMeasurements,
    Stations,
)
from .request_client import HttpRequestClient


class LuchtmeetNetApi(HttpRequestClient):
    """Luchtmeetnet API."""

    async def get_component(self, component_name: str) -> Component:
        """Retrieve the specifics of a selected component."""
        path = COMPONENT_API.format(component_name)

        return Component.from_json(await self._make_request(path))

    async def get_components(
        self, page: int = 1, order_by: str | None = None
    ) -> Components:
        """Retrieve components."""
        path = COMPONENTS_API

        return Components.from_json(
            await self._make_request(path, {"page": str(page), "order_by": order_by})
        )

    async def get_organisations(self, page: int = 1) -> Organisations:
        """Retrieve organisations."""
        path = ORGANISATIONS_API

        return Organisations.from_json(
            await self._make_request(path, {"page": str(page)})
        )

    async def get_stations(
        self,
        page: int = 1,
        order_by: str | None = None,
        organisation_id: str | None = None,
    ) -> Stations:
        """Retrieve stations."""
        path = STATIONS_API

        return Stations.from_json(
            await self._make_request(
                path,
                {
                    "page": str(page),
                    "order_by": order_by,
                    "organisation_id": organisation_id,
                },
            )
        )

    async def get_station(self, station_number: str) -> Station:
        """Retrieve station information."""
        path = STATION_API.format(station_number)

        return Station.from_json(await self._make_request(path))

    async def get_station_measurements(  # pylint: disable=R0913, R0917
        self,
        station_number: str,
        page: int = 1,
        order: str | None = None,
        order_direction: str | None = None,
        formula: str | None = None,
    ) -> StationMeasurements:
        """Retrieve station information."""
        path = STATION_MEASUREMENTS_API.format(station_number)

        return StationMeasurements.from_json(
            await self._make_request(
                path,
                {
                    "page": str(page),
                    "order": order,
                    "order_direction": order_direction,
                    "formula": formula,
                },
            )
        )

    async def get_measurements(  # pylint: disable=R0913, R0917  # noqa: PLR0913
        self,
        start: str | None = None,
        end: str | None = None,
        page: int = 1,
        order_by: str | None = None,
        order_direction: str | None = None,
        formula: str | None = None,
        station_number: str | None = None,
    ) -> Measurements:
        """Retrieve measurements."""
        path = MEASUREMENTS_API

        return Measurements.from_json(
            await self._make_request(
                path,
                {
                    "start": start,
                    "end": end,
                    "station_number": station_number,
                    "page": str(page),
                    "order_by": order_by,
                    "order_direction": order_direction,
                    "formula": formula,
                },
            )
        )

    async def get_lki(  # pylint: disable=R0913, R0917  # noqa: PLR0913
        self,
        start: str | None = None,
        end: str | None = None,
        page: int = 1,
        order_by: str | None = None,
        order_direction: str | None = None,
        station_number: str | None = None,
    ) -> LkiValues:
        """Retrieve calculate LKI values."""
        path = LKI_API

        return LkiValues.from_json(
            await self._make_request(
                path,
                {
                    "start": start,
                    "end": end,
                    "station_number": station_number,
                    "page": str(page),
                    "order_by": order_by,
                    "order_direction": order_direction,
                },
            )
        )

    async def get_concentrations(  # pylint: disable=R0913, R0917  # noqa: PLR0913
        self,
        formula: str,
        latitude: float,
        longitude: float,
        start: str | None = None,
        end: str | None = None,
        station_number: str | None = None,
    ) -> Concentrations:
        """Retrieve calculate LKI values."""
        path = CONCENTRATIONS_API

        return Concentrations.from_json(
            await self._make_request(
                path,
                {
                    "start": start,
                    "end": end,
                    "station_number": station_number,
                    "formula": formula,
                    "latitude": str(latitude),
                    "longitude": str(longitude),
                },
            )
        )
