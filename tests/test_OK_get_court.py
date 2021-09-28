import courtbot


def test_has_properties():

    court = courtbot.get_state("OK")

    assert court.courts

    case = court.get_case('tulsa-CF-2020-1')

    assert case.events
