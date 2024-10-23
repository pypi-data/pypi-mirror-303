"""
Characterises [soilQualityIndexTotalLandUseEffects](https://hestia.earth/term/soilQualityIndexTotalLandUseEffects)
based on an updated [LANCA model (De Laurentiis et al. 2019)](
http://publications.jrc.ec.europa.eu/repository/handle/JRC113865) and on the LANCA (Regionalised) Characterisation
Factors version 2.5 (Horn and Meier, 2018).
"""
from hestia_earth.utils.model import find_term_match

from hestia_earth.models.log import logRequirements, logShouldRun
from . import MODEL
from ..utils.indicator import _new_indicator

REQUIREMENTS = {
    "ImpactAssessment": {
        "emissionsResourceUse": [
            {"@type": "Indicator", "value": "", "term.@id": "soilQualityIndexLandOccupation"},
            {"@type": "Indicator", "value": "", "term.@id": "soilQualityIndexLandTransformation"}
        ]
    }
}

RETURNS = {
    "Indicator": {
        "value": "",
        "methodTier": "tier 1",
        "statsDefinition": "modelled"
    }
}
TERM_ID = 'soilQualityIndexTotalLandUseEffects'


def _indicator(value: float):
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    return indicator


def _run(land_occupation_indicator, transformation_indicator):
    value = land_occupation_indicator['value'] + transformation_indicator['value']
    return _indicator(value) if value else None


def _should_run(impactassessment: dict):
    land_occupation_indicator = find_term_match(impactassessment.get('emissionsResourceUse', []),
                                                "soilQualityIndexLandOccupation")
    transformation_indicator = find_term_match(impactassessment.get('emissionsResourceUse', []),
                                               "soilQualityIndexLandTransformation")

    has_valid_values = all([isinstance(land_occupation_indicator.get('value', None), (int, float)),
                            isinstance(transformation_indicator.get('value', None), (int, float))])

    logRequirements(impactassessment, model=MODEL, term=TERM_ID,
                    transformation_indicator=transformation_indicator,
                    land_occupation_indicator=land_occupation_indicator,
                    has_valid_values=has_valid_values
                    )

    should_run = all([transformation_indicator, land_occupation_indicator, has_valid_values])

    logShouldRun(impactassessment, MODEL, TERM_ID, should_run)
    return should_run, land_occupation_indicator, transformation_indicator


def run(impactassessment: dict):
    should_run, land_occupation_indicator, transformation_indicator = _should_run(impactassessment)
    return _run(land_occupation_indicator, transformation_indicator) if should_run else None
