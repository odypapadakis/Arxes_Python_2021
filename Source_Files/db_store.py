import mysql.connector


def db_stuff(stuff_in):

    for i in range(len(stuff_in)):
        print(stuff_in[i])
        print("\n")
    # stuff in is a list of 3 items of the following types
    #   1) dataframe 2) Simple Name 3)long name

    df_in = stuff_in[0][0]
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
        table_name = stuff_in[k][1]
        sql = ("CREATE TABLE " + table_name +
               "(id INT AUTO_INCREMENT PRIMARY KEY, country_type VARCHAR(255)," +
               "`2016` INT,`2017` INT,`2018` INT,`2019` INT)")
        mycursor.execute(sql)
        base_sql_insert = "INSERT INTO " + table_name + " (`country_type`,`2016`,`2017`,`2018`,`2019`) VALUES ('"

        for i in range(len(df_in.columns)):

            temp = df_in.iloc[1, i]

            if i != 0:
                base_sql_insert += "'"
                temp = temp.rstrip(temp[-1])

            base_sql_insert += temp + "',"

        base_sql_insert = base_sql_insert.rstrip(base_sql_insert[-1])
        base_sql_insert += ");"
        mycursor.execute(base_sql_insert)
        mydb.commit()
