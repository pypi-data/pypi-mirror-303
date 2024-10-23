import json
from unittest.mock import patch

from hestia_earth.models.poschEtAl2008.terrestrialAcidificationPotentialAccumulatedExceedance import MODEL, TERM_ID, run
from tests.utils import fixtures_path, fake_new_indicator

class_path = f"hestia_earth.models.{MODEL}.{TERM_ID}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{TERM_ID}"


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_run(*args):
    with open(f"{fixtures_folder}/impact-assessment.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)

    with open(f"{fixtures_folder}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    value = run(cycle)
    assert value == expected


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_lookup_to_bad_country(*args):
    with open(f"{fixtures_folder}/impact-assessment.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)
    cycle['country']['@id'] = "example-land-not-real"

    value = run(cycle)
    assert value['value'] is None


@patch(f"{class_path}._new_indicator", side_effect=fake_new_indicator)
def test_lookup_no_term_type(*args):
    """
    We currently do not filter out bad termTypes so this is expected behavior.
    """
    with open(f"{fixtures_folder}/impact-assessment.jsonld", encoding='utf-8') as f:
        cycle = json.load(f)
    del cycle['emissionsResourceUse'][0]['term']['termType']
    del cycle['emissionsResourceUse'][1]['term']['termType']
    cycle['emissionsResourceUse'][2]['term']['termType'] = "wrong-type"

    value = run(cycle)
    assert value['value'] == 0.085
