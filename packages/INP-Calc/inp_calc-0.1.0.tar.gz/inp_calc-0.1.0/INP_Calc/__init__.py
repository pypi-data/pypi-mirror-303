"""INP_Calc: A module for converting freezing fraction (FF) to concentration, volume, and surface area."""

__version__ = "0.1.0"

from .calculations import FF_to_conc, FF_to_volume, FF_to_surface

# Optionally, you can provide a brief overview of the functions available in the module
__all__ = [
    "FF_to_conc",
    "FF_to_volume",
    "FF_to_surface",
]
