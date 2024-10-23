import json
from numpy.typing import NDArray
from os.path import isfile
from pytest import mark
from unittest.mock import MagicMock, patch

from hestia_earth.models.ipcc2019.aboveGroundBiomass import (
    _is_lcc_event, _rescale_category_cover, _should_run, MODEL, run, TERM_ID
)
from hestia_earth.models.ipcc2019.aboveGroundBiomass_utils import BiomassCategory, sample_constant

from tests.utils import fake_new_measurement, fixtures_path

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
utils_path = f"hestia_earth.models.{MODEL}.{TERM_ID}_utils"
term_path = "hestia_earth.models.utils.term"
property_path = "hestia_earth.models.utils.property"

fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"

_ITERATIONS = 1000


def _load_fixture(path: str, default=None):
    if isfile(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return default


def _fake_calc_descriptive_stats(arr: NDArray, *_args, **_kwargs):
    return {"value": [round(row[0], 6) for row in arr]}


# subfolder, should_run
PARAMS_SHOULD_RUN = [
    ("forest-to-cropland", True),
    ("forest-to-cropland-greater-than-100", True),
    ("forest-to-cropland-less-than-100", True),
    ("forest-to-cropland-lcc-q2", True),
    ("forest-to-cropland-lcc-q3", True),
    ("forest-to-cropland-lcc-q4", True),
    ("forest-to-orchard", True),
    ("forest-to-orchard-with-backup-factors", True),
    ("forest-to-orchard-with-in-category-lcc", True),
    ("historical-land-cover-mix", True),
    ("historical-argentina-pasture", True),
    ("historical-brazil-maize", True),
    ("perennial-to-grassland-with-pasture-condition", True)
]
IDS_SHOULD_RUN = [p[0] for p in PARAMS_SHOULD_RUN]


@mark.parametrize("subfolder, should_run", PARAMS_SHOULD_RUN, ids=IDS_SHOULD_RUN)
def test_should_run(subfolder: str, should_run: bool):
    folder = f"{fixtures_folder}/{subfolder}"

    site = _load_fixture(f"{folder}/site.jsonld", {})

    result, *_ = _should_run(site)
    assert result == should_run


def test_should_run_no_data():
    SITE = {}
    EXPECTED = False

    result, *_ = _should_run(SITE)
    assert result == EXPECTED


PARAMS_RUN = [subfolder for subfolder, should_run in PARAMS_SHOULD_RUN if should_run]


@mark.parametrize("subfolder", PARAMS_RUN)
@patch(f"{class_path}.calc_descriptive_stats", side_effect=_fake_calc_descriptive_stats)
@patch(f"{class_path}._new_measurement", side_effect=fake_new_measurement)
@patch(f"{utils_path}._get_sample_func", return_value=sample_constant)
def test_run(
    _get_sample_func_mock: MagicMock,
    _new_measurement_mock: MagicMock,
    _calc_descriptive_stats_mock: MagicMock,
    subfolder: str
):
    folder = f"{fixtures_folder}/{subfolder}"

    site = _load_fixture(f"{folder}/site.jsonld", {})
    expected = _load_fixture(f"{folder}/result.jsonld", [])

    with patch(f"{class_path}._ITERATIONS", _ITERATIONS):
        result = run(site)

    assert result == expected


# subfolder
PARAMS_RUN_WITH_STATS = [
    "forest-to-cropland-with-stats",
    "forest-to-orchard-with-in-category-lcc-with-stats",
    "historical-land-cover-mix-with-stats"
]


@mark.parametrize("subfolder", PARAMS_RUN_WITH_STATS)
@patch(f"{class_path}._new_measurement", side_effect=fake_new_measurement)
def test_run_with_stats(
    _new_measurement_mock: MagicMock,
    subfolder: str
):
    folder = f"{fixtures_folder}/{subfolder}"

    site = _load_fixture(f"{folder}/site.jsonld", {})
    expected = _load_fixture(f"{folder}/result.jsonld", [])

    with patch(f"{class_path}._ITERATIONS", _ITERATIONS):
        result = run(site)

    assert result == expected


# input, expected
PARAMS_RESCALE_CATEGORY_COVER = [
    (
        {BiomassCategory.ANNUAL_CROPS: 90},
        {BiomassCategory.ANNUAL_CROPS: 90, BiomassCategory.OTHER: 10}
    ),
    (
        {BiomassCategory.OTHER: 90},
        {BiomassCategory.OTHER: 100}
    ),
    (
        {BiomassCategory.ANNUAL_CROPS: 60, BiomassCategory.VINE: 60},
        {BiomassCategory.ANNUAL_CROPS: 50, BiomassCategory.VINE: 50}
    ),
    (
        {BiomassCategory.NATURAL_FOREST: 100},
        {BiomassCategory.NATURAL_FOREST: 100}
    )
]
IDS_RESCALE_CATEGORY_COVER = ["fill", "fill w/ other", "squash", "do nothing"]


@mark.parametrize("input, expected", PARAMS_RESCALE_CATEGORY_COVER, ids=IDS_RESCALE_CATEGORY_COVER)
def test_rescale_category_cover(input: dict, expected: dict):
    assert _rescale_category_cover(input) == expected


# a, b, expected
PARAMS_IS_LCC_EVENT = [
    (
        {
            "appleTree": 33.333,
            "pearTree": 33.333,
            BiomassCategory.ANNUAL_CROPS: 33.334,
        },
        {
            "appleTree": 33.33333,
            "pearTree": 33.33333,
            BiomassCategory.ANNUAL_CROPS: 33.33334,
        },
        True
    ),
    (
        {
            "appleTree": 33.3333,
            "pearTree": 33.3333,
            BiomassCategory.ANNUAL_CROPS: 33.3334,
        },
        {
            "appleTree": 33.33333,
            "pearTree": 33.33333,
            BiomassCategory.ANNUAL_CROPS: 33.33334,
        },
        False
    )
]
IDS_IS_LCC_EVENT = ["True", "False"]


@mark.parametrize("a, b, expected", PARAMS_IS_LCC_EVENT, ids=IDS_IS_LCC_EVENT)
def test_is_lcc_event(a: dict, b: dict, expected: bool):
    assert _is_lcc_event(a, b) is expected
