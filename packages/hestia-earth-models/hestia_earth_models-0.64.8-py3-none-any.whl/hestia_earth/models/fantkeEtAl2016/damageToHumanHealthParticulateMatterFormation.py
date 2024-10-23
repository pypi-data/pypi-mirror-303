from hestia_earth.utils.lookup import column_name

from hestia_earth.models.log import logRequirements, logShouldRun
from . import MODEL
from ..utils.impact_assessment import impact_lookup_value
from ..utils.indicator import _new_indicator

REQUIREMENTS = {
    "ImpactAssessment": {
        "emissionsResourceUse": [
            {
                "@type": "Indicator", "value": "", "term.termType": "emission"
            }
        ]
    }
}

TERM_ID = 'damageToHumanHealthParticulateMatterFormation'

LOOKUPS = {
    "emission": "damageToHumanHealthParticulateMatterFormationFantkeEtAl2016"
}

RETURNS = {
    "Indicator": {
        "value": ""
    }
}

default_group_key = 'default'


def _indicator(value: float):
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    return indicator


def run(impact_assessment: dict):
    value = impact_lookup_value(model=MODEL, term_id=TERM_ID, impact=impact_assessment,
                                lookup_col=column_name(LOOKUPS['emission']),
                                grouped_key=default_group_key)
    logRequirements(impact_assessment, model=MODEL, term=TERM_ID,
                    value=value)

    should_run = all([value is not None])
    logShouldRun(impact_assessment, MODEL, TERM_ID, should_run)

    return _indicator(value) if should_run else None
