import mysql.connector as db

conn = db.connect(host="localhost", user="root", passwd="", database="detail")
cur = conn.cursor()

sql_query = "SELECT * FROM plates;"
cur.execute(sql_query)
result = cur.fetchall()

for row in result:
        print("Owner : ",row[0])
        print("State : ",row[1])
        print("District : ",row[2])
        print("Unqalpha : ",row[3])
        print("Unqnum : ",row[4])
        print()

conn.close()