from sql import *
from validators import *


def test_sql_select():
    a = SqlSelect('seleries.db').execute('habitants','name','job',name='илья')
    print(a)
    a = SqlSelect('seleries.db').execute('habitants','job','selery')
    print(a)
    a = SqlSelect('seleries.db').execute('habitants', 'name', 'balance',name='ортем')
    print(a)
    a = SqlSelect('seleries.db').execute('habitants', 'job', 'selery',name='лера')
    print(a)

def test_validators():
    IsNameInDataBaseValidator('илья').validate()

# test_sql_select()
test_validators()