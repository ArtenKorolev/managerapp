from source.db.db import Database
from source.sqlitedb.sqlite3commands import *


class Sqlite(Database):
    def __init__(self, db):
        self._data_base = db

    def insert(self,table,**new_object_params):
        SqliteInsert(self._data_base).execute(table, **new_object_params)

    def select(self,table, *fields_to_select, **select_condition_fields):
        return SqliteSelect(self._data_base).execute(table, *fields_to_select, **select_condition_fields)

    def update(self,table, instance_id, **fields_and_values_to_update):
        SqliteUpdate(self._data_base).execute(table, instance_id, **fields_and_values_to_update)

    def delete(self,table, **instance_params):
        SqliteDelete(self._data_base).execute(table, **instance_params)

    def transaction(self,sql_operations_string):
        SqliteTransaction(self._data_base).execute(sql_operations_string)

