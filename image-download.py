import mysql.connector as db
import os

def write(data,filename):
    with open(filename,'wb') as file:
        file.write(data)
    print("Downloaded")

def main():
    i = 0
    conn = db.connect(host="localhost", database="detail",user="root",password="")
    cur = conn.cursor()

    sql_query = "SELECT * FROM image;"
    cur.execute(sql_query)

    result = cur.fetchall()
    for row in result:
        filename = os.path.join('K:/result/',str(row[0])+'.jpeg')
        img = row[1]
        print(type(img))
        write(img,filename)


if __name__ == "__main__":
    main()
