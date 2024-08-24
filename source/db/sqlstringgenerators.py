from abc import ABC,abstractmethod
from .converters import *


class SqlStringGenerator(ABC):
    @abstractmethod
    def generate_sql_string(self):...


class SqlInsertStringGenerator(SqlStringGenerator):
    def generate_sql_string(self, table, **new_object_params):
        arguments = KwargsToInsertSqlStrConverter().convert(**new_object_params)

        sql_string = f"INSERT INTO {table} ({arguments[0]}) VALUES ({arguments[1]});"
        return sql_string


class SqlSelectStringGenerator(SqlStringGenerator):
    def generate_sql_string(self, table, *fields_to_select):
        arguments = ArgsToSqlStrConverter().convert(*fields_to_select)
        
        sql_string = f"SELECT {arguments} FROM {table};"
        return sql_string
    

class SqlSelectWithConditionsStringGenerator(SqlStringGenerator):
    def generate_sql_string(self, table, *fields_to_select, **conditions):
        fields = ArgsToSqlStrConverter().convert(*fields_to_select)
        conditions = KwargsToSqlStrConverter().convert(**conditions)

        sql_string = f"SELECT {fields} FROM {table} WHERE {conditions};"
        return sql_string
    

class SqlUpdateStringGenerator(SqlStringGenerator):
    def generate_sql_string(self, table, instance_id, **fields_and_values_to_update):
        arguments = KwargsToSqlStrConverter().convert(**fields_and_values_to_update)
        instanceid = ArgsToSqlStrConverter().convert(instance_id)

        sql_string = f"UPDATE {table} SET {arguments} WHERE id = {instanceid};"
        return sql_string


class SqlDeleteStringGenerator(SqlStringGenerator):
    def generate_sql_string(self, table, **instance_params):
        params = KwargsToSqlStrConverter().convert(**instance_params)

        sql_string = f"DELETE FROM {table} WHERE {params};"
        return sql_string
    

class SqlColumnsFromTableStringGenerator(SqlStringGenerator):
    def generate_sql_string(self, table):
        sql_string = f"PRAGMA table_info({table});"
        return sql_string
    

class SqlTransactionStringGenerator(SqlStringGenerator):
    def generate_sql_string(self,sql_operations_string):
        sql_string = "BEGIN TRANSACTION;" + sql_operations_string + "COMMIT;"
        return sql_string
