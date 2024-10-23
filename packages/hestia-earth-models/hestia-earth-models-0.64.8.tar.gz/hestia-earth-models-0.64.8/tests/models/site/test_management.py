import json
from unittest.mock import patch

import pytest
from hestia_earth.schema import TermTermType, SiteSiteType

from hestia_earth.models.site.management import MODEL, MODEL_KEY, run, _should_run
from tests.utils import fixtures_path

CLASS_PATH = f"hestia_earth.models.{MODEL}.{MODEL_KEY}"
fixtures_folder = f"{fixtures_path}/{MODEL}/{MODEL_KEY}"

TERM_BY_ID = {
    'genericCropPlant': {'@type': 'Term', '@id': 'genericCropPlant', 'termType': TermTermType.LANDCOVER.value},
    'wheatPlant': {'@type': 'Term', '@id': 'wheatPlant', 'termType': TermTermType.LANDCOVER.value},
    'oatPlant': {'@type': 'Term', '@id': 'oatPlant', 'termType': TermTermType.LANDCOVER.value},
    'agatiTree': {'@type': 'Term', '@id': 'agatiTree', 'termType': TermTermType.LANDCOVER.value},
    'wildGarlicPlant': {'@type': 'Term', '@id': 'wildGarlicPlant', 'termType': TermTermType.LANDCOVER.value},
    'animalHousing': {
        "@type": "Term",
        "@id": "animalHousing",
        "name": "Animal housing",
        "termType": TermTermType.LANDCOVER.value,
        "units": "% area"
    }
}

LAND_COVER_TERM_BY_SITE_TYPE = {
    SiteSiteType.ANIMAL_HOUSING.value: "animalHousing",
    SiteSiteType.CROPLAND.value: "cropland"
}


def lookup_side_effect(*args, **kwargs):
    # Values taken from real lookups.
    _ = kwargs
    if args[0]["@id"] == "ureaKgN" and args[1] == "nitrogenContent":
        return 45.5
    if args[0]["@id"] == "compostKgMass" and args[1] == "ANIMAL_MANURE":
        return False
    return True


@patch(f"{CLASS_PATH}.download_hestia", side_effect=lambda id, *args: TERM_BY_ID[id])
@patch(f"{CLASS_PATH}.related_cycles")
def test_should_run(mock_related_cycles, *args):
    # no cycles => do not run
    mock_related_cycles.return_value = []
    should_run, *args = _should_run({})
    assert should_run is False

    # no products => do not run
    mock_related_cycles.return_value = [{"products": []}]
    should_run, *args = _should_run({})
    assert should_run is False

    # with irrelevant termType => do not run
    mock_related_cycles.return_value = [
        {
            "products": [
                {"term": {"termType": TermTermType.BUILDING.value}},
                {"term": {"termType": TermTermType.EXCRETA.value}}
            ],
            "startDate": "2021",
            "endDate": "2022"
        }
    ]
    should_run, *args = _should_run({})
    assert should_run is False

    # products and practices but no relevant terms/termTypes => do not run
    mock_related_cycles.return_value = [
        {
            "practices": [
                {"term": {"@id": "soilAssociationOrganicStandard"}},
                {"term": {"@id": "noTillage"}}
            ],
            "products": [
                {"term": {"termType": TermTermType.BUILDING.value}},
                {"term": {"termType": TermTermType.EXCRETA.value}}
            ]
        }
    ]
    should_run, *args = _should_run({})
    assert should_run is False

    # # practices with relevant termType => run
    mock_related_cycles.return_value = [
        {
            "practices": [
                {"term": {"termType": TermTermType.WATERREGIME.value}},
                {"term": {"termType": TermTermType.MACHINERY.value}}
            ],
            "startDate": "2021",
            "endDate": "2022"
        }
    ]
    should_run, *args = _should_run({})
    assert should_run is True

    # with relevant product, blank site_type => no run
    mock_related_cycles.return_value = [
        {
            "products": [
                {
                    "term": {
                        "termType": TermTermType.CROP.value,
                        "@id": "genericCropProduct"
                    },
                    "value": [51],
                    "startDate": "2001",
                    "endDate": "2002"
                }
            ],
            "startDate": "2021",
            "endDate": "2022"
        }
    ]
    should_run, *args = _should_run({})
    assert should_run is False

    # with relevant product and site_type => run
    mock_related_cycles.return_value = [
        {
            "products": [
                {
                    "term": {
                        "termType": TermTermType.CROP.value,
                        "@id": "genericCropProduct"
                    },
                    "value": [51],
                    "startDate": "2001",
                    "endDate": "2002"
                }
            ],
            "startDate": "2021",
            "endDate": "2022"
        }
    ]
    should_run, *args = _should_run({"siteType": "cropland"})
    assert should_run is True
    assert args[0] == [{
        'term': TERM_BY_ID['genericCropPlant'],
        'value': 100,
        'endDate': '2022',
        'startDate': '2021'
    }]


@pytest.mark.parametrize(
    "test_name,fixture_path",
    [
        ("Products and practices", f"{fixtures_folder}"),
        ("Example 1", f"{fixtures_folder}/inputs/example1"),
        ("Example 2", f"{fixtures_folder}/inputs/example2"),
        ("Example 3", f"{fixtures_folder}/inputs/example3"),
        ("Example 4", f"{fixtures_folder}/inputs/example4"),
        ("Condense Nodes", f"{fixtures_folder}/inputs/condense_nodes"),
        # Expected:
        #   - appleTree (81) x 3 condenses 2020-03-01 to 2021-02-15
        #   - animalManureUsed (true) x 2 condenses 2001-04-01 to 2001-12-31
        #   - treeNutTree, lebbekTree (82) does not condense [different terms]
        #   - organicFertiliserUsed (true|false) does not condense [different values]
        #   - glassOrHighAccessibleCover (83) does not condense [different date ranges (overlapping)]
        #   - durianTree (84) does not condense [different date ranges (disjoint)]
        #   - irrigatedSurfaceIrrigationContinuouslyFlooded (85) does not condense ["%" units]
        #   - sassafrasTree (86) x 2 condenses 2001-01-01 to 2004-12-31
        #   - bananaPlant (87) does not condense [non-consecutive years]
        #   - durianTree (89) does not condense [dates overwritten See 808]
        ("Site Type", f"{fixtures_folder}/inputs/site_type")
    ]
)
@patch(
    f"{CLASS_PATH}.get_landCover_term_id_from_site_type",
    side_effect=lambda site_type: LAND_COVER_TERM_BY_SITE_TYPE[site_type]
)
@patch(f"{CLASS_PATH}.download_hestia", side_effect=lambda term_id, *args: TERM_BY_ID[term_id])
@patch(f"{CLASS_PATH}.related_cycles")
@patch(f"{CLASS_PATH}._get_lookup_with_debug", side_effect=lookup_side_effect)
def test_run(
        mock_get_lookup_with_debug,
        mock_related_cycles,
        mock_download,
        mock_land_cover_lookup,
        test_name,
        fixture_path
):
    with open(f"{fixture_path}/cycles.jsonld", encoding='utf-8') as f:
        cycles = json.load(f)
    mock_related_cycles.return_value = cycles

    try:
        with open(f"{fixture_path}/site.jsonld", encoding='utf-8') as f:
            site = json.load(f)
    except FileNotFoundError:
        with open(f"{fixtures_folder}/site.jsonld", encoding='utf-8') as f:
            site = json.load(f)

    with open(f"{fixture_path}/result.jsonld", encoding='utf-8') as f:
        expected = json.load(f)

    result = run(site)
    assert result == expected
