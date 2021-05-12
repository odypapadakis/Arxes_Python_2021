import mysql.connector

def db_stuff():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor"
    )

    mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE mydatabase")
    a = mycursor.execute("SHOW DATABASES")
    print (a)