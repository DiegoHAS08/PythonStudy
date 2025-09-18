import sqlite3

con = sqlite3.connect("banco.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)")
cur.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", ("Diego", 20))

con.commit()
con.close()
