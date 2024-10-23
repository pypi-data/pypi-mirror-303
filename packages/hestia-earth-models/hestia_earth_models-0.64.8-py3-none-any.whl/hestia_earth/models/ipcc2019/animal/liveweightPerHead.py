from hestia_earth.schema import TermTermType
from hestia_earth.utils.model import filter_list_term_type

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.blank_node import merge_blank_nodes
from hestia_earth.models.utils.property import _new_property, node_has_no_property
from .utils import productivity_lookup_value
from .. import MODEL

REQUIREMENTS = {
    "Cycle": {
        "site": {
            "@type": "Site",
            "country": {"@type": "Term", "termType": "region"}
        },
        "animals": [{
            "@type": "Animal",
            "term.termType": "liveAnimal",
            "none": {
                "properties": [{
                    "@type": "Property",
                    "value": "",
                    "term.@id": "liveweightPerHead"
                }]
            }
        }]
    }
}
LOOKUPS = {
    "region-liveAnimal-liveweightPerHead": "liveweight per head"
}
RETURNS = {
    "Animal": [{
        "properties": [{
            "@type": "Property",
            "value": ""
        }]
    }]
}
TERM_ID = 'liveweightPerHead'


def _property(value: float):
    prop = _new_property(TERM_ID, MODEL)
    prop['value'] = value
    return prop


def _run_animal(data: dict):
    animal = data.get('animal')
    value = data.get('value')
    return animal | {
        'properties': merge_blank_nodes(animal.get('properties', []), [_property(value)])
    }


def _should_run(cycle: dict):
    country = cycle.get('site', {}).get('country', {})
    country_id = country.get('@id')
    live_animals = filter_list_term_type(cycle.get('animals', []), TermTermType.LIVEANIMAL)
    live_animals = list(filter(node_has_no_property(TERM_ID), live_animals))
    live_animals_with_value = [{
        'animal': animal,
        'value': productivity_lookup_value(TERM_ID, list(LOOKUPS.keys())[0], country, animal)
    } for animal in live_animals]

    def _should_run_animal(value: dict):
        animal = value.get('animal')
        lookup_value = value.get('value')
        term_id = animal.get('term').get('@id')

        logRequirements(cycle, model=MODEL, term=term_id, property=TERM_ID,
                        country_id=country_id,
                        liveweightPerHead=lookup_value)

        should_run = all([
            country_id,
            lookup_value is not None
        ])
        logShouldRun(cycle, MODEL, term_id, should_run, property=TERM_ID)

        return should_run

    return list(filter(_should_run_animal, live_animals_with_value))


def run(cycle: dict):
    animals = _should_run(cycle)
    return list(map(_run_animal, animals))
