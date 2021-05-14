import pandas as pd
import re

def data_processor_pandas(filename):
    print("Data processor working on: " + filename)
    # df = pd.read_csv('filename.csv', sep='\t')

    df = pd.read_table(filename)
    print(df)

    # df1 = df[df['c_resid,unit,nace_r2,geo\\time'].str.contains('ES' or  'EL', na=False, regex = True) ]
    # print(df1)
    print("AAAAAAAAAAA")

    # df = df[df['c_resid,unit,nace_r2,geo\\time'].str.contains(pat = 'ES|EL', regex = True) ]

    # print(df['c_resid,unit,nace_r2,geo\\time'].str.contains(pat = 'ES|EL', regex = True))
    df = df.loc[df['c_resid,unit,nace_r2,geo\\time'].str.contains(pat = 'ES|EL', regex = True) ]


    print(df)
    # print(df.columns)
    # print(df['c_resid,unit,nace_r2,geo\\time'].str.contains(pat='ES|EL', regex=True, axis = 1))

    df2 = df.loc[df.columns[df.columns.str.contains('2019|2018')],axis = 1]
    print(df)
    # df =
    # print("BBBBBBBBB")
    # df1.drop(list(df1.filter(regex = 'not(2016|2017|2018|2019)')), axis = 1, inplace = True)
    # df2 = df1.drop(['2018'],axis=1)
    # column_list = [0,1,2,3]


    # df2 =  df2.drop(df2.columns[column_list], axis = 1)
    # df = df.columns[df.columns.str.contains('2019|2018|2017|2016',axis = 1)]
    # print(df)