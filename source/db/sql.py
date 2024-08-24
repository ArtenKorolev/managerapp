from source.db.sqlstringgenerators import *
from abc import ABCMeta,abstractmethod


class SqlCommand(metaclass=ABCMeta):
    def __init__(self, db):
        self._data_base = db

    @abstractmethod
    def execute(self, table: str, *args): ...


class SqlInsert(ABC, SqlCommand):
    def execute(self, table, **new_object_params):
        ...


class SqlGetColumnsFromTable(ABC,SqlCommand):
    def execute(self, table):
        ...


class SqlSelect(ABC,SqlCommand):
    def execute(self, table, *fields_to_select, **select_condition_fields):
        ...


class SqlUpdate(ABC,SqlCommand):
    def execute(self, table, instance_id, **fields_and_values_to_update):
        ...


class SqlDelete(ABC,SqlCommand):
    def execute(self, table, **instance_params):
        ...


class SqlTransaction(ABC,SqlCommand):
    def execute(self,sql_operations_string):
        ...
