"""
Management node

This model provides data gap-filled data from cycles in the form of a list of management nodes
(https://www.hestia.earth/schema/Management).

It includes products of type crop, forage, landCover (gap-filled with a value of 100) and practices of type waterRegime,
tillage, cropResidueManagement and landUseManagement.

All values are copied from the source node, except for crop and forage terms in which case the dates are copied from the
cycle.

When nodes are chronologically consecutive with "% area" or "boolean" units and the same term and value, they are
condensed into a single node to aid readability.
"""
from functools import reduce

from hestia_earth.schema import SchemaType, TermTermType, SiteSiteType
from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.model import filter_list_term_type, linked_node
from hestia_earth.utils.tools import safe_parse_float, flatten, non_empty_list
from hestia_earth.utils.blank_node import get_node_value

from hestia_earth.models.log import logRequirements, logShouldRun, log_blank_nodes_id
from hestia_earth.models.utils.term import get_lookup_value
from hestia_earth.models.utils.blank_node import condense_nodes
from hestia_earth.models.utils.site import related_cycles
from hestia_earth.models.utils.site import get_land_cover_term_id as get_landCover_term_id_from_site_type
from . import MODEL

REQUIREMENTS = {
    "Site": {
        "related": {
            "Cycle": [{
                "@type": "Cycle",
                "startDate": "",
                "endDate": "",
                "products": [
                    {
                        "@type": "Product",
                        "term.termType": ["crop", "forage", "landCover"],
                        "units": ["% area", "boolean"]
                    }
                ],
                "practices": [
                    {
                        "term.termType": [
                            "waterRegime",
                            "tillage",
                            "cropResidueManagement",
                            "landUseManagement",
                            "system"
                        ],
                        "units": ["% area", "boolean"],
                        "value": ""
                    }
                ],
                "inputs": [
                    {
                        "@type": "Input",
                        "term.termType": [
                            "inorganicFertiliser",
                            "organicFertiliser",
                            "soilAmendment"
                        ]
                    }
                ]
            }]
        }
    }
}
RETURNS = {
    "Management": [{
        "@type": "Management",
        "term.termType": [
            "landCover", "waterRegime", "tillage", "cropResidueManagement", "landUseManagement", "system"
        ],
        "value": "",
        "endDate": "",
        "startDate": ""
    }]
}
LOOKUPS = {
    "crop": ["landCoverTermId"],
    "forage": ["landCoverTermId"],
    "inorganicFertiliser": "nitrogenContent",
    "organicFertiliser": "ANIMAL_MANURE",
    "soilAmendment": "PRACTICE_INCREASING_C_INPUT",
    "landUseManagement": "GAP_FILL_TO_MANAGEMENT"
}
MODEL_KEY = 'management'
LAND_COVER_KEY = LOOKUPS['crop'][0]
ANIMAL_MANURE_USED_TERM_ID = "animalManureUsed"
INORGANIC_NITROGEN_FERTILISER_USED_TERM_ID = "inorganicNitrogenFertiliserUsed"
ORGANIC_FERTILISER_USED_TERM_ID = "organicFertiliserUsed"
AMENDMENT_INCREASING_C_USED_TERM_ID = "amendmentIncreasingSoilCarbonUsed"
INPUT_RULES = {
    TermTermType.INORGANICFERTILISER.value: (
        (
            TermTermType.INORGANICFERTILISER.value,  # Lookup column
            lambda x: safe_parse_float(x) > 0,  # Condition
            INORGANIC_NITROGEN_FERTILISER_USED_TERM_ID  # New term.
        ),
    ),
    TermTermType.SOILAMENDMENT.value: (
        (
            TermTermType.SOILAMENDMENT.value,
            lambda x: x is True,
            AMENDMENT_INCREASING_C_USED_TERM_ID
        ),
    ),
    TermTermType.ORGANICFERTILISER.value: (
        (
            TermTermType.SOILAMENDMENT.value,
            lambda x: x is True,
            ORGANIC_FERTILISER_USED_TERM_ID
        ),
        (
            TermTermType.ORGANICFERTILISER.value,
            lambda x: x is True,
            ANIMAL_MANURE_USED_TERM_ID
        )
    )
}
_SKIP_LAND_COVER_SITE_TYPES = [
    SiteSiteType.CROPLAND.value
]


def management(data: dict):
    node = {'@type': SchemaType.MANAGEMENT.value}
    return node | data


def _extract_node_value(node: dict) -> dict:
    return node | {'value': get_node_value(node)}


def _include(value: dict, keys: list) -> dict: return {k: v for k, v in value.items() if k in keys}


def _default_dates(cycle: dict, values: list):
    return [(_include(cycle, ["startDate", "endDate"]) | v) for v in values]


def _dates_from_current_cycle(cycle: dict, values: list) -> list:
    """Always uses the dates from the cycle."""
    return [v | _include(cycle, ["startDate", "endDate"]) for v in values]


def _copy_item_if_exists(source: dict, keys: list[str] = None, dest: dict = None) -> dict:
    keys = keys or []
    dest = dest or {}
    return reduce(lambda p, c: p | ({c: source[c]} if c in source else {}), keys, dest)


def _get_landCover_term_id(product: dict) -> str:
    value = get_lookup_value(product.get('term', {}), LAND_COVER_KEY, model=MODEL, model_key=LAND_COVER_KEY)
    return value.split(';')[0] if value else None


def _get_relevant_items(
    cycles: list[dict], item_name: str, relevant_terms: list, date_fill: callable = _default_dates
):
    """
    Get items from the list of cycles with any of the relevant terms.
    Also adds dates if missing.
    """
    return [
        [
            item
            for item in date_fill(cycle=cycle, values=filter_list_term_type(cycle.get(item_name, []), relevant_terms))
        ]
        for cycle in cycles
    ]


def _get_lookup_with_debug(term: dict, column: str) -> any:
    get_lookup_value(term, column, model_key=MODEL_KEY, land_cover_key=LAND_COVER_KEY)


def _data_from_input(cycle: dict, term_id: str) -> dict:
    return {
        "term": {
            "@type": "Term",
            "@id": term_id,
            "termType": "landUseManagement"
        },
        "value": True,
        "startDate": cycle["startDate"],
        "endDate": cycle["endDate"]
    }


def _process_rule(cycle, term, term_type) -> list:
    relevant_terms = []
    for column, condition, new_term in INPUT_RULES[term_type]:
        lookup_result = _get_lookup_with_debug(term, LOOKUPS[column])

        if condition(lookup_result):
            relevant_terms.append(_data_from_input(cycle=cycle, term_id=new_term))

    return relevant_terms


def _get_relevant_inputs(cycles: list[dict]) -> list:
    relevant_inputs = []
    for cycle in [c for c in cycles if "inputs" in c]:
        for i in cycle["inputs"]:
            if i.get("term", {}).get("termType", "") in INPUT_RULES:
                relevant_inputs.extend(
                    _process_rule(
                        cycle=cycle,
                        term=i.get("term", {}),
                        term_type=i.get("term", {}).get("termType", "")
                    )
                )

    return relevant_inputs


def _has_gap_fill_to_management_set(practices: list) -> list:
    """
    Include only landUseManagement practices where GAP_FILL_TO_MANAGEMENT = True
    """
    result = [
        p for p in practices
        if p.get("term", {}).get("termType", {}) != TermTermType.LANDUSEMANAGEMENT.value
        or get_lookup_value(lookup_term=p.get("term", {}), column=LOOKUPS["landUseManagement"])
    ]
    return result


def _should_run_all_products(cycles: list, site_type: str):
    products_land_cover = flatten(_get_relevant_items(
        cycles=cycles,
        item_name="products",
        relevant_terms=[TermTermType.LANDCOVER]
    )) if site_type else []
    products_land_cover = [
        _extract_node_value(
            _include(
                value=product,
                keys=["term", "value", "startDate", "endDate", "properties"]
            )
        ) for product in products_land_cover
    ]

    products_crop_forage = _get_relevant_items(
        cycles=cycles,
        item_name="products",
        relevant_terms=[TermTermType.CROP, TermTermType.FORAGE],
        date_fill=_dates_from_current_cycle
    )
    products_crop_forage = [
        _copy_item_if_exists(
            source=product,
            keys=["startDate", "endDate", "properties"],
            dest={
                "term": linked_node(download_hestia(_get_landCover_term_id(product))),
                "value": round(100 / len(_products), 2)
            }
        )
        for _products in products_crop_forage
        for product in list(filter(_get_landCover_term_id, _products))
    ] if site_type else []
    dates = sorted(list(set(
        non_empty_list(flatten([[cycle.get('startDate'), cycle.get('endDate')] for cycle in cycles]))
    ))) if site_type not in _SKIP_LAND_COVER_SITE_TYPES else []
    site_type_id = get_landCover_term_id_from_site_type(site_type) if site_type else None
    site_type_term = download_hestia(site_type_id) if all([len(dates) >= 2, site_type_id]) else None
    products_site_type = [{
        "term": linked_node(site_type_term),
        "value": 100,
        "startDate": dates[0],
        "endDate": dates[-1]
    }] if site_type_term else []

    return products_site_type, products_crop_forage, products_land_cover


def _should_run(site: dict):
    cycles = related_cycles(site)

    products_animal, products_crop_forage, products_land_cover = _should_run_all_products(
        cycles=cycles,
        site_type=site.get("siteType")
    )
    all_products = products_land_cover + products_crop_forage + products_animal
    all_products = condense_nodes(all_products)

    practices = [
        _extract_node_value(
            _include(
                value=practice,
                keys=["term", "value", "startDate", "endDate"]
            )
        ) for practice in flatten(_get_relevant_items(
            cycles=cycles,
            item_name="practices",
            relevant_terms=[
                TermTermType.WATERREGIME,
                TermTermType.TILLAGE,
                TermTermType.CROPRESIDUEMANAGEMENT,
                TermTermType.LANDUSEMANAGEMENT,
                TermTermType.SYSTEM
            ]
        ))
    ]
    practices = _has_gap_fill_to_management_set(practices)
    practices = condense_nodes(practices)

    relevant_inputs = _get_relevant_inputs(cycles)
    logRequirements(
        site,
        model=MODEL,
        term=None,
        model_key=MODEL_KEY,
        products_crop_forage_ids=log_blank_nodes_id(products_crop_forage),
        products_land_cover_ids=log_blank_nodes_id(products_land_cover),
        products_animal=log_blank_nodes_id(products_animal),
        practice_ids=log_blank_nodes_id(practices),
        inputs=log_blank_nodes_id(relevant_inputs)
    )
    should_run = any(all_products + practices + relevant_inputs)
    logShouldRun(site, MODEL, None, should_run=should_run, model_key=MODEL_KEY)
    return should_run, all_products, practices, relevant_inputs


def run(site: dict):
    should_run, products, practices, inputs = _should_run(site)
    return list(map(management, products + practices + inputs)) if should_run else []
