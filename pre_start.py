import sqlite3

connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# This program should be executed before running main.py

try:
    with open ('table_creation.sql','r') as sql_file:
        sql_file=sql_file.read()
        cursor.executescript(sql_file)
        print('Executed script, all tables created')
except Exception as e:
    print("Couldn't find 'table_creation.sql' file, make sure to check the path")
    print(e)
    exit()

# Will insert dummy records
try:
    with open ('dummy_record.sql','r') as sql_file:
        sql_file=sql_file.read()
        cursor.executescript(sql_file)
        print('Executed script, all records inserted')
except Exception:
    print("Couldn't find 'insert_records.sql' file, make sure to check the path")
    exit()

print('Pre-start script executed successfully')
print("Program will exit now")
