import json
import re
from bs4 import BeautifulSoup
from urllib import request as request


class Case(object):

    def __init__(self, case_json):
        self._case_info = json.loads(case_json)
        self._events = self.format_events(self._case_info)

    @property
    def events(self):
        return self._events

    @staticmethod
    def build_date(event):
        # TODO: Add year
        date = (
            event["day_of_week"] +
            ", " +
            event["month"] +
            " " +
            event["day"] +
            ", at " +
            event["time"] +
            " " +
            event["am_pm"]
        )
        return date

    @staticmethod
    def format_events(case_info):
        events = [
            dict(
                date=Case.build_date(event),
                description=event["hearing_type"]
            )
            for event in case_info
        ]
        return events


class Court(object):

    def __init__(self, name, location, case_identifier):
        self.name = name
        self.location = location
        self.case_identifier = case_identifier

    @staticmethod
    def get_case(case_id):
        return VermontCourtCalendars.get_case(case_id)


class VermontCourtCalendars(object):
    court_calendar_url = "https://github.com/codeforbtv/court-calendars"
    case_identifier = dict(
        definition=[
            "county",
            "division",
            "docket"
        ],
        example="addison_civil_104-8-20",
        recipe="{county}_{division}_{docket}"
    )

    def __init__(self):
        self._court_info = None
        self._courts = None
        self._supported_locations = None

    @property
    def court_info(self):
        if self._court_info is None:
            all_courts = []
            with request.urlopen(VermontCourtCalendars.court_calendar_url) as response:
                soup = BeautifulSoup(response, features="html.parser")
                for link in soup.findAll('a'):
                    if re.match(r"/codeforbtv/court-calendars/tree/main/", link.get('href')):
                        county_div = link.get('href').split("/")[-1]
                        county = county_div.split("_")[0]
                        div = county_div.split("_")[1]
                        all_courts.append(
                            dict(
                                county=county,
                                division=div,
                                name=county + " " + div + " division"
                            )
                        )
            self._court_info = all_courts
        return self._court_info

    @property
    def supported_locations(self):
        if self._supported_locations is None:
            self._supported_locations = dict()
            location_regex = r"(county)"
            for key in set(loc_key for court in self.court_info for loc_key in list(court.keys())):
                if re.match(location_regex, str(key)):
                    self._supported_locations[key] = sorted(list(set([court.get(key) for court in self.court_info])))
        return self._supported_locations

    @property
    def courts(self):
        if self._courts is None:
            self._courts = sorted(
                [court.get("name") for court in self.court_info]
            )
        return self._courts

    @staticmethod
    def get_case_url(case_id):
        url_stub = "https://raw.githubusercontent.com/codeforbtv/court-calendars/main"
        docket = case_id.split("_")[-1]
        county_div = case_id.split(docket)[0][0:-1]
        case_url = "/".join([url_stub, county_div, docket + ".json"])
        return case_url

    @staticmethod
    def get_case(case_id):
        case_url = VermontCourtCalendars.get_case_url(case_id)
        with request.urlopen(case_url) as response:
            case_json = response.read()
        return Case(case_json)

    def get_court(self, court_name):
        court_name = court_name.lower().strip()
        court_info = None
        for ci in self.court_info:
            if ci.get('name') == court_name or ci.get('name')[0:-9] == court_name:
                court_info = ci
                break

        if court_info is None:
            raise KeyError(court_name + " not found.")
        else:
            return Court(
                court_info.get('name'),
                dict(county=court_info.get('county')),
                VermontCourtCalendars.case_identifier
            )


vtcc = VermontCourtCalendars()
courts = vtcc.courts
supported_locations = vtcc.supported_locations
get_court = vtcc.get_court
