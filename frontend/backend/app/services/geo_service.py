"""Geocoding and geographic helpers.

This module is intentionally minimal; it can be extended to use an external geocoding
provider (e.g. Nominatim, Google Maps) and to perform PostGIS queries.
"""


def geocode_address(address: str) -> dict:
    """Resolve an address to lat/lng coordinates.

    Returns a dict like {"lat": float, "lng": float}.
    """
    # TODO: integrate with a real geocoding provider.
    return {"lat": 0.0, "lng": 0.0}
