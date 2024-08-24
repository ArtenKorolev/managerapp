from source.entities.use_cases.optionexecutors import *


class OptionExecutorFacade:
    def __init__(self,connection,client_driver):
        self.__updater = HabitantUpdateExecutor(connection,client_driver)
        self.__creator = NewHabitantCreateExecutor(connection, client_driver)
        self.__selery_issuer = SeleryToAllHabitantsExecutor(connection, client_driver)
        self.__transaction_executor = TransactionWithTwoHabitantsExecutor(connection, client_driver)
        self.__all_habitant_browser = GetAllHabitantExecutor(connection, client_driver)
        self.__habitant_deleter = DeleteHabitantExecutor(connection,client_driver)
        self.__one_habitant_browser = GetOneHabitantExecutor(connection,client_driver)
    
    def update_habitant(self):
        self.__updater.execute()
    
    def create_habitant(self):
        self.__creator.execute()

    def selery_to_all_habitants(self):
        self.__selery_issuer.execute()

    def transaction_with_two_habitants(self):
        self.__transaction_executor.execute()

    def get_all_habitants(self):
        self.__all_habitant_browser.execute()

    def delete_habitant(self):
        self.__habitant_deleter.execute()

    def get_one_habitant(self):
        self.__one_habitant_browser.execute()