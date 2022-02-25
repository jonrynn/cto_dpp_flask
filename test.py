import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "create table users (petID int, petName text, ownerName text, petType text)"

cursor.execute(create_table)

user = ('1', 'fido', 'fred', 'dog')
insert_query = "insert into users values (?,?,?,?)"
cursor.execute(insert_query, user)

select_query = "select * from users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
