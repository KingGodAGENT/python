import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()
sql = '''
insert into Books(id, title, author, published_year, in_stock)
values (1, '파이썬은 과연 병인가?', '어린왕자', '2024', True);
'''

cursor.execute(sql)
connection.commit()
connection.close()