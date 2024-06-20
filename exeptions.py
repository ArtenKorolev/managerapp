class KwargsParamValidateExeption(Exception):
    def __init__(self, error_message):
        self.error_message = error_message


class NameNotInDataBaseExeption(Exception):
    def __init__(self,error_message):
        self.error_message = error_message