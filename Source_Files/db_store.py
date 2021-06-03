# This function creates mySQL database from the input data
# This function requires a MySQL database to be up and running.

#  Use this !!!
#  pip install mysql-connector-python
import mysql.connector
from tkinter import messagebox as mb


# The inputis a list of  lists, each consistsing of 3 items
# 1 ) A pandas data frame list_in ,
# 2)  The user appointed name
# 3) The original name of the tsv file

def db_store(list_in):


    # Create the connection to the local mySQL database and test it
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="toor"
        )
    except mysql.connector.Error as err:
        print("DATABASE ERROR ", "ERROR Something went wrong:\n {}".format(err))
        mb.showerror("DATABASE ERROR ", "ERROR Something went wrong:\n {}".format(err))
        # print("ERROR Something went wrong: {}".format(err))
        return 1   # Return 1 if unable to connect to a database

    # Create a cursor
    mycursor = db_connection.cursor(buffered=True)

    # Create the database
    mycursor.execute("DROP DATABASE IF EXISTS arxes_db;")
    mycursor.execute("CREATE DATABASE arxes_db;")
    mycursor.execute("use arxes_db;")

    for k in range(len(list_in)):

        #  Get the dataframe from the list
        df = list_in[k][0]
        #  Get the user title from the list ( will be the name of the table )
        user_title = list_in[k][1]

        # First step is to create a table which will be named with the user provided name .
        table_name = user_title
        sql = ("CREATE TABLE " +
               table_name +
               "(id INT AUTO_INCREMENT PRIMARY KEY," +
               " country_visitor_type VARCHAR(255)," +
               "`2016` INT," +
               "`2017` INT," +
               "`2018` INT," +
               "`2019` INT)")
        print(sql)
        mycursor.execute(sql)

        # For each row in our table
        for j in range(len(list_in[k]) + 1):

            # Base sql insertion query string , concatenate stuff to it , in order to make the insertions queries
            sql_insert = "INSERT INTO " + table_name + \
                         " (`country_visitor_type`,`2016`,`2017`,`2018`,`2019`) VALUES ("

            # for each column item in a row
            for i in range(len(df.columns)):
                temp = "'"
                temp += df.iloc[j, i]

                # Delete the whitespace after the df item
                temp = temp.rstrip(temp[-1])

                sql_insert += temp + "',"

            #  Delete the last comma
            sql_insert = sql_insert.rstrip(sql_insert[-1])
            sql_insert += ");"

            # # Show the SQL query
            # print(sql_insert)

            # Execute it
            mycursor.execute(sql_insert)

            # Save the changes to the database
            db_connection.commit()
