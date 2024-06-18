from abc import ABC,abstractmethod
from exeptions import *


class Validator(ABC):
    @abstractmethod
    def validate(self):...


class KwargsValidator(Validator):
    def __init__(self, **kwargs):
        self.__kwargs = kwargs

    def validate(self):
        self.__validate_str_param('name')
        self.__validate_str_param('job')

    def __validate_str_param(self, param):
        try:
            int(self.__kwargs[param])
        except:
            return
        else:
            raise KwargsParamValidateExeption('Были переданы цифры там, где ожидается строка')
        
