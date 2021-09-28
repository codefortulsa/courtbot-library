
import courtbot

def test_has_properties():

    court = courtbot.get_state("CA")

    assert court.courts

def test_fetch_list():

    court = courtbot.get_state("CA")

    result = court.get_list('2021-09-23')

    assert len(result) == 699

def test_fetch_case():

    court = courtbot.get_state("CA")

    result = court.get_case('2021-09-23', 'C1918672')

    assert result['caseName'] == 'The People of the State of California\nvs.\nPEREZ, JOSE SOLEDAD'

