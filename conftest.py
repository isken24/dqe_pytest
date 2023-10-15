import pytest
import pyodbc
from variables import *


@pytest.fixture(scope='module')
def connection_string():
    conn_str = f'DRIVER={DRIVER};SERVER={SERVER};' \
                       f'DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    yield conn_str


@pytest.fixture(scope='module')
def cnxn(connection_string):
    cnxn = pyodbc.connect(connection_string)
    yield cnxn
    cnxn.close()


@pytest.fixture
def cursor(cnxn):
    cursor = cnxn.cursor()
    yield cursor
    cursor.close()
