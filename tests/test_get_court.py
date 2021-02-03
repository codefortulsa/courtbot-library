import courtbot


def test_has_properties():

    court = courtbot.get_state("OK")

    assert court.courts

    case = court.get_case('tulsa-CF-2020-1')

    assert case.events

    court = courtbot.get_state("VT")

    assert court.courts

    # TODO: This particular case_id may not always exist...
    case = court.get_case('addison_civil_150-6-19')

    assert case.events
