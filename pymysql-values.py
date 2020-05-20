import pymysql as db

conn = db.connect("localhost", "root", "", "plates")
cur = conn.cursor()

value = []
ename = input("Enter name : ")
value.append(ename)
estate = input("Enter the state : ")
value.append(estate)
edistrict = input("Enter district number : ")
value.append(edistrict)
eunqchar = input("Enter unique character : ")
value.append(eunqchar)
eunqnum = input("Enter 4 digit number : ")
value.append(eunqnum)

try:
    sql_query = "INSERT INTO details VALUES(%s,%s,%s,%s,%s);"
    cur.execute(sql_query,value)
    print("Successful")
except Exception as e:
    print("not successful")

conn.close()