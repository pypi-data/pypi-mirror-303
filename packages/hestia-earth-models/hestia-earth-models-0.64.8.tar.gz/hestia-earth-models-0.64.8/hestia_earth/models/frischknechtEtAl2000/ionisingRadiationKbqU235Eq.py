from functools import reduce
from hestia_earth.schema import TermTermType
from hestia_earth.utils.tools import list_sum, flatten, non_empty_list

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.emission import filter_emission_inputs
from hestia_earth.models.utils.indicator import _new_indicator
from hestia_earth.models.utils.lookup import factor_value
from . import MODEL

REQUIREMENTS = {
    "ImpactAssessment": {
        "emissionsResourceUse": [{
            "@type": "Indicator",
            "value": "",
            "term.@id": [
                "ionisingCompoundsToAirInputsProduction",
                "ionisingCompoundsToWaterInputsProduction",
                "ionisingCompoundsToSaltwaterInputsProduction"
            ],
            "inputs": [{"@type": "Input", "term.termType": "waste"}]
        }]
    }
}
LOOKUPS = {
    "waste": [
        "ionisingCompoundsToAirInputsProduction",
        "ionisingCompoundsToWaterInputsProduction",
        "ionisingCompoundsToSaltwaterInputsProduction"
    ]
}
RETURNS = {
    "Indicator": {
        "value": "",
        "inputs": ""
    }
}

TERM_ID = 'ionisingRadiationKbqU235Eq'


def _indicator(value: float, input: dict):
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    indicator['inputs'] = [input]
    return indicator


def _run(grouped_emissions_inputs: list):
    input = grouped_emissions_inputs[0].get('input')
    values = [
        factor_value(
            model=MODEL,
            term_id=TERM_ID,
            lookup_name=f"{TermTermType.WASTE.value}.csv",
            lookup_col=i.get('emission').get('term', {}).get('@id')
        )(data=i.get('emission') | {'term': i.get('input')})
        for i in grouped_emissions_inputs
    ]
    value = list_sum(values)
    return _indicator(value, input) if value else None


def _should_run(impact_assessment: dict):
    emissions = flatten([
        ([
            {'emission': emission, 'input': input}
            for input in filter_emission_inputs(emission, TermTermType.WASTE)
        ])
        for emission in impact_assessment.get('emissionsResourceUse', [])
        if emission.get('term', {}).get('@id') in LOOKUPS[TermTermType.WASTE.value]
    ])
    emissions_per_input = reduce(
        lambda p, c: p | {c.get('input').get('@id'): p.get(c.get('input').get('@id'), []) + [c]},
        emissions,
        {}
    )

    logRequirements(impact_assessment, model=MODEL,
                    has_emissions=bool(emissions_per_input))

    should_run = all([emissions_per_input])

    logShouldRun(impact_assessment, MODEL, TERM_ID, should_run)
    return should_run, emissions_per_input


def run(impact_assessment: dict):
    should_run, emissions_per_input = _should_run(impact_assessment)
    return non_empty_list(map(_run, emissions_per_input.values())) if should_run else []
