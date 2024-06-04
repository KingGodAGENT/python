import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()
sql = '''
insert into coffee(id, coffeeName, coffeePrice, coffeeKcal)
values (2, 'americano', 2500, 10);
'''

cursor.execute(sql)
connection.commit()
connection.close()