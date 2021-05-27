# This function takes a list as its input and created mySQL database tables
# The list consists of 3 items
# 1 -> A pandas data frame,
#       This dataframe will be inserted into a database table
# 2 -> A Simple name
#        This name will be used to name our database tables
# 3 -> The original name of the tsv file, which we do not care about in this function.

import mysql.connector


def db_stuff(stuff_in):

    # df_in = stuff_in[0][0]
    # Create the connection to the local mySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="toor"
    )

    # Create a cursor to do our bidding
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute("DROP DATABASE IF EXISTS arxes_db;")
    mycursor.execute("CREATE DATABASE arxes_db;")
    mycursor.execute("use arxes_db;")

    for k in range(len(stuff_in)):
        print("K = " , k)
        # First step is to create a table.
        table_name = stuff_in[k][1]
        sql = ("CREATE TABLE " +
               table_name +
               "(id INT AUTO_INCREMENT PRIMARY KEY," +
               " country_type VARCHAR(255)," +
               "`2016` INT," +
               "`2017` INT," +
               "`2018` INT," +
               "`2019` INT)")

        mycursor.execute(sql)

        # This will be tha base sql insertion  query, which we will add to , in order to make the insertions
        sql_insert = "INSERT INTO " + table_name + " (`country_type`,`2016`,`2017`,`2018`,`2019`) VALUES ('"

        for i in range(len(stuff_in[k][0].columns)):
            print("i = ", i)
            temp = stuff_in[k][0].iloc[1, i]

            if i != 0:
                sql_insert += "'"
                temp = temp.rstrip(temp[-1])

            sql_insert += temp + "',"

        sql_insert = sql_insert.rstrip(sql_insert[-1])
        sql_insert += ");"
        mycursor.execute(sql_insert)
        mydb.commit()
