from sql import *
from abc import ABC, abstractmethod
from validators import *


class Service(ABC):
    def __init__(self, connection):
        self._connection = connection

    @abstractmethod
    def execute(self):...


class CreateHabitantService(Service):
    def execute(self, **params):
        KwargsValidator(**params).validate()
        SqlInsert(self._connection).execute('habitants', **params)


class GetAllHabitantsService(Service):
    def execute(self):
        return SqlSelect(self._connection).execute('habitants','all')


class UpdateHabitantService(Service):
    def execute(self, instance_id,**kwargs):
        KwargsValidator(**kwargs).validate()
        SqlUpdate(self._connection).execute('habitants', instance_id, **kwargs)


class DeleteHabitantService(Service):
    def execute(self,**instance_params):
        KwargsValidator(**instance_params).validate()
        SqlDelete(self._connection).execute('habitants', **instance_params)


class SeleryToAllHabitantsService(Service):
    def execute(self):
        habitants = GetAllHabitantsService(self._connection).execute()

        for i in habitants:
            updated_balance = i['balance'] + i['selery']
            SqlUpdate(self._connection).execute('habitants', i['id'], balance=updated_balance)


class TransactionWithTwoHabiatntsService(Service):
    def execute(self,id_to_decrease,id_to_increase,amount):
        #FIXME вывод словаря из SqlSelect багованый, баланс доступен по ключу id
        print(SqlSelect(self._connection).execute(
            'habitants', 'balance', id=id_to_increase))
        increased_habitant_balance = SqlSelect(self._connection).execute('habitants','balance',id=id_to_increase)[0]['balance'] + amount
        decreased_habitant_balance = SqlSelect(self._connection).execute('habitants', 'balance', id=id_to_decrease)[0]['balance'] - amount

        result_sql_string = SqlUpdateStringGenerator().generate_sql_string('habitants',id_to_decrease,balance=decreased_habitant_balance) + SqlUpdateStringGenerator().generate_sql_string('habitants',id_to_increase,balance=increased_habitant_balance)
        
        print(result_sql_string)

        SqlTransaction(self._connection).execute(result_sql_string)


class GetOneHabitantDataSevice(Service):
    def execute(self,name):
        habitant_data = SqlSelect(self._connection).execute('habitants','all',name=name)
        print(habitant_data)
        return habitant_data[0]