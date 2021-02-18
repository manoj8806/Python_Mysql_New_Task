import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="manoj_db")
mycursor = mydb.cursor()
mycursor.execute("select * from employee")
result = mycursor.fetchall()
for i in result:
    print(i)
