import mysql.connector

def db_stuff(df_in):

    print("Doing MYSQL STUFF")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor"
    )


    mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE mydatabase")

    mycursor.execute("DROP DATABASE IF EXISTS arxes_db;")
    myresult = mycursor.fetchall()
    print (myresult)

    mycursor.execute("CREATE DATABASE arxes_db;")
    myresult = mycursor.fetchall()
    print (myresult)

    mycursor.execute("SHOW DATABASES;")
    myresult = mycursor.fetchall()
    print (myresult)

    mycursor.execute("use arxes_db;")
    myresult = mycursor.fetchall()
    print (myresult)

    print("~Doing MYSQL STUFF")

    df_in.to_sql(con = 'test_name')
