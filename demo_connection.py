import sys
sys.path.append('C:/Users/Iskandar_Khudzhamkul/AppData/Local/Programs/Python/Python38/lib/site-packages/pymssql')

import pymssql
from pymssql import *


conn = pymssql.connect(
    server='127.0.0.1',
    user='testlogin',
    password='testPa$$24',
    database='AdventureWorks2012',
    tds_version=r'7.0'
    #as_dict=True
)

SQL_QUERY = """
SELECT COUNT(*) FROM [Person].[Address]
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY)

records = cursor.fetchall()
for r in records:
    print(r)

