"""Exceptions."""


class HydroOttawaError(Exception):
    """Generic Hydro Ottawa Exception."""


class HydroOttawaConnectionError(HydroOttawaError):
    """Error to indicate we cannot connect."""


class HydroOttawaInvalidAuthError(HydroOttawaError):
    """Error to indicate there is invalid auth."""
