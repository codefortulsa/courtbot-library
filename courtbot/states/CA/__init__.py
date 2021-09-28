
import requests

"""A package for retreiving court calendar data from Santa Clara County, California"""

counties = [ 'santa clara' ]

courts = [ 'santa clara' ]

court_names = ["Civil",
               "Probate",
               "Family",
               "Juvenile",
               "Criminalhoj",
               "CriminalPaloAlto",
               "CriminalSouthCounty"]

class Court:

    def __init__(self, name, department):
        self.__name = name
        self.__dept = department

    def setDepartment(self, dept_name):
        self.__dept = dept_name

    def getDepartment(self):
        return self.__dept

class CourtAppearance:

    def __init__(self):
        self.__when = ''

    def __call__(self, appear_date, case_num):

        cases = get_list( appear_date )

        for case in cases:
            if case['caseNbr'] == case_num:
                return case

        return {}

    def setCourtName(self, name):
        self.__court_name = name

    def getCourtName(self):
        return self.__court_name

    court_name = property(getCourtName, setCourtName)

    def setWhen(self, appear_datetime):
        self.__when = appear_datetime

    def getWhen(self):
        return self.__when

    when = property(getWhen, setWhen)

    def setCaseNumber(self, case_number):
        self.__case_number = case_number

    def getCaseNumber(self):
        return self.__case_number

    case_number = property(getCaseNumber, setCaseNumber)

    def setParties(self, parties):
        self.__parties = parties

    def getParties(self):
        return self.__psrties

    parties = property(getParties, setParties)

    def setCourt(self, court_name, department):
        self.__court = Court(name, department)

    def getCourt(self):
        return self.__court

    court = property(getCourt, setCourt)

get_case = CourtAppearance()


class CourtAppearanceList:

    def __call__(self, appear_date):

        case_urls = []

        for court_name in court_names:

            depts = requests.get("https://portal.scscourt.org/api/calendar/" + court_name + "/" + appear_date + "/" + appear_date)

            data = depts.json()['data']

            for dept_info in data:
                case_urls.append(
                    'https://portal.scscourt.org/api/calendardepartment/' +
                    dept_info['courtroom'] + '/' +
                    court_name + '/' +
                    appear_date + '/' + appear_date)

        calendar_infos = []

        for case_url in case_urls:

            cal = requests.get(case_url).json()

            for cal_entry in cal['data']:
                cal_entry['court'] = court_name
                cal_entry['created'] = cal['created']

                calendar_infos.append(cal_entry)

        return calendar_infos

get_list = CourtAppearanceList()


