# from sqlalchemy import create_engine
# import pymysql
# import mysql.connector
# import pandas as pd
#
# def db_stuff2(df):
#
#     data = pd.DataFrame({
#         'book_id': [12345, 12346, 12347],
#         'title': ['Python Programming', 'Learn MySQL', 'Data Science Cookbook'],
#         'price': [29, 23, 27]
#     })
#
#     connection = mysql.connector.connect(host='localhost',
#                                  user='root',
#                                  password='toor'
#                                  )
#
#     mycursor = connection.cursor(buffered=True)
#
#     mycursor.execute("DROP DATABASE IF EXISTS arxes_db;")
#     mycursor.execute("CREATE DATABASE arxes_db;")
#
#
#
#
#     engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
#                            .format(user="root",
#                                    pw="12345",
#                                    db="arxes_db",))
# s
#     data.to_sql('book_details', con=engine, if_exists='append', chunksize=1000)

import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

def db_stuff2(df):
    engine = create_engine('mysql+mysqlconnector://[root]:[toor]@[localhost]:[port]/[arxes_db]', echo=False)
    df.to_sql(name='sample_table2', con=engine, if_exists='append', index=False)

