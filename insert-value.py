import mysql.connector as db

conn = db.connect(host="localhost", user="root", passwd="", database="detail")
cur = conn.cursor()

details = []

owner = input("Owner : ")
state = input("State : ")
district = int(input("District : "))
unqalpha = input("Unique Alphabet : ")
unqnum = int(input("Unique 4 Digit : "))

details.append(owner)
details.append(state)
details.append(district)
details.append(unqalpha)
details.append(unqnum)

sql_query = "INSERT INTO plates (name,state,district,unqalpha,unqnum)VALUES(%s,%s,%s,%s,%s);"
cur.execute(sql_query,details)
conn.commit()

conn.close()