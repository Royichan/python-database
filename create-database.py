import mysql.connector as db

conn = db.connect(host="localhost",user="root",passwd="")
cur = conn.cursor()
sql = "CREATE DATABASE detail;"
cur.execute(sql)
conn.close()