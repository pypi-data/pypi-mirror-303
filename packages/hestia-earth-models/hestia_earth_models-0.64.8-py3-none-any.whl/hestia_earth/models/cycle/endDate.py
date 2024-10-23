"""
End Date

This model sets the [Cycle endDate](https://hestia.earth/schema/Cycle#endDate) based on:
* if no `cycleDuration` is provided, and the `endDate` is set to month precision (e.g., `2000-01`),
assumed it ended on the 14th of the month.
"""
from hestia_earth.utils.date import is_in_months

from hestia_earth.models.log import logRequirements, logShouldRun
from . import MODEL

REQUIREMENTS = {
    "Cycle": {
        "endDate": "month precision",
        "none": {
            "cycleDuration": ""
        }
    }
}
RETURNS = {
    "The endDate as a string": ""
}
MODEL_KEY = 'endDate'


def _run(cycle: dict):
    endDate = cycle.get('endDate')
    return f"{endDate}-14"


def _should_run(cycle: dict):
    has_endDate = cycle.get('endDate') is not None
    has_month_precision = has_endDate and is_in_months(cycle.get('endDate'))
    no_cycleDuration = cycle.get('cycleDuration') is None

    logRequirements(cycle, model=MODEL, key=MODEL_KEY, by='endDate',
                    has_endDate=has_endDate,
                    has_month_precision=has_month_precision,
                    no_cycleDuration=no_cycleDuration)

    should_run = all([has_endDate, has_month_precision, no_cycleDuration])
    logShouldRun(cycle, MODEL, None, should_run, key=MODEL_KEY, by='endDate')
    return should_run


def run(cycle: dict): return _run(cycle) if _should_run(cycle) else None
