import oscn


courts = oscn.courts


class MakeCase(object):

    def __call__(self, case_id):
        return oscn.request.Case(case_id)


get_case = MakeCase()
