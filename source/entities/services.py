from source.db.validators import *


#critical buisness rules
class Service(ABC):
    def __init__(self, data_source):
        self._ds = data_source

    @abstractmethod
    def execute(self):...


class CreateHabitantService(Service):
    def execute(self, **params):
        KwargsValidator(**params).validate()
        self._ds.insert('habitants', **params)


class GetAllHabitantsService(Service):
    def execute(self):
        return self._ds.select('habitants','all')


class UpdateHabitantService(Service):
    def execute(self, instance_id,**kwargs):
        KwargsValidator(**kwargs).validate()
        self._ds.update('habitants', instance_id, **kwargs)


class DeleteHabitantService(Service):
    def execute(self,**instance_params):
        KwargsValidator(**instance_params).validate()
        self._ds.delete('habitants', **instance_params)


class SeleryToAllHabitantsService(Service):
    def execute(self):
        habitants = GetAllHabitantsService(self._ds).execute()

        for i in habitants:
            updated_balance = i['balance'] + i['selery']
            self._ds.update('habitants', i['id'], balance=updated_balance)


class TransactionWithTwoHabiatntsService(Service):
    def execute(self,id_to_decrease,id_to_increase,amount):
        increased_habitant_balance = self._ds.select('habitants','balance',id=id_to_increase)[0]['balance'] + amount
        decreased_habitant_balance = self._ds.select('habitants', 'balance', id=id_to_decrease)[0]['balance'] - amount

        result_sql_string = SqlUpdateStringGenerator().generate_sql_string('habitants',id_to_decrease,balance=decreased_habitant_balance) + SqlUpdateStringGenerator().generate_sql_string('habitants',id_to_increase,balance=increased_habitant_balance)

        self._ds.transaction(result_sql_string)


class GetOneHabitantDataSevice(Service):
    def execute(self,name):
        habitant_data = self._ds.select('habitants','all',name=name)

        return habitant_data[0]