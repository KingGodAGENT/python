import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()
sql = '''
create table COFFEE(
    id integer primary key,
    coffeeName Text,
    coffeePrice integer,
    coffeeKcal integer
)
'''

cursor.execute(sql)
connection.commit()
connection.close()