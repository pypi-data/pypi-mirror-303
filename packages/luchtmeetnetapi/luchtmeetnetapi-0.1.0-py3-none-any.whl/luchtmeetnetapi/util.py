"""Utility functions for the Luchtmeetnet API package."""

from __future__ import annotations

from math import atan2, cos, radians, sin, sqrt

EARTH_RADIUS = 6371.0


def get_approximate_distance(
    coord1: tuple[float, float], coord2: tuple[float, float]
) -> float:
    """Get approximate distance between two coordinates using the haversine function.

    The outcome is not exact, but good enough for our purposes.
    Coordinates are expected in the format (longitude, latitude).
    """
    coord1 = (radians(coord1[0]), radians(coord1[1]))
    coord2 = (radians(coord2[0]), radians(coord2[1]))

    longitude_delta = coord2[0] - coord1[0]
    latitude_delta = coord2[1] - coord1[1]

    a = sin(latitude_delta / 2) * sin(latitude_delta / 2) + cos(coord1[1]) * cos(
        coord2[1]
    ) * sin(longitude_delta / 2) * sin(longitude_delta / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS * c
