import sqlite3

connection = sqlite3.connect('plagiarism.db')

cr=db.cursor()
cr.execute("insert into customer(id,name,login,password,admin) values('1','ram','ram_ji','123','abc')")

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO customer (id,name,login,password) VALUES (?, ?,?,?)",
            ('First Post', 'Content for the first post')
            )


connection.commit()
connection.close()