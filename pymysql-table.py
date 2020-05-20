import pymysql as db

conn = db.connect("localhost", "root", "", "plates")
cur = conn.cursor()

query = "CREATE TABLE details (name VARCHAR(30) PRIMARY KEY, state CHAR(2), district INT(2), unqalpa CHAR(1), unqnum INT(4));"

cur.execute(query)

conn.close()