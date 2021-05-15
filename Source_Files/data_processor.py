import pandas as pd
import re
from os import path
import tkinter as tk
from tkinter import messagebox as mb

def data_processor(filename):
    # filename = "Data_Arrivals.tsv"

    # Select years
    start_year = 2016
    end_year = 2019


    selected_years =  str(start_year)
    for i in range(start_year+1 , end_year +1):
        selected_years = selected_years +"|" + str(i)



    selected_countries = "EL|ES"

    # The regular expressions for the selections are completed
    selected_countries_RE = selected_countries + "\Z"
    selected_years_RE = re.compile(selected_years + "|COUNTRY")

    # load the tsv into a pandas dataframe
    df = pd.read_table(filename)

    # Change the first column name, because it has silly characters and causes problems
    df = df.rename(columns={df.columns[0]: 'COUNTRY'})

    #In the dataframe df, return true if the RE:Selected_countries_RE is true
    mask = (df['COUNTRY'].str.contains(selected_countries_RE,regex = True))

    # Apply the mask to the dataframe to filter
    df = df[mask]

    # Filter out the columns that do not match the selected years
    df = df.filter(regex=selected_years_RE, axis=1)

    # df.to_csv(filename, index=False)
    # print(df)

    size = len(filename)
    # Slice string to remove last 3 characters from string
    filename = filename[:size - 4]

    filename  = filename + ".csv"

    # try:
    #     f = open(filename, "wb")
    # except  IOError as ex_IO:
    #     mb.showinfo(" Error writing file:", "File: \n" + filename + "\n Error: " + str(ex_IO))
    #     exit(0)
    # print("OK to write")

    if (path.isfile(filename)):
        overwrite = mb.askquestion("File already exists", "Overwrite --> " + filename + " <-- ?? ")
        if (overwrite == "no"):
            mb.showinfo("No Changes made", " Exiting\t\t")
            exit(0)

    try:
        # Write the files to disk
        f = open(filename, "wb")
        # f.write("dummy_data")
        f.close()
    except IOError as ex_IO:
        mb.showinfo(" Error writing file:", "File: \n" + filename + "\n Error: " + str(ex_IO))
        exit(0)

    df.to_csv(filename, encoding='utf-8', index=False)