import json
import pytest
from unittest.mock import patch
from tests.utils import fixtures_path, fake_new_indicator

from hestia_earth.models.frischknechtEtAl2000.ionisingRadiationKbqU235Eq import MODEL, TERM_ID, run, _should_run

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"


@pytest.mark.parametrize(
    'test_name,impact,expected_should_run',
    [
        (
            'no emissionsResourceUse => no run',
            {},
            False
        ),
        (
            'no emissions in the lookups list => no run',
            {
                'emissionsResourceUse': [
                    {
                        'term': {'@id': 'co2ToAirInputsProduction'}
                    }
                ]
            },
            False
        ),
        (
            'with emissions in the lookup list but no waste inputs => no run',
            {
                'emissionsResourceUse': [
                    {
                        'term': {'@id': 'ionisingCompoundsToAirInputsProduction'}
                    }
                ]
            },
            False
        ),
        (
            'with emissions in the lookup list and waste inputs => run',
            {
                'emissionsResourceUse': [
                    {
                        'term': {'@id': 'ionisingCompoundsToAirInputsProduction'},
                        'inputs': [{'termType': 'waste'}]
                    }
                ]
            },
            True
        )
    ]
)
def test_should_run(test_name, impact, expected_should_run):
    should_run, *args = _should_run(impact)
    assert should_run == expected_should_run, test_name


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_run(*args):
    with open(f"{fixtures_folder}/impact-assessment.jsonld", encoding='utf-8') as f:
        impactassessment = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(impactassessment)
    assert value == expected
