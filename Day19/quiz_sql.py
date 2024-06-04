import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()
sql = '''
create table Books(
    id int primary key,
    title text,
    author text,
    published_year text,
    in_stock bool
)
'''

cursor.execute(sql)
connection.commit()
connection.close()