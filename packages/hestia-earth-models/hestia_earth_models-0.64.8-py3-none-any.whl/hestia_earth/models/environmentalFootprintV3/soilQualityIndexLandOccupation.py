from hestia_earth.schema import TermTermType
from hestia_earth.utils.lookup import download_lookup
from hestia_earth.utils.tools import list_sum, non_empty_list

from hestia_earth.models.log import logRequirements, logShouldRun, log_as_table
from hestia_earth.models.utils import hectar_to_square_meter, days_to_years
from hestia_earth.models.utils.blank_node import most_relevant_blank_node_by_type
from hestia_earth.models.utils.indicator import _new_indicator
from hestia_earth.models.utils.landCover import get_pef_grouping
from hestia_earth.models.utils.lookup import fallback_country
from . import MODEL
from .utils import get_coefficient_factor

REQUIREMENTS = {
    "ImpactAssessment": {
        "cycle": {
            "@type": "Cycle",
            "siteDuration": "> 0",
            "siteArea": "> 0",
            "site": {
                "siteType": "",
                "@type": "Site",
                "management": [{"@type": "Management", "value": "", "term.termType": "landCover"}],
                "country": {"@type": "Term", "termType": "region"}
            },
            "optional": {
                "otherSitesDuration": "> 0",
                "otherSitesArea": "> 0",
                "otherSites": [{
                    "@type": "Site",
                    "siteType": "",
                    "management": [{"@type": "Management", "value": "", "term.termType": "landCover"}],
                    "country": {"@type": "Term", "termType": "region"}
                }]
            }
        }
    }
}
LOOKUPS = {
    "@doc": "Performs lookup on landCover.csv for column headers and region-pefTermGrouping-landOccupation.csv for CFs",
    "region-pefTermGrouping-landOccupation": "",
    "landCover": "pefTermGrouping"
}

RETURNS = {
    "Indicator": {
        "value": ""
    }
}
TERM_ID = 'soilQualityIndexLandOccupation'
LOOKUP = f"{list(LOOKUPS.keys())[1]}.csv"


def _indicator(value: float):
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    return indicator


def _run(sites: list):
    values = [site['coeff'] * hectar_to_square_meter(site['area']) * days_to_years(site['duration']) for site in sites]
    return _indicator(list_sum(values)) if values else None


def _should_run(impact_assessment: dict):
    cycle = impact_assessment.get('cycle', {})
    end_date = cycle.get('endDate')

    has_site = bool(cycle.get('site', False))
    has_other_sites = bool(cycle.get('otherSites', []))

    all_sites = non_empty_list([cycle.get('site')] + cycle.get('otherSites', []))
    site_areas = [cycle.get('siteArea')] + cycle.get('otherSitesArea', [])
    site_durations = [cycle.get('siteDuration')] + cycle.get('otherSitesDuration', [])

    sites = [
        {
            'site-type': site.get('siteType'),
            'country-id': site.get('country', {}).get('@id'),
            'area': site_areas[index] if len(site_areas) >= index + 1 else None,
            'duration': site_durations[index] if len(site_durations) >= index + 1 else None,
            'landCover-id': (most_relevant_blank_node_by_type(
                site.get("management", []),
                term_type=TermTermType.LANDCOVER.value,
                date=end_date
            ) or {}).get('term', {}).get('@id'),
        }
        for index, site in enumerate(all_sites)
    ]

    sites = [
        site for site in sites
        if all([
            (site.get('area') or 0) > 0,
            (site.get('duration') or 0) > 0,
            site.get('landCover-id')
        ])
    ]

    sites = [
        site |
        {
            'coeff': get_coefficient_factor(
                LOOKUP,
                fallback_country(site.get('country-id'), [download_lookup(LOOKUP)]),
                get_pef_grouping(site.get('landCover-id')),
                term_id=TERM_ID
            )
        } for site in sites
    ]
    valid_sites = [site for site in sites if site.get('coeff') is not None]

    has_valid_sites = bool(valid_sites)

    logRequirements(cycle, model=MODEL, term=TERM_ID,
                    has_valid_sites=has_valid_sites,
                    has_site=has_site,
                    has_other_sites=has_other_sites,
                    valid_sites=log_as_table(valid_sites),
                    )

    should_run = all([has_valid_sites])
    logShouldRun(cycle, MODEL, TERM_ID, should_run)
    return should_run, valid_sites


def run(impact_assessment: dict):
    should_run, sites = _should_run(impact_assessment)
    return _run(sites) if should_run else None
