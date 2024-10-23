import json
from unittest.mock import patch

from hestia_earth.models.environmentalFootprintV3.soilQualityIndexLandOccupation import MODEL, TERM_ID, run, _should_run
from tests.utils import fixtures_path, fake_new_indicator

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"


with open(f"{fixtures_path}/impact_assessment/emissions/impact-assessment.jsonld", encoding='utf-8') as f:
    impact = json.load(f)


def test_should_run():
    with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    # a LandCover type with no CF => no run
    cycle['site']['management'] = [{"endDate": "2024-03-31", "@type": "Management",
                                    "term": {"termType": "landCover", "@type": "Term", "@id": "ocean"}}]

    should_run, *args = _should_run({'cycle': cycle})
    assert not should_run

    # no management => no run
    cycle['site']['management'] = []
    should_run, *args = _should_run({'cycle': cycle})
    assert not should_run


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_run(*args):
    with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    impact['cycle'] = cycle
    value = run(impact)
    assert value == expected


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_run_other_sites(*args):
    """
    This test case contains 2 sites:
    One is a crop in france, with value:
    CF_METHOD_factor_france_permanent_crops * ( siteArea_france_crop * time_in_years )
    = 87.631 * ( 1.0082662E-7 * 1 )
    = 8.835537537220001e-06

    And one a forest in italy, with value:
    CF_METHOD_factor_italy_forest * ( siteArea_italy_forest * time_in_years )
    = 43.198 * ( 1.3573373E-9 * 1 )
    = 5.86342566854E-08

    We expect the model to return 8.835537537220001e-06 + 5.86342566854E-08 = 8.894171793905402e-06

    """
    with open(f"{fixtures_folder}/otherSites/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/otherSites/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    impact['cycle'] = cycle
    value = run(impact)
    assert value == expected


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_run_with_subclass_landcover(*args):
    """
    Example data:
    Country: Italy
    Quantity in m^2: 1.3573373E-9
    CF METHOD factor: 4.3198E+01
    "Charact Result [soil quality index]" result also in result.jsonld : 5.86342566854E-08
    siteArea in test file in ha:    1.3573373E-9 / 10 000 = 1.3573373e-13

    landCover field "plantationForest" should map to
    Name Flow: "forest, intensive Land occupation"
    """
    with open(f"{fixtures_folder}/plantationForest/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/plantationForest/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    impact['cycle'] = cycle
    value = run(impact)
    assert value == expected


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_run_with_region_missing_data(*args):
    """
    When given valid sub-region or country not in the lookup file should default to 'region-world'
    """
    with open(f"{fixtures_folder}/default-region-world/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/default-region-world/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    impact['cycle'] = cycle
    value = run(impact)
    assert value == expected


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_run_with_no_region(*args):
    """
    When no location is specified, defaults to region world.
    """
    with open(f"{fixtures_folder}/cycle.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    del cycle['site']['country']

    with open(f"{fixtures_folder}/default-region-world/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    impact['cycle'] = cycle
    value = run(impact)
    assert value == expected
