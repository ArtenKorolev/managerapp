from abc import ABC, abstractmethod
import os


class Client(ABC):
    @abstractmethod
    def user_input(self, query_string):...

    @abstractmethod
    def output(self,info):...

    @abstractmethod
    def clear(self):...


class ConsoleClient(Client):
    def user_input(self, query_string):
        user_input = input(query_string)
        return user_input

    def output(self, info):
        print(info)

    def clear(self):
        os.system('cls')

