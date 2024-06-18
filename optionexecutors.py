from services import *
from time import sleep
from abc import ABC, abstractmethod


class OptionExecutor(ABC):
    def __init__(self, connection, client_dirver):
        self._client_driver = client_dirver
        self._connection = connection

    @abstractmethod
    def execute(self):...


class GetAllHabitantExecutor(OptionExecutor):
    def execute(self):
        habitants = GetAllHabitantsService(self._connection).execute()

        for i in habitants:
            self._client_driver.output(f"ID:{i['id']}")
            self._client_driver.output(f"Имя: {i['name']}")
            self._client_driver.output(f"Зарплата: {i['selery']}")
            self._client_driver.output(f"Баланс: {i['balance']}")
            self._client_driver.output(f"Работа: {i['job']}")
            self._client_driver.output('------------------')

        self._client_driver.user_input('')


class HabitantUpdateExecutor(OptionExecutor):
    def execute(self):
        updated_habitant_params = self._client_driver.get_updated_habitant_params()
        UpdateHabitantService(self._connection).execute(
            updated_habitant_params['habitant_id'], **updated_habitant_params['new_params'])
        
class NewHabitantCreateExecutor(OptionExecutor):
    def execute(self):
        new_habitant_params = self._client_driver.get_new_habitant_params()
        CreateHabitantService(self._connection).execute(**new_habitant_params)


class SeleryToAllHabitantsExecutor(OptionExecutor):
    def execute(self):
        SeleryToAllHabitantsService(self._connection).execute()
        self._client_driver.output('Зарплата всем жителям раздана успешно!')
        sleep(3)


class TransactionWithTwoHabitantsExecutor(OptionExecutor):
    def execute(self):
        transaction_data = self._client_driver.get_transaction_data()
        TransactionWithTwoHabiatntsService(
            self._connection).execute(*transaction_data)
        self._client_driver.output('Транзакция завершилась успешно!')
        sleep(3)


class DeleteHabitantExecutor(OptionExecutor):
    def execute(self):
        name_to_delete = self._client_driver.get_name_of_habitant_to_delete()
        DeleteHabitantService(self._connection).execute(name=name_to_delete)
        self._client_driver.output(
            f'Житель с именем {name_to_delete} был успешно удален из системы!')
        sleep(3)
