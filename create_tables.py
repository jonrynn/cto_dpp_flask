import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "create table if not exists users (petID INTEGER PRIMARY KEY,  petName text, petOwner text, petType text)"
cursor.execute(create_table)

cursor.execute("insert into users values ('1','fido','fred','dog')")

connection.commit()

connection.close()


