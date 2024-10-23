from hestia_earth.utils.lookup import download_lookup, get_table_value, column_name, extract_grouped_data
from hestia_earth.utils.tools import safe_parse_float

from hestia_earth.models.log import debugMissingLookup
from hestia_earth.models.utils.productivity import PRODUCTIVITY, get_productivity
from .. import MODEL


def productivity_lookup_value(term_id: str, lookup: str, country: dict, animal: dict):
    country_id = country.get('@id')
    productivity_key = get_productivity(country)
    lookup_name = f"{lookup}.csv"
    lookup = download_lookup(lookup_name)
    column = column_name(animal.get('term').get('@id'))
    value = get_table_value(lookup, 'termid', country_id, column)
    debugMissingLookup(lookup_name, 'termid', country_id, column, value, model=MODEL, term=term_id)
    return safe_parse_float(
        extract_grouped_data(value, productivity_key.value) or
        extract_grouped_data(value, PRODUCTIVITY.HIGH.value)  # defaults to high if low is not found
    )
