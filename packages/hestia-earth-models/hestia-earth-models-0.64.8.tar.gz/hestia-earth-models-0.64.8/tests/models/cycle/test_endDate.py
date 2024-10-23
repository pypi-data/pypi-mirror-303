from hestia_earth.models.cycle.endDate import _should_run, run


def test_should_run():
    # no endDate => no run
    cycle = {}
    should_run = _should_run(cycle)
    assert not should_run

    # with endDate with days => no run
    cycle['endDate'] = '2020-01-01'
    should_run = _should_run(cycle)
    assert not should_run

    # with endDate no days => run
    cycle['endDate'] = '2020-01'
    should_run = _should_run(cycle)
    assert should_run is True


def test_run():
    assert run({'endDate': '2020-01'}) == '2020-01-14'
