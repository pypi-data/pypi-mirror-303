import json
from unittest.mock import patch

from pytest import mark

from hestia_earth.models.environmentalFootprintV3.soilQualityIndexTotalLandUseEffects import MODEL, TERM_ID, run, \
    _should_run
from tests.utils import fixtures_path, fake_new_indicator

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"

transform_indicator = {'term': {'@id': 'soilQualityIndexLandTransformation'}, 'value': 10}
occupation_indicator = {'term': {'@id': 'soilQualityIndexLandOccupation'}, 'value': 10}
missing_value_indicator = {'term': {'@id': 'soilQualityIndexLandOccupation'}}
bad_value_indicator = {'term': {'@id': 'soilQualityIndexLandOccupation'}, 'value': "42"}


@mark.parametrize(
    "emissions_resource_use, expected",
    [
        ([], False),
        ([transform_indicator], False),
        ([transform_indicator, transform_indicator], False),
        ([transform_indicator, missing_value_indicator], False),
        ([transform_indicator, bad_value_indicator], False),
        ([transform_indicator, occupation_indicator], True),
    ],
    ids=["Empty", "missing entry", "duplicate entry", "no value in entry", "bad value in entry", "correct assessment"]
)
def test_should_run(emissions_resource_use, expected):
    with open(f"{fixtures_folder}/impactassessment.jsonld", encoding='utf-8') as f:
        impactassessment = json.load(f)

    impactassessment['emissionsResourceUse'] = emissions_resource_use

    should_run, *args = _should_run(impactassessment)
    assert should_run is expected


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_run(*args):
    with open(f"{fixtures_folder}/impactassessment.jsonld", encoding='utf-8') as f:
        impactassessment = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(impactassessment)
    assert value == expected
