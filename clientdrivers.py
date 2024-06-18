from services import *


class ClientDriver:
    def __init__(self,client):
        self.__client = client
    
    def output(self, info):
        self.__client.output(info)

    def user_input(self,query_string):
        return self.__client.user_input(query_string)

    def clear(self):
        self.__client.clear()

    def get_new_habitant_params(self):
        self.__client.output('Введите параметры нового жителя:')
        params = self.__get_habitant_params()

        new_habitant_params = {
            'name': params['name'],
            'selery': params['selery'],
            'balance': params['balance'],
            'job': params['job']
        }

        return new_habitant_params

    def get_updated_habitant_params(self):
        habitant_id = int(self.__client.user_input(
            'Ведите id жителя, чьи параметры хотите изменить:'))

        print('Далее введите измененные параметры этого жителя, если параметр менять не надо, введите его прежнее значение')
        params = self.__get_habitant_params()

        updated_habitant_params = {
            'name': params['name'],
            'selery': params['selery'], 
            'balance': params['balance'],
            'job': params['job']
        }
        return {'habitant_id':habitant_id,'new_params':updated_habitant_params}

    def __get_habitant_params(self):
        while True:
            try:
                params = self.__try_to_get_habitant_params()
                KwargsValidator(**params).validate()
                return params
            except ValueError:
                self.__client.output('Введите число!')
            except KwargsParamValidateExeption as e:
                self.__client.output(f'Ошибка - {e.error_message}')

    def __try_to_get_habitant_params(self):
        name = self.__client.user_input('Имя :')
        selery = int(self.__client.user_input('Зарплата :'))
        balance = int(self.__client.user_input('Баланс: '))
        job = self.__client.user_input('Работа: ')

        return {'name': name,'selery': selery,'balance': balance,'job': job}
    
    def get_transaction_data(self):
        while True:
            try:
                return self.__try_to_get_transaction_data()
            except ValueError:
                self.__client.output('Введите число!')

    def __try_to_get_transaction_data(self):
        decrease_id = int(self.__client.user_input('Введите id жителя, деньги у которого со счета хотите списать:'))
        increase_id = int(self.__client.user_input('Введите id жителя, которому хотите положить деньги на счет:'))
        amount = int(self.__client.user_input('Введите количество средств для передачи:'))

        return (decrease_id,increase_id,amount)

    def get_name_of_habitant_to_delete(self):
        name = self.__client.user_input('Введите имя жителя, которого хотите удалить из системы:')

        return name
