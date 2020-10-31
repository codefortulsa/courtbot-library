import courtbot


def test_body_text():

    court = courtbot.get_state("OK")

    assert court.courts

    case = court.Case('tulsa-CF-2020-1')

    assert case.events
