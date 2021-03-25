import courtbot


def test_has_properties():

    court = courtbot.get_state("OK")

    assert court.courts

    case = court.get_case('tulsa-CF-2020-1')

    assert case.events

    state = courtbot.get_state("VT")

    assert state.courts
    assert state.courts[0] == 'addison civil division'

    assert state.supported_locations
    assert state.supported_locations['county'][0] == 'addison'

    court = state.get_court("addison civil division")
    assert court.name == "addison civil division"
    court = state.get_court("Addison civil")
    assert court.name == "addison civil division"

    case_identifier = court.case_identifier
    assert case_identifier["definition"]
    assert case_identifier["example"]
    assert case_identifier["recipe"]

    case = court.get_case("addison_civil_104-8-20")

    assert case.events
