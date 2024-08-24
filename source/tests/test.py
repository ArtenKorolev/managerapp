from source.entities.services import GetAllHabitantsService
from source.sqlitedb.sqlite3 import Sqlite
from source.db.validators import *


def test_sql_select():
    a = SqlSelect('population.db').execute('habitants','name','job',name='илья')
    print(a)
    a = SqlSelect('population.db').execute('habitants','job','selery')
    print(a)
    a = SqlSelect('population.db').execute('habitants', 'name', 'balance',name='ортем')
    print(a)
    a = SqlSelect('population.db').execute('habitants', 'job', 'selery',name='лера')
    print(a)

def test_validators():
    IsNameInDataBaseValidator('илья').validate()

# test_sql_select()
# test_validators()

def test_all_hab():
    a = GetAllHabitantsService(Sqlite('population.db')).execute()
    print(a)

def test_sqlite3():
    a = Sqlite('population.db').select('habitants','all')
    print(a)

