import json
from unittest.mock import patch

from hestia_earth.models.environmentalFootprintV3.soilQualityIndexLandTransformation import MODEL, TERM_ID, run, \
    _should_run
from tests.utils import fixtures_path, fake_new_indicator

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"


def fake_rounded_indicator(value: float):
    indicator = fake_new_indicator(TERM_ID, MODEL)
    indicator['value'] = round(value, 7)
    return indicator


def test_should_run_ocean(*args):
    """
    Should not run if a LandCover has no CF (ocean)
    """
    with open(f"{fixtures_folder}/bad-sites/site-LandCover-has-no-CF.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    should_run, *args = _should_run(site)
    assert should_run is False


def test_should_run_no_management_entries(*args):
    """
    no management => no run
    """
    with open(f"{fixtures_folder}/bad-sites/site-no-management.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    should_run, *args = _should_run(site)
    assert should_run is False


def test_should_run_no_sites(*args):
    """
    impact assessment with no site => no run
    """
    with open(f"{fixtures_path}/impact_assessment/emissions/impact-assessment.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    should_run, *args = _should_run(site)
    assert should_run is False


def test_should_run_no_transformation(*args):
    """
    1 management with no transformation => no run
    """
    with open(f"{fixtures_folder}/bad-sites/site-no-transformations.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    should_run, *args = _should_run(site)
    assert should_run is False


@patch(f"{class_path}._indicator", side_effect=fake_rounded_indicator)
def test_run_in_cycle(*args):
    with open(f"{fixtures_folder}/Italy/site-italy-inside-cycle.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    with open(f"{fixtures_folder}/Italy/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(site)
    assert value == expected


@patch(f"{class_path}._indicator", side_effect=fake_rounded_indicator)
def test_run_other_sites(*args):
    with open(f"{fixtures_folder}/Italy/site-italy-otherSites.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    with open(f"{fixtures_folder}/Italy/result-otherSites.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(site)
    assert value == expected


@patch(f"{class_path}._indicator", side_effect=fake_rounded_indicator)
def test_run_with_region(*args):
    """
    When given valid sub-region or country not in the lookup file should default to 'region-world'
    """
    with open(f"{fixtures_folder}/region-world/region-europe.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    with open(f"{fixtures_folder}/region-world/result-default-region-world.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(site)
    assert value == expected


@patch(f"{class_path}._indicator", side_effect=fake_rounded_indicator)
def test_run_with_no_region(*args):
    """
    When no location is specified, defaults to region world.
    """
    with open(f"{fixtures_folder}/region-world/no-region.jsonld", encoding='utf-8') as f:
        site = json.load(f)

    with open(f"{fixtures_folder}/region-world/result-default-region-world.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(site)
    assert value == expected
