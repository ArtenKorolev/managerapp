from abc import ABC,abstractmethod
from sql import *
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
        

class IsNameInDataBaseValidator(Validator):
    def __init__(self,name):
        self.__name = name

    def validate(self):
        all_names = SqlSelect('seleries.db').execute('habitants','name')

        for i in all_names:
            if i['name'] == self.__name:
                return
            
        raise NameNotInDataBaseExeption('Жителя с таким именем не существует!')
