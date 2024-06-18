from clientdrivers import *
from client import *
from optionexecutorfacade import *


# connection = sqlite3.connect('seleries.db')


class Main:
    def __init__(self,option_executor,client_driver):
        self.__options = option_executor
        self.__client_driver = client_driver

    def start(self):
        while True:
            self.__client_driver.clear()
            self.__client_driver.output('Добро пожаловать в менеджер работ, зарплат, баланса и многого другого!')
            self.__client_driver.output('Вот опции нашего менеджера:\n 1 - Посмотреть всех жителей города \n 2 - Добавить нового жителя \n 3 - Изменить параметры какого-то жителя \n 4 - Выдать зарплату всем жителям \n 5 - Удалить жителя \n 6 - Перевод с одного счета на другой \n 7 - Выйти')
            answer = int(self.__client_driver.user_input('Выберите одну опцию!'))
            
            if answer == 1:
                self.__options.get_all_habitants()
            elif answer == 2:
                self.__options.create_habitant()
            elif answer == 3:
                self.__options.update_habitant()
            elif answer == 4:
                self.__options.selery_to_all_habitants()
            elif answer == 5:
                self.__options.delete_habitant()
            elif answer == 6:
                self.__options.transaction_with_two_habitants()
            elif answer == 7:
                exit(0)
        

# if __name__ == "__main__":
#     try:
#         Main(HabitantController(connection, ClientDriver(ConsoleClient())),ClientDriver(ConsoleClient())).start()
#     except Exception as e:
#         print(f'Программа принудительно завершила работу с ошибкой {e}, сообщите разработчику и перезапустите менеджер')

Main(OptionExecutorFacade('seleries.db', ClientDriver(ConsoleClient())),
     ClientDriver(ConsoleClient())).start()
