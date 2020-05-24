import mysql.connector as db
import glob

def convertToBinary(filename):
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(plate):
    conn = db.connect(host="localhost", database="detail",user="root",password="")
    cur = conn.cursor()
    
    photo = plate
    platePicture = convertToBinary(photo)
    sql_query = "INSERT INTO image (plateimg) VALUES (%s)"
    cur.execute(sql_query,(platePicture,))
    print("Uploaded")
    
    conn.commit()
    conn.close()

def main():
    #path to folder
    path = glob.glob('K:/number-plates/*.jpeg')
    print(path)
    for img in path:
        insertBLOB(img)

if __name__ == "__main__":
    print("enter main")
    main()