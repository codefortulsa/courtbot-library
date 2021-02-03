import pandas
import json
import urllib.request as request


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

    @classmethod
    def format_events(cls, case_info):
        events = [
            dict(
                date=Case.build_date(event),
                description=event["hearing_type"]
            )
            for event in case_info
        ]
        return events


class VermontCourtCalendars(object):
    court_calendar_url = "https://raw.githubusercontent.com/codeforbtv/court-calendars/main/event_lookup.csv"

    def __init__(self):
        self._lookup_table = None
        self._courts = None

    @property
    def lookup_table(self):
        if self._lookup_table is None:
            self._lookup_table = VermontCourtCalendars.fetch_lookup_table()
            self._lookup_table["case_id"] = (
                    self._lookup_table.county + "_" + self._lookup_table.division + "_" + self.lookup_table.docket)
        return self._lookup_table

    @property
    def courts(self):
        if self._courts is None:
            self._courts = sorted(
                [county + "_" + division
                 for county in set(self.lookup_table.county)
                 for division in set(self.lookup_table[self.lookup_table.county == county].division)])

        return self._courts

    @classmethod
    def fetch_lookup_table(cls):
        with request.urlopen(cls.court_calendar_url) as response:
            lookup_table = pandas.read_csv(response)

        return lookup_table

    def get_case_url(self, case_id):
        url = self.lookup_table.loc[self.lookup_table.case_id == case_id, "link"][0]
        return url

    def get_case(self, case_id):
        case_url = self.get_case_url(case_id)
        with request.urlopen(case_url) as response:
            case_json = response.read()
        return Case(case_json)


vtcc = VermontCourtCalendars()
courts = vtcc.courts
get_case = vtcc.get_case
