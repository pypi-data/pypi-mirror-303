from enum import Enum
from functools import reduce
from math import isclose
from numpy import average, copy, random, vstack
from numpy.typing import NDArray
from typing import Callable, Optional, Union

from hestia_earth.schema import (
    MeasurementMethodClassification,
    MeasurementStatsDefinition,
    SiteSiteType,
    TermTermType
)

from hestia_earth.utils.blank_node import get_node_value
from hestia_earth.utils.model import filter_list_term_type
from hestia_earth.utils.tools import non_empty_list

from hestia_earth.models.log import log_as_table, logRequirements, logShouldRun
from hestia_earth.models.utils import pairwise
from hestia_earth.models.utils.array_builders import gen_seed
from hestia_earth.models.utils.blank_node import group_nodes_by_year
from hestia_earth.models.utils.descriptive_stats import calc_descriptive_stats
from hestia_earth.models.utils.ecoClimateZone import EcoClimateZone, get_eco_climate_zone_value
from hestia_earth.models.utils.measurement import _new_measurement
from hestia_earth.models.utils.term import get_lookup_value

from . import MODEL
from .aboveGroundBiomass_utils import assign_biomass_category, BiomassCategory, sample_biomass_equilibrium


REQUIREMENTS = {
    "Site": {
        "siteType": ["cropland", "permanent pasture", "forest", "other natural vegetation"],
        "management": [
            {
                "@type": "Management",
                "value": "",
                "term.termType": "landCover",
                "endDate": "",
                "optional": {
                    "startDate": ""
                }
            }
        ],
        "measurements": [
            {
                "@type": "Measurement",
                "value": ["1", "2", "3", "4", "7", "8", "9", "10", "11", "12"],
                "term.@id": "ecoClimateZone"
            }
        ]
    }
}
LOOKUPS = {
    "landCover": "BIOMASS_CATEGORY",
    "ecoClimateZone": [
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_ANNUAL_CROPS",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_COCONUT",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_FOREST",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_GRASSLAND",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_JATROPHA",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_JOJOBA",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_NATURAL_FOREST",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_OIL_PALM",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_OLIVE",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_ORCHARD",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_PLANTATION_FOREST",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_RUBBER",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_SHORT_ROTATION_COPPICE",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_TEA",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_VINE",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_WOODY_PERENNIAL",
        "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_OTHER"
    ]
}
RETURNS = {
    "Measurement": [{
        "value": "",
        "sd": "",
        "min": "",
        "max": "",
        "statsDefinition": "simulated",
        "observations": "",
        "dates": "",
        "methodClassification": "tier 1 model"
    }]
}
TERM_ID = 'aboveGroundBiomass'

_ITERATIONS = 10000
_METHOD_CLASSIFICATION = MeasurementMethodClassification.TIER_1_MODEL.value
_STATS_DEFINITION = MeasurementStatsDefinition.SIMULATED.value

_LAND_COVER_TERM_TYPE = TermTermType.LANDCOVER
_TARGET_LAND_COVER = 100

_EQUILIBRIUM_TRANSITION_PERIOD = 20
_EXCLUDED_ECO_CLIMATE_ZONES = {EcoClimateZone.POLAR_MOIST, EcoClimateZone.POLAR_DRY}
_VALID_SITE_TYPES = {
    SiteSiteType.CROPLAND.value,
    SiteSiteType.FOREST.value,
    SiteSiteType.OTHER_NATURAL_VEGETATION.value,
    SiteSiteType.PERMANENT_PASTURE.value
}

_GROUP_LAND_COVER_BY_BIOMASS_CATEGORY = [
    BiomassCategory.ANNUAL_CROPS,
    BiomassCategory.GRASSLAND,
    BiomassCategory.OTHER,
    BiomassCategory.SHORT_ROTATION_COPPICE
]
"""
Terms associated with these biomass categories can be grouped together when summarising land cover coverage in
`_group_by_term_id`.
"""


class _InventoryKey(Enum):
    """
    The inner keys of the annualised inventory created by the `_compile_inventory` function.

    The value of each enum member is formatted to be used as a column header in the `log_as_table` function.
    """
    BIOMASS_CATEGORY_SUMMARY = "biomass-categories"
    LAND_COVER_SUMMARY = "land-cover-categories"
    LAND_COVER_CHANGE_EVENT = "lcc-event"
    YEARS_SINCE_LCC_EVENT = "years-since-lcc-event"
    REGIME_START_YEAR = "regime-start-year"


_REQUIRED_INVENTORY_KEYS = [e for e in _InventoryKey]


def run(site: dict) -> list[dict]:
    """
    Run the model on a Site.

    Parameters
    ----------
    site : dict
        A valid HESTIA [Site](https://www.hestia.earth/schema/Site).

    Returns
    -------
    list[dict]
        A list of HESTIA [Measurement](https://www.hestia.earth/schema/Measurement) nodes with `term.termType` =
        `aboveGroundBiomass`
    """
    should_run, inventory, kwargs = _should_run(site)
    return _run(inventory, iterations=_ITERATIONS, **kwargs) if should_run else []


def _should_run(site: dict) -> tuple[bool, dict, dict]:
    """
    Extract and re-organise required data from the input [Site](https://www.hestia.earth/schema/Site) node and determine
    whether the model should run.

    Parameters
    ----------
    site : dict
        A valid HESTIA [Site](https://www.hestia.earth/schema/Site).

    Returns
    -------
    tuple[bool, dict, dict]
        should_run, inventory, kwargs
    """
    site_type = site.get("siteType")
    eco_climate_zone = get_eco_climate_zone_value(site, as_enum=True)

    land_cover = filter_list_term_type(site.get("management", []), _LAND_COVER_TERM_TYPE)

    has_valid_site_type = site_type in _VALID_SITE_TYPES
    has_valid_eco_climate_zone = all([
        eco_climate_zone,
        eco_climate_zone not in _EXCLUDED_ECO_CLIMATE_ZONES
    ])
    has_land_cover_nodes = len(land_cover) > 0

    should_compile_inventory = all([
        has_valid_site_type,
        has_valid_eco_climate_zone,
        has_land_cover_nodes
    ])

    inventory = _compile_inventory(land_cover) if should_compile_inventory else {}
    kwargs = {
        "eco_climate_zone": eco_climate_zone,
        "seed": gen_seed(site)
    }

    logRequirements(
        site, model=MODEL, term=TERM_ID,
        site_type=site_type,
        has_valid_site_type=has_valid_site_type,
        has_valid_eco_climate_zone=has_valid_eco_climate_zone,
        has_land_cover_nodes=has_land_cover_nodes,
        **kwargs,
        inventory=_format_inventory(inventory)
    )

    should_run = all([
        len(inventory) > 0,
        all(data for data in inventory.values() if all(key in data.keys() for key in _REQUIRED_INVENTORY_KEYS))
    ])

    logShouldRun(site, MODEL, TERM_ID, should_run)

    return should_run, inventory, kwargs


def _compile_inventory(land_cover_nodes: list[dict]) -> dict:
    """
    Build an annual inventory of model input data.

    Returns a dict with shape:
    ```
    {
        year (int): {
            _InventoryKey.BIOMASS_CATEGORY_SUMMARY: {
                category (BiomassCategory): value (float),
                ...categories
            },
            _InventoryKey.LAND_COVER_SUMMARY: {
                category (str | BiomassCategory): value (float),
                ...categories
            },
            _InventoryKey.LAND_COVER_CHANGE_EVENT: value (bool),
            _InventoryKey.YEARS_SINCE_LCC_EVENT: value (int),
            _InventoryKey.REGIME_START_YEAR: value (int)
        },
        ...years
    }
    ```

    Parameters
    ----------
    land_cover_nodes : list[dict]
        A list of HESTIA [Management](https://www.hestia.earth/schema/Measurement) nodes with `term.termType` =
        `landCover`

    Returns
    -------
    dict
        The inventory of data.
    """
    land_cover_grouped = group_nodes_by_year(land_cover_nodes)

    def build_inventory_year(inventory: dict, year_pair: tuple[int, int]) -> dict:
        """
        Build a year of the inventory using the data from `land_cover_categories_grouped`.

        Parameters
        ----------
        inventory: dict
            The land cover change portion of the inventory. Must have the same shape as the returned dict.
        year_pair : tuple[int, int]
            A tuple with the shape `(prev_year, current_year)`.

        Returns
        -------
        dict
            The land cover change portion of the inventory.
        """

        prev_year, current_year = year_pair
        land_cover_nodes = land_cover_grouped.get(current_year, {})

        biomass_category_summary = _summarise_land_cover_nodes(land_cover_nodes, _group_by_biomass_category)
        land_cover_summary = _summarise_land_cover_nodes(land_cover_nodes, _group_by_term_id)

        prev_land_cover_summary = inventory.get(prev_year, {}).get(_InventoryKey.LAND_COVER_SUMMARY, {})

        is_lcc_event = _is_lcc_event(land_cover_summary, prev_land_cover_summary)

        time_delta = current_year - prev_year
        prev_years_since_lcc_event = inventory.get(prev_year, {}).get(_InventoryKey.YEARS_SINCE_LCC_EVENT, 0)
        years_since_lcc_event = time_delta if is_lcc_event else prev_years_since_lcc_event + time_delta
        regime_start_year = current_year - years_since_lcc_event

        update_dict = {
            current_year: {
                _InventoryKey.BIOMASS_CATEGORY_SUMMARY: biomass_category_summary,
                _InventoryKey.LAND_COVER_SUMMARY: land_cover_summary,
                _InventoryKey.LAND_COVER_CHANGE_EVENT: is_lcc_event,
                _InventoryKey.YEARS_SINCE_LCC_EVENT: years_since_lcc_event,
                _InventoryKey.REGIME_START_YEAR: regime_start_year
            }
        }
        return inventory | update_dict

    start_year = list(land_cover_grouped)[0]
    initial_land_cover_nodes = land_cover_grouped.get(start_year, {})

    initial = {
        start_year: {
            _InventoryKey.BIOMASS_CATEGORY_SUMMARY: _summarise_land_cover_nodes(
                initial_land_cover_nodes, _group_by_biomass_category
            ),
            _InventoryKey.LAND_COVER_SUMMARY: _summarise_land_cover_nodes(
                initial_land_cover_nodes, _group_by_term_id
            ),
            _InventoryKey.LAND_COVER_CHANGE_EVENT: False,
            _InventoryKey.YEARS_SINCE_LCC_EVENT: _EQUILIBRIUM_TRANSITION_PERIOD,
            _InventoryKey.REGIME_START_YEAR: start_year - _EQUILIBRIUM_TRANSITION_PERIOD
        }
    }

    return reduce(
        build_inventory_year,
        pairwise(land_cover_grouped.keys()),  # Inventory years need data from previous year to be compiled.
        initial
    )


def _group_by_biomass_category(result: dict[BiomassCategory, float], node: dict) -> dict[BiomassCategory, float]:
    """
    Reducer function for `_group_land_cover_nodes_by` that groups and sums node value by their associated
    `BiomassCategory`.

    Parameters
    ----------
    result : dict
        A dict with the shape `{category (BiomassCategory): sum_value (float), ...categories}`.
    node : dict
        A HESTIA `Management` node with `term.termType` = `landCover`.

    Returns
    -------
    result : dict
        A dict with the shape `{category (BiomassCategory): sum_value (float), ...categories}`.
    """
    biomass_category = _retrieve_biomass_category(node)
    value = get_node_value(node)

    update_dict = {biomass_category: result.get(biomass_category, 0) + value}

    should_run = biomass_category and value
    return result | update_dict if should_run else result


def _group_by_term_id(
    result: dict[Union[str, BiomassCategory], float], node: dict
) -> dict[Union[str, BiomassCategory], float]:
    """
    Reducer function for `_group_land_cover_nodes_by` that groups and sums node value by their `term.@id` if a the land
    cover is a woody plant, else by their associated `BiomassCategory`

    Land cover events can be triggered by changes in land cover within the same `BiomassCategory` (e.g., `peachTree` to
    `appleTree`) due to the requirement to clear the previous woody biomass to establish the new land cover.

    Some land covers (e.g., land covers associated with the `BiomassCategory` = `Annual crops`, `Grassland`, `Other` or
    `Short rotation coppice`) are exempt from this rule due to the Tier 1 assumptions that biomass does not accumulate
    within the category or the maturity cycle of the land cover is significantly shorter than the amortisation period of
    20 years.

    Parameters
    ----------
    result : dict
        A dict with the shape `{category (str | BiomassCategory): sum_value (float), ...categories}`.
    node : dict
        A HESTIA `Management` node with `term.termType` = `landCover`.

    Returns
    -------
    result : dict
        A dict with the shape `{category (str | BiomassCategory): sum_value (float), ...categories}`.
    """
    term_id = node.get("term", {}).get("@id")
    biomass_category = _retrieve_biomass_category(node)
    value = get_node_value(node)

    key = biomass_category if biomass_category in _GROUP_LAND_COVER_BY_BIOMASS_CATEGORY else term_id

    update_dict = {key: result.get(key, 0) + value}

    should_run = biomass_category and value
    return result | update_dict if should_run else result


def _retrieve_biomass_category(node: dict) -> Optional[BiomassCategory]:
    """
    Retrieve the `BiomassCategory` associated with a land cover using the `BIOMASS_CATEGORY` lookup.

    If lookup value is missing, return `None`.

    Parameters
    ----------
    node : dict
        A valid `Management` node with `term.termType` = `landCover`.

    Returns
    -------
    BiomassCategory | None
        The associated `BiomassCategory` or `None`
    """
    LOOKUP = LOOKUPS["landCover"]
    term = node.get("term", {})
    lookup_value = get_lookup_value(term, LOOKUP)

    return assign_biomass_category(lookup_value) if lookup_value else None


def _summarise_land_cover_nodes(
    land_cover_nodes: list[dict],
    group_by_func: Callable[[dict, dict], dict] = _group_by_biomass_category
) -> dict[Union[str, BiomassCategory], float]:
    """
    Group land cover nodes using `group_by_func`.

    Parameters
    ----------
    land_cover_nodes : list[dict]
        A list of HESTIA `Management` nodes with `term.termType` = `landCover`.

    Returns
    -------
    result : dict
        A dict with the shape `{category (str | BiomassCategory): sum_value (float), ...categories}`.
    """
    category_cover = reduce(group_by_func, land_cover_nodes, dict())
    return _rescale_category_cover(category_cover)


def _rescale_category_cover(
    category_cover: dict[Union[BiomassCategory, str], float]
) -> dict[Union[BiomassCategory, str], float]:
    """
    Enforce a land cover coverage of 100%.

    If input coverage is less than 100%, fill the remainder with `BiomassCategory.OTHER`. If the input coverage is
    greater than 100%, proportionally downscale all categories.

    Parameters
    ----------
    category_cover : dict[BiomassCategory | str, float]
        The input category cover dict.

    Returns
    -------
    result : dict[BiomassCategory | str, float]
        The rescaled category cover dict.
    """
    total_cover = sum(category_cover.values())
    return (
        _fill_category_cover(category_cover) if total_cover < _TARGET_LAND_COVER
        else _squash_category_cover(category_cover) if total_cover > _TARGET_LAND_COVER
        else category_cover
    )


def _fill_category_cover(
    category_cover:  dict[Union[BiomassCategory, str], float]
) -> dict[Union[BiomassCategory, str], float]:
    """
    Fill the land cover coverage with `BiomassCategory.OTHER` to enforce a total coverage of 100%.

    Parameters
    ----------
    category_cover : dict[BiomassCategory | str, float]
        The input category cover dict.

    Returns
    -------
    result : dict[BiomassCategory | str, float]
        The rescaled category cover dict.
    """
    total_cover = sum(category_cover.values())
    update_dict = {
        BiomassCategory.OTHER: category_cover.get(BiomassCategory.OTHER, 0) + (_TARGET_LAND_COVER - total_cover)
    }
    return category_cover | update_dict


def _squash_category_cover(
    category_cover: dict[Union[BiomassCategory, str], float]
) -> dict[Union[BiomassCategory, str], float]:
    """
    Proportionally shrink all land cover categories to enforce a total coverage of 100%.

    Parameters
    ----------
    category_cover : dict[BiomassCategory | str, float]
        The input category cover dict.

    Returns
    -------
    result : dict[BiomassCategory | str, float]
        The rescaled category cover dict.
    """
    total_cover = sum(category_cover.values())
    return {
        category: (cover / total_cover) * _TARGET_LAND_COVER
        for category, cover in category_cover.items()
    }


def _is_lcc_event(
    a: dict[Union[BiomassCategory, str], float],
    b: dict[Union[BiomassCategory, str], float]
) -> bool:
    """
    Land cover values (% area) are compared with an absolute tolerance of 0.0001, which is equivalent to 1 m2 per
    hectare.

    Parameters
    ----------
    a : dict[BiomassCategory | str, float]
        The first land-cover summary dict.
    b : dict[BiomassCategory | str, float]
        The second land-cover summary dict.

    Returns
    -------
    bool
        Whether a land-cover change event has occured.
    """
    keys_match = sorted(str(key) for key in b.keys()) == sorted(str(key) for key in a.keys())
    values_close = all(
        isclose(b.get(key), a.get(key, -999), abs_tol=0.0001) for key in b.keys()
    )

    return not all([keys_match, values_close])


def _format_inventory(inventory: dict) -> str:
    """
    Format the SOC inventory for logging as a table. Rows represent inventory years, columns represent soc stock change
    data for each measurement method classification present in inventory. If the inventory is invalid, return `"None"`
    as a string.
    """
    inventory_years = sorted(set(non_empty_list(years for years in inventory.keys())))
    land_covers = _get_unique_categories(inventory, _InventoryKey.LAND_COVER_SUMMARY)
    inventory_keys = _get_loggable_inventory_keys(inventory)

    should_run = inventory and len(inventory_years) > 0

    return log_as_table(
        {
            "year": year,
            **{
                _format_column_header(category): _format_number(
                    inventory.get(year, {}).get(_InventoryKey.LAND_COVER_SUMMARY, {}).get(category, 0)
                ) for category in land_covers
            },
            **{
                _format_column_header(key): _INVENTORY_KEY_TO_FORMAT_FUNC[key](
                    inventory.get(year, {}).get(key)
                ) for key in inventory_keys
            }
        } for year in inventory_years
    ) if should_run else "None"


def _get_unique_categories(inventory: dict, key: _InventoryKey) -> list:
    """
    Extract the unique biomass or land cover categories from the inventory.

    Can be used to cache sampled parameters for each `BiomassCategory` or to log land covers.
    """
    categories = reduce(
        lambda result, categories: result | set(categories),
        (inner.get(key, {}).keys() for inner in inventory.values()),
        set()
    )
    return sorted(
        categories,
        key=lambda category: category.value if isinstance(category, Enum) else str(category),
    )


def _get_loggable_inventory_keys(inventory: dict) -> list:
    """
    Return a list of unique inventory keys in a fixed order.
    """
    unique_keys = reduce(
        lambda result, keys: result | set(keys),
        (
            (key for key in group.keys() if key in _INVENTORY_KEY_TO_FORMAT_FUNC)
            for group in inventory.values()
        ),
        set()
    )
    key_order = {key: i for i, key in enumerate(_INVENTORY_KEY_TO_FORMAT_FUNC.keys())}
    return sorted(unique_keys, key=lambda key_: key_order[key_])


def _format_bool(value: Optional[bool]) -> str:
    """Format a bool for logging in a table."""
    return str(bool(value))


def _format_number(value: Optional[float]) -> str:
    """Format a float for logging in a table."""
    return f"{value:.1f}" if isinstance(value, (float, int)) else "None"


def _format_column_header(value: Union[_InventoryKey, BiomassCategory, str]):
    """Format an enum or str for logging as a table column header."""
    as_string = value.value if isinstance(value, Enum) else str(value)
    return as_string.replace(" ", "-")


_INVENTORY_KEY_TO_FORMAT_FUNC = {
    _InventoryKey.LAND_COVER_CHANGE_EVENT: _format_bool,
    _InventoryKey.YEARS_SINCE_LCC_EVENT: _format_number
}
"""
Map inventory keys to format functions. The columns in inventory logged as a table will also be sorted in the order of
the `dict` keys.
"""


def _run(
    inventory: dict,
    *,
    eco_climate_zone: EcoClimateZone,
    iterations: int,
    seed: Union[int, random.Generator, None] = None
) -> list[dict]:
    """
    Calculate the annual above ground biomass stock based on an inventory of land cover data.

    Inventory should be a dict with shape:
    ```
    {
        year (int): {
            _InventoryKey.BIOMASS_CATEGORY_SUMMARY: {
                category (BiomassCategory): value (float),
                ...categories
            },
            _InventoryKey.LAND_COVER_SUMMARY: {
                category (str | BiomassCategory): value (float),
                ...categories
            },
            _InventoryKey.LAND_COVER_CHANGE_EVENT: value (bool),
            _InventoryKey.YEARS_SINCE_LCC_EVENT: value (int),
            _InventoryKey.REGIME_START_YEAR: value (int)
        },
        ...years
    }
    ```

    Parameters
    ----------
    inventory : dict
        The annual inventory of land cover data.
    ecoClimateZone : EcoClimateZone
        The eco-climate zone of the site.
    iterations: int
        The number of iterations to run the model as a Monte Carlo simulation.
    seed : int | random.Generator | None
        The seed for the random sampling of model parameters.

    Returns
    -------
    list[dict]
        A list of HESTIA [Measurement](https://www.hestia.earth/schema/Measurement) nodes with `term.termType` =
        `aboveGroundBiomass`
    """
    rng = random.default_rng(seed)
    unique_biomass_categories = _get_unique_categories(inventory, _InventoryKey.BIOMASS_CATEGORY_SUMMARY)

    timestamps = list(inventory.keys())

    factor_cache = {
        category: sample_biomass_equilibrium(iterations, category, eco_climate_zone, rng)
        for category in unique_biomass_categories
    }

    def get_average_equilibrium(year) -> NDArray:
        biomass_categories = inventory.get(year, {}).get(_InventoryKey.BIOMASS_CATEGORY_SUMMARY, {})
        values = [factor_cache.get(category) for category in biomass_categories.keys()]
        weights = [weight for weight in biomass_categories.values()]
        return average(values, axis=0, weights=weights)

    equilibrium_annual = vstack([get_average_equilibrium(year) for year in inventory.keys()])

    def calc_biomass_stock(result: NDArray, index_year: tuple[int, int]) -> NDArray:
        index, year = index_year

        years_since_llc_event = inventory.get(year, {}).get(_InventoryKey.YEARS_SINCE_LCC_EVENT, 0)
        regime_start_year = inventory.get(year, {}).get(_InventoryKey.REGIME_START_YEAR, 0)
        regime_start_index = (
            timestamps.index(regime_start_year) if regime_start_year in timestamps else 0
        )

        regime_start_biomass = result[regime_start_index]
        current_biomass_equilibrium = equilibrium_annual[index]

        time_ratio = min(years_since_llc_event / _EQUILIBRIUM_TRANSITION_PERIOD, 1)
        biomass_delta = (current_biomass_equilibrium - regime_start_biomass) * time_ratio

        result[index] = regime_start_biomass + biomass_delta
        return result

    biomass_annual = reduce(
        calc_biomass_stock,
        list(enumerate(timestamps))[1:],
        copy(equilibrium_annual)
    )

    descriptive_stats = calc_descriptive_stats(
        biomass_annual,
        _STATS_DEFINITION,
        axis=1,     # Calculate stats rowwise.
        decimals=6  # Round values to the nearest milligram.
    )
    return [_measurement(timestamps, **descriptive_stats)]


def _measurement(
    timestamps: list[int],
    value: list[float],
    *,
    sd: list[float] = None,
    min: list[float] = None,
    max: list[float] = None,
    statsDefinition: str = None,
    observations: list[int] = None
) -> dict:
    """
    Build a Hestia `Measurement` node to contain a value and descriptive statistics calculated by the models.

    Parameters
    ----------
    timestamps : list[int]
        A list of calendar years associated to the calculated SOC stocks.
    value : list[float]
        A list of values representing the mean biomass stock for each year of the inventory
    sd : list[float]
        A list of standard deviations representing the standard deviation of the biomass stock for each year of the
        inventory.
    min : list[float]
        A list of minimum values representing the minimum modelled biomass stock for each year of the inventory.
    max : list[float]
        A list of maximum values representing the maximum modelled biomass stock for each year of the inventory.
    statsDefinition : str
        The [statsDefinition](https://www-staging.hestia.earth/schema/Measurement#statsDefinition) of the measurement.
    observations : list[int]
        The number of model iterations used to calculate the descriptive statistics.

    Returns
    -------
    dict
        A valid HESTIA `Measurement` node, see: https://www.hestia.earth/schema/Measurement.
    """
    update_dict = {
        "value": value,
        "sd": sd,
        "min": min,
        "max": max,
        "statsDefinition": statsDefinition,
        "observations": observations,
        "dates": [f"{year}-12-31" for year in timestamps],
        "methodClassification": _METHOD_CLASSIFICATION
    }
    measurement = _new_measurement(TERM_ID) | {
        key: value for key, value in update_dict.items() if value
    }
    return measurement
