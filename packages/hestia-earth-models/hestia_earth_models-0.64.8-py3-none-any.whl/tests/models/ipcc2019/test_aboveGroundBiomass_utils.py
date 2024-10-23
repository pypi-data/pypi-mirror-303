from pytest import mark

from itertools import product
from hestia_earth.models.ipcc2019.aboveGroundBiomass_utils import (
    _build_col_name, _get_sample_func, assign_biomass_category, BiomassCategory, EcoClimateZone,
    sample_biomass_equilibrium, sample_constant, sample_plus_minus_error
)

_ITERATIONS = 1000


# kwargs, sample_func, expected_shape
PARAMS_GET_SAMPLE_FUNC = [
    ({"value": 1}, sample_constant),
    ({"value": 1, "error": 10}, sample_plus_minus_error),
]
IDS_GET_SAMPLE_FUNC = ["constant", "+/- error"]


@mark.parametrize("kwargs, sample_func", PARAMS_GET_SAMPLE_FUNC, ids=IDS_GET_SAMPLE_FUNC)
def test_get_sample_func(kwargs, sample_func):
    result = _get_sample_func(kwargs)
    assert result == sample_func


PARAMS_BIOMASS = [p for p in product(BiomassCategory, EcoClimateZone)]
IDS_BIOMASS = [f"{p[0].name} + {p[1].name}" for p in PARAMS_BIOMASS]


@mark.parametrize("biomass_category, eco_climate_zone", PARAMS_BIOMASS, ids=IDS_BIOMASS)
def test_sample_biomass_equilibrium(biomass_category, eco_climate_zone):
    EXPECTED_SHAPE = (1, _ITERATIONS)
    result = sample_biomass_equilibrium(_ITERATIONS, biomass_category, eco_climate_zone)
    assert result.shape == EXPECTED_SHAPE


# input, expected
PARAMS_ASSIGN_BIOMASS_CATEGORY = [
    ("Annual crops", BiomassCategory.ANNUAL_CROPS),
    ("Coconut", BiomassCategory.COCONUT),
    ("Forest", BiomassCategory.FOREST),
    ("Grassland", BiomassCategory.GRASSLAND),
    ("Jatropha", BiomassCategory.JATROPHA),
    ("Jojoba", BiomassCategory.JOJOBA),
    ("Natural forest", BiomassCategory.NATURAL_FOREST),
    ("Oil palm", BiomassCategory.OIL_PALM),
    ("Olive", BiomassCategory.OLIVE),
    ("Orchard", BiomassCategory.ORCHARD),
    ("Other", BiomassCategory.OTHER),
    ("Plantation forest", BiomassCategory.PLANTATION_FOREST),
    ("Rubber", BiomassCategory.RUBBER),
    ("Short rotation coppice", BiomassCategory.SHORT_ROTATION_COPPICE),
    ("Tea", BiomassCategory.TEA),
    ("Vine", BiomassCategory.VINE),
    ("Woody perennial", BiomassCategory.WOODY_PERENNIAL),
    ("Miscellaneous value", None)
]
IDS_ASSIGN_BIOMASS_CATEGORY = [p[0] for p in PARAMS_ASSIGN_BIOMASS_CATEGORY]


@mark.parametrize("input, expected", PARAMS_ASSIGN_BIOMASS_CATEGORY, ids=IDS_ASSIGN_BIOMASS_CATEGORY)
def test_assign_biomass_category(input: str, expected: BiomassCategory):
    assert assign_biomass_category(input) == expected


# input, expected
PARAMS_BUILD_COLUMN_NAME = [
    (BiomassCategory.ANNUAL_CROPS, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_ANNUAL_CROPS"),
    (BiomassCategory.COCONUT, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_COCONUT"),
    (BiomassCategory.FOREST, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_FOREST"),
    (BiomassCategory.GRASSLAND, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_GRASSLAND"),
    (BiomassCategory.JATROPHA, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_JATROPHA"),
    (BiomassCategory.JOJOBA, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_JOJOBA"),
    (BiomassCategory.NATURAL_FOREST, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_NATURAL_FOREST"),
    (BiomassCategory.OIL_PALM, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_OIL_PALM"),
    (BiomassCategory.OLIVE, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_OLIVE"),
    (BiomassCategory.ORCHARD, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_ORCHARD"),
    (BiomassCategory.OTHER, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_OTHER"),
    (BiomassCategory.PLANTATION_FOREST, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_PLANTATION_FOREST"),
    (BiomassCategory.RUBBER, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_RUBBER"),
    (BiomassCategory.SHORT_ROTATION_COPPICE, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_SHORT_ROTATION_COPPICE"),
    (BiomassCategory.TEA, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_TEA"),
    (BiomassCategory.VINE, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_VINE"),
    (BiomassCategory.WOODY_PERENNIAL, "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_WOODY_PERENNIAL"),
    ("Miscellaneous value", "AG_BIOMASS_EQUILIBRIUM_KG_C_HECTARE_OTHER")
]
IDS_BUILD_COLUMN_NAME = [p[0] for p in PARAMS_BUILD_COLUMN_NAME]


@mark.parametrize("input, expected", PARAMS_BUILD_COLUMN_NAME, ids=IDS_BUILD_COLUMN_NAME)
def test_build_col_name(input: BiomassCategory, expected: str):
    assert _build_col_name(input) == expected
