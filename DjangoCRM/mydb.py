"""
Steps:

1.Install mysql community version
2. Run install and set root username and password: "root" for both in my case.
3. pip install mysql
4. pip install mysql-connector (will most likely give error :mysql.connector.errors.NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported)
or pip install mysql-connector-python (no errors - perfectly working)
"""

import mysql.connector

dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"

)

#prepare a cursor object

cursorObject=dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE elderco")# mysql command to create database

#message for terminal - optional

print("All Done!")
#Note: Just need to create database once.
#To confirm database is created, open MySql WORKBENCH -> "schemas" at the bottom corner and see your database name

"""
if you get mysql.connector.errors.NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported

open terminal and : pip install mysql-connector-python
"""

#After setting the database, migrate - but first run pip install mysqlclient