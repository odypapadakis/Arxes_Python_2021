import mysql.connector
import pandas

def db_stuff(stuff_in):
    print("---------------")
    # print(stuff_in)
    for i in range(len(stuff_in)):
        print(stuff_in[i])
        print("\n")
    # stuff in containg 2 items
    #  each item is 1) dataframe 2) Simple Name 3)long name

    print("---------------")

    df_in = stuff_in[0][0]
    # print("Doing MYSQL STUFF")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor"
    )

    mycursor = mydb.cursor(buffered=True)
    # mycursor.execute("CREATE DATABASE mydatabase")

    mycursor.execute("DROP DATABASE IF EXISTS arxes_db;")
    # myresult = mycursor.fetchall()
    # print (myresult)

    mycursor.execute("CREATE DATABASE arxes_db;")
    # myresult = mycursor.fetchall()
    # print (myresult)

    # mycursor.execute("SHOW DATABASES;")
    # myresult = mycursor.fetchall()
    # print (myresult)

    mycursor.execute("use arxes_db;")
    # myresult = mycursor.fetchall()
    # print (myresult)

    sql = ("CREATE TABLE arrivals(id INT AUTO_INCREMENT PRIMARY KEY, country_type VARCHAR(255),`2016` INT,`2017` INT,`2018` INT,`2019` INT)")
    mycursor.execute(sql)

    sql = ("CREATE TABLE nights(id INT AUTO_INCREMENT PRIMARY KEY, country_type VARCHAR(255),`2016` INT,`2017` INT,`2018` INT,`2019` INT)")
    mycursor.execute(sql)

    print(df_in)
    # print(type(df_in))
    # for j in range(len(stuff_in[]))
    base_sql_insert = "INSERT INTO arrivals (`country_type`,`2016`,`2017`,`2018`,`2019`) VALUES ('"

    for i in range (len(df_in.columns)):

        temp = df_in.iloc[1, i]

        if(i!= 0):
            base_sql_insert += "'"
            temp = temp.rstrip(temp[-1])
        # print(df_in.iloc[0,i]+"**")


        base_sql_insert += temp + "',"

    base_sql_insert = base_sql_insert.rstrip(base_sql_insert[-1])
    base_sql_insert += ");"





    print(base_sql_insert)

    mycursor.execute(base_sql_insert)
    mydb.commit()
    # myresult = mycursor.fetchall()
    # print (myresult)



    # print("~Doing M   YSQL STUFF")