from enum import Enum
from numpy import random
from numpy.typing import NDArray
from typing import Callable, Optional, Union

from hestia_earth.models.utils.array_builders import repeat_single, truncated_normal_1d
from hestia_earth.models.utils.ecoClimateZone import EcoClimateZone, get_ecoClimateZone_lookup_grouped_value


class BiomassCategory(Enum):
    """
    Enum representing biomass categories, sourced from IPCC (2006), IPCC (2019) and European Commission (2010).

    Enum values formatted for logging as table.
    """
    ANNUAL_CROPS = "annual-crops"
    COCONUT = "coconut"                                             # European Commission (2010)
    FOREST = "forest"                                               # IPCC (2019) recalculated per eco-climate zone
    GRASSLAND = "grassland"
    JATROPHA = "jatropha"                                           # European Commission (2010)
    JOJOBA = "jojoba"                                               # European Commission (2010)
    NATURAL_FOREST = "natural-forest"                               # IPCC (2019) recalculated per eco-climate zone
    OIL_PALM = "oil palm"                                           # IPCC (2019)
    OLIVE = "olive"                                                 # IPCC (2019)
    ORCHARD = "orchard"                                             # IPCC (2019)
    OTHER = "other"
    PLANTATION_FOREST = "plantation-forest"                         # IPCC (2019) recalculated per eco-climate zone
    RUBBER = "rubber"                                               # IPCC (2019)
    SHORT_ROTATION_COPPICE = "short-rotation-coppice"               # IPCC (2019)
    TEA = "tea"                                                     # IPCC (2019)
    VINE = "vine"                                                   # IPCC (2019)
    WOODY_PERENNIAL = "woody-perennial"                             # IPCC (2006)


BIOMASS_CATEGORY_TO_LAND_COVER_LOOKUP_VALUE = {
    BiomassCategory.ANNUAL_CROPS: "Annual crops",
    BiomassCategory.COCONUT: "Coconut",
    BiomassCategory.FOREST: "Forest",
    BiomassCategory.GRASSLAND: "Grassland",
    BiomassCategory.JATROPHA: "Jatropha",
    BiomassCategory.JOJOBA: "Jojoba",
    BiomassCategory.NATURAL_FOREST: "Natural forest",
    BiomassCategory.OIL_PALM: "Oil palm",
    BiomassCategory.OLIVE: "Olive",
    BiomassCategory.ORCHARD: "Orchard",
    BiomassCategory.OTHER: "Other",
    BiomassCategory.PLANTATION_FOREST: "Plantation forest",
    BiomassCategory.RUBBER: "Rubber",
    BiomassCategory.SHORT_ROTATION_COPPICE: "Short rotation coppice",
    BiomassCategory.TEA: "Tea",
    BiomassCategory.VINE: "Vine",
    BiomassCategory.WOODY_PERENNIAL: "Woody perennial"
}


def assign_biomass_category(lookup_value: str) -> BiomassCategory:
    """
    Return the `BiomassCategory` enum member associated with the input lookup value. If lookup value is missing or
    doesn't map to any category, return `None`.
    """
    return next(
        (key for key, value in BIOMASS_CATEGORY_TO_LAND_COVER_LOOKUP_VALUE.items() if value == lookup_value),
        None
    )


def sample_biomass_equilibrium(
    iterations: int,
    biomass_category: BiomassCategory,
    eco_climate_zone: EcoClimateZone,
    seed: Union[int, random.Generator, None] = None
) -> dict:
    """
    Sample a biomass equilibrium using the function specified in `KWARGS_TO_SAMPLE_FUNC`.

    Parameters
    ----------
    iterations : int
        The number of samples to take.
    biomass_category : BiomassCategory
        The biomass category of the land cover.
    eco_climate_zone : EcoClimateZone
        The eco-climate zone of the site.
    seed : int | Generator | None, optional
        A seed to initialize the BitGenerator. If passed a Generator, it will be returned unaltered. If `None`, then
        fresh, unpredictable entropy will be pulled from the OS.

    Returns
    -------
    NDArray
        The sampled parameter as a numpy array with shape `(1, iterations)`.
    """
    kwargs = _get_biomass_equilibrium(biomass_category, eco_climate_zone)
    func = _get_sample_func(kwargs)
    return func(iterations=iterations, seed=seed, **kwargs)


def _get_biomass_equilibrium(biomass_category: BiomassCategory, eco_climate_zone: EcoClimateZone) -> dict:
    """
    Retrieve the biomass equilibrium data for a specific combination of biomass category and eco-climate zone.

    Parameters
    ----------
    biomass_category : BiomassCategory
        The biomass category of the land cover.
    eco_climate_zone : EcoClimateZone
        The eco-climate zone of the site.

    Returns
    -------
    dict
        The biomass equilibrium data.
    """
    return get_ecoClimateZone_lookup_grouped_value(
        eco_climate_zone.value,
        _build_col_name(biomass_category),
        default={"value": 0}
    )


def _build_col_name(biomass_category: BiomassCategory) -> str:
    """
    Get the column name for the `ecoClimateZone-lookup.csv` for a specific biomass category equilibrium.
    """
    COL_NAME_ROOT = "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_"
    return (
        f"{COL_NAME_ROOT}{biomass_category.name}" if isinstance(biomass_category, BiomassCategory)
        else f"{COL_NAME_ROOT}OTHER"
    )


def _get_sample_func(kwargs: dict) -> Callable:
    """
    Select the correct sample function for a parameter based on the distribution data available. All possible
    parameters for the model should have, at a minimum, a `value`, meaning that no default function needs to be
    specified.

    This function has been extracted into it's own method to allow for mocking of sample function.

    Keyword Args
    ------------
    value : float
        The distribution mean.
    sd : float
        The standard deviation of the distribution.
    uncertainty : float
        The +/- uncertainty of the 95% confidence interval expressed as a percentage of the mean.
    error : float
        Two standard deviations expressed as a percentage of the mean.

    Returns
    -------
    Callable
        The sample function for the distribution.
    """
    return next(
        sample_func for required_kwargs, sample_func in _KWARGS_TO_SAMPLE_FUNC.items()
        if all(kwarg in kwargs.keys() for kwarg in required_kwargs)
    )


def sample_plus_minus_error(
    *, iterations: int, value: float, error: float, seed: Optional[int] = None, **_
) -> NDArray:
    """Randomly sample a model parameter with a truncated normal distribution described using plus/minus error."""
    sd = value * (error / 200)
    low = value - (value * (error / 100))
    high = value + (value * (error / 100))
    return truncated_normal_1d(shape=(1, iterations), mu=value, sigma=sd, low=low, high=high, seed=seed)


def sample_constant(*, iterations: int, value: float, **_) -> NDArray:
    """Sample a constant model parameter."""
    return repeat_single(shape=(1, iterations), value=value)


_KWARGS_TO_SAMPLE_FUNC = {
    ("value", "error"): sample_plus_minus_error,
    ("value",): sample_constant
}
