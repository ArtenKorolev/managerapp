from abc import abstractmethod, ABC
from sqlstringgenerators import *
import sqlite3


class SqlCommand(ABC):
    def __init__(self, db):
        self._data_base = db

    @abstractmethod
    def execute(self, table: str, *args): ...


class SqlInsert(SqlCommand):
    def execute(self, table, **new_object_params):
        connection = sqlite3.connect(self._data_base)
        cursor = connection.cursor()

        sql_string = SqlInsertStringGenerator().generate_sql_string(table,**new_object_params)
        cursor.execute(sql_string)

        connection.commit()
        cursor.close()
        connection.close()


class SqlGetColumnsFromTable(SqlCommand):
    def execute(self, table):
        connection = sqlite3.connect(self._data_base)
        cursor = connection.cursor()

        sql_string = SqlColumnsFromTableStringGenerator().generate_sql_string(table)
        cursor.execute(sql_string)

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return self.__generate_list_with_columns_name(result)

    #TODO refactoring
    @staticmethod
    def __generate_list_with_columns_name(t):
        l = []
        for i in t:
            l.append(i[1])
        return l


class SqlSelect(SqlCommand):
    def execute(self, table, *fields_to_select, **select_condition_fields):
        connection = sqlite3.connect(self._data_base)
        cursor = connection.cursor()

        if not select_condition_fields:
            sql_string = SqlSelectStringGenerator().generate_sql_string(table, *fields_to_select)
        elif select_condition_fields:
            sql_string = SqlSelectWithConditionsStringGenerator().generate_sql_string(table,*fields_to_select,**select_condition_fields)

        cursor.execute(sql_string)

        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return self.__generate_list_with_dicts_of_objects(table,result,*fields_to_select) 
    
    #TODO refactoring
    def __generate_list_with_dicts_of_objects(self,table,list_with_tuples_with_object_data, *fields_to_select):
        list_with_dicts_of_objects = []

        list_of_columns_name = SqlGetColumnsFromTable(self._data_base).execute(table)

        for i in list_with_tuples_with_object_data:
            current_object_dict = dict()

            if fields_to_select == ('all',):
                columns_names = list_of_columns_name
            elif fields_to_select != ('all',):
                columns_names = fields_to_select 

            for j in range(len(i)):

                current_object_dict[columns_names[j]] = i[j]

            list_with_dicts_of_objects.append(current_object_dict)
        
        return list_with_dicts_of_objects


class SqlUpdate(SqlCommand):
    def execute(self, table, instance_id, **fields_and_values_to_update):
        connection = sqlite3.connect(self._data_base)
        cursor = connection.cursor()

        sql_string = SqlUpdateStringGenerator().generate_sql_string(table, instance_id, **fields_and_values_to_update)
        cursor.execute(sql_string)

        connection.commit()
        cursor.close()
        connection.close()


class SqlDelete(SqlCommand):
    def execute(self, table, **instance_params):
        connection = sqlite3.connect(self._data_base)
        cursor = connection.cursor()

        sql_string = SqlDeleteStringGenerator().generate_sql_string(table,**instance_params)
        cursor.execute(sql_string)

        connection.commit()
        cursor.close()
        connection.close()


class SqlTransaction(SqlCommand):
    def execute(self,sql_operations_string):
        connection = sqlite3.connect(self._data_base)
        cursor = connection.cursor()

        sql_string = SqlTransactionStringGenerator().generate_sql_string(sql_operations_string)
        cursor.executescript(sql_string)

        connection.commit()
        cursor.close()
        connection.close()
