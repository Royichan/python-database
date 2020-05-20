import mysql.connector as db

conn = db.connect(host="localhost",user="root",passwd="",database="detail")
cur = conn.cursor()
sql_query = "CREATE TABLE plates (name VARCHAR(30) PRIMARY KEY, state CHAR(2), district INT(2), unqalpha CHAR(1), unqnum INT(4));"
cur.execute(sql_query)
conn.close()