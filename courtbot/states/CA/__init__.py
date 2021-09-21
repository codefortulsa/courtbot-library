
"""A package for retreiving court calendar data from Santa Clara County, California"""

class Court:

   __all__ = ["Civil",
               "Probate",
               "Family",
               "Juvenile",
               "Criminalhoj",
               "CriminalPaloAlto",
               "CriminalSouthCounty"]

    __init__(self, name, department):
        self.__name = name
        self.__dept = department

    def setDepartment(self, dept_name):
        self.__dept = dept_name

    def getDepartment(self):
        return self.__dept

class CourtAppearance:

    def __init__(self):
        self.__when = ''

    def setWhen(self, appearance_datetime):
        self.__when = appearance_datetime

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

