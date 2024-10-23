"""
Characterises [soilQualityIndexLandTransformation](https://hestia.earth/term/soilQualityIndexLandTransformation)
based on an updated [LANCA model (De Laurentiis et al. 2019)](
http://publications.jrc.ec.europa.eu/repository/handle/JRC113865) and on the LANCA (Regionalised) Characterisation
Factors version 2.5 (Horn and Meier, 2018).
"""
from typing import List

from hestia_earth.schema import TermTermType
from hestia_earth.utils.lookup import download_lookup
from hestia_earth.utils.model import filter_list_term_type
from hestia_earth.utils.tools import list_sum, safe_parse_date, non_empty_list

from hestia_earth.models.log import logRequirements, logShouldRun, log_as_table
from hestia_earth.models.utils import hectar_to_square_meter
from hestia_earth.models.utils import pairwise
from . import MODEL
from .utils import get_coefficient_factor
from ..utils.indicator import _new_indicator
from ..utils.landCover import get_pef_grouping
from ..utils.lookup import fallback_country

REQUIREMENTS = {
    "ImpactAssessment": {
        "cycle": {
            "@type": "Cycle",
            "site": {
                "area": "> 0",
                "@type": "Site",
                "management": [{"@type": "Management", "term.termType": "landCover"}],
                "optional": {"country": {"@type": "Term", "termType": "region"}}
            },
            "optional": {
                "otherSitesArea": "> 0",
                "otherSites": [{
                    "@type": "Site",
                    "management": [{"@type": "Management", "term.termType": "landCover"}],
                    "optional": {"country": {"@type": "Term", "termType": "region"}}
                }]
            }
        }
    }
}

LOOKUPS = {
    "@doc": "Uses `landCover.csv` for column headers and region-pefTermGrouping-landTransformation-X.csv for to/from CFs. (CFs in `region-pefTermGrouping-landTransformation-from.csv` appear to be the opposite values as those in `region-pefTermGrouping-landTransformation-to.csv` but can be different in some cases)",  # noqa: E501
    "region-pefTermGrouping-landTransformation-from": "",
    "region-pefTermGrouping-landTransformation-to": "",
    "landCover": "pefTermGrouping"
}

from_lookup_file = f"{list(LOOKUPS.keys())[1]}.csv"
to_lookup_file = f"{list(LOOKUPS.keys())[2]}.csv"

RETURNS = {
    "Indicator": {
        "value": ""
    }
}

TERM_ID = 'soilQualityIndexLandTransformation'


def _indicator(value: float):
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    return indicator


def _run(sites: List[dict]):
    result = []
    for site in sites:
        values = [(transformation_from_factor + transformation_to_factor) * hectar_to_square_meter(site['area'])
                  for transformation_from_factor, transformation_to_factor in site['transformation_factors']]
        result.append(list_sum(values))
    return _indicator(list_sum(result)) if result else None


def _should_run(impact_assessment: dict):
    cycle = impact_assessment.get('cycle', {})

    has_site = bool(cycle.get('site', {}))
    site_area = cycle.get('site', {}).get("area", False)
    has_area = site_area > 0

    has_other_sites = bool(cycle.get('otherSites', []))

    all_sites = non_empty_list([cycle.get('site')] + cycle.get('otherSites', []))
    site_areas = [cycle.get('site', {}).get('area')] + cycle.get('otherSitesArea', [])

    sites = [
        {
            'site_id': site.get('@id', site.get('id')),
            'transformation_pairs': list(pairwise(
                sorted(filter_list_term_type(site.get("management", []), TermTermType.LANDCOVER.value),
                       key=lambda d: safe_parse_date(d['endDate'])))),
            'country_id_str': site.get('country', {}).get('@id', ''),
            'area': site_areas[index] if len(site_areas) >= index + 1 else None,
        }
        for index, site in enumerate(all_sites)
    ]

    sites = [
        site for site in sites
        if all([
            (site.get('area') or 0) > 0,
            site.get('transformation_pairs', [])
        ])
    ]

    sites = [
        site |
        {
            'column_names': [(get_pef_grouping(from_transformation['term']['@id']),
                              get_pef_grouping(to_transformation['term']['@id']))
                             for from_transformation, to_transformation in site['transformation_pairs']],
        } for site in sites
    ]

    has_lookup_column = lambda s: s['column_names'] and all([all(pair) for pair in s['column_names']])  # noqa: E731
    valid_sites = [site for site in sites if has_lookup_column(site)]

    has_valid_sites = bool(valid_sites)

    valid_sites = [
        site |
        {
            'country_id': fallback_country(site['country_id_str'],
                                           [download_lookup(from_lookup_file), download_lookup(to_lookup_file)]
                                           )
        } for site in valid_sites
    ]

    valid_sites = [
        site |
        {
            'transformation_factors': [(get_coefficient_factor(lookup_name=from_lookup_file,
                                                               country_id=site['country_id'], term_id=TERM_ID,
                                                               occupation_type=from_transformation_header),
                                        get_coefficient_factor(lookup_name=to_lookup_file,
                                                               country_id=site['country_id'], term_id=TERM_ID,
                                                               occupation_type=to_transformation_header))
                                       for from_transformation_header, to_transformation_header in site['column_names']]
        } for site in valid_sites
    ]

    log_equivalent_eu_pef_land_use_names = [
        [{
            'site-id': site['site_id'],
            'hestia-term': hestia_term,
            'corine-term': corine_term,
        } for hestia_term, corine_term in site['column_names']
        ] for site in valid_sites]

    log_transformation_factors = [
        [{
            'site-id': site['site_id'],
            'country-id-used-for-factors': site['country_id'],
            'country-id-in-input': site['country_id_str'],
            'factor-from': from_transformation_header,
            'factor-to': to_transformation_header,
        } for from_transformation_header, to_transformation_header in site['transformation_factors']
        ] for site in valid_sites]

    logRequirements(impact_assessment, model=MODEL, term=TERM_ID,
                    has_site=has_site,
                    has_area=has_area,
                    has_other_sites=has_other_sites,
                    has_valid_sites=has_valid_sites,
                    equivalent_EU_PEF_landUse_names=log_as_table(log_equivalent_eu_pef_land_use_names),
                    transformation_factors=log_as_table(log_transformation_factors)
                    )
    should_run = has_valid_sites

    logShouldRun(impact_assessment, MODEL, TERM_ID, should_run)

    return should_run, valid_sites


def run(impact_assessment: dict):
    should_run, sites = _should_run(impact_assessment)
    return _run(sites) if should_run else None
