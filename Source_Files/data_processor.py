# This function "Cleans" the data to keep just the years / countries / type of visitor we want.
# In this instance we will keep the data for:
# Countries: Greece , Spain
# Years : 2016,2017,2018,2019
# Types of visitors: Foreigners and Total.
# It also stores the cleaned data in a csv file.

import pandas as pd
import re
from os import path
from os import remove
from tkinter import messagebox as mb

#  This function takes as input a list that contains:
# 1) The filename of the .tsv file on disk that has all the data.
# 2) The user created title of the data
# 3) The original filename

def data_processor(list_in):

    filename = list_in[0]
    user_title = list_in[1]
    original_name = list_in[2]

    print("Processing ", filename)

    #  ----------  Selection of years, countries, visitor types --------------------------------

    # Select years to keep data for.
    start_year = 2016
    end_year = 2019

    # Select countries to keep data for
    selected_countries = "EL|ES"

    # Slect visitor type to keep data for. Options are (FOR|LOC|TOTAL)
    visitor_type_RE = "FOR|TOTAL"

    #  ---------- Regular expressions creation  --------------------------------

    # Create the regular expression that holds the years to be kept in the dataframe
    selected_years = str(start_year)
    for i in range(start_year+1, end_year + 1):
        selected_years = selected_years + "|" + str(i)
    # For example "2016|2017|2018|2019"

    # Add the 'ends with character'  regex
    selected_countries_RE = selected_countries + "\Z"

    # load the as a pandas dataframe
    df = pd.read_table(filename)

    # Change the title of the first column, because it has weird characters that cause problems.
    df = df.rename(columns={df.columns[0]: 'COUNTRY'})

    # Keep the COUNTRY column, in addition to the selected years column
    selected_years_RE = re.compile(selected_years + "|COUNTRY")

    #  ---------- Filtering of the Data Frame --------------------------------

    # Filter out the columns that do not match the selected years
    df = df.filter(regex=selected_years_RE, axis=1)

    # Clear rows that do not match the countries Regex
    df = df[(df['COUNTRY'].str.contains(selected_countries_RE, regex=True))]

    # Clear rows that do not start with the visitor type Regex
    df = df[(df['COUNTRY'].str.match(visitor_type_RE))]

    # Create the csv files that we will store.
    size = len(filename)
    # Strip the last 4 character ( remove ".tsv" of the original filename )
    filename_out = filename[:size - 4] + ".csv"

    # Check for file existence and ask to write / overwrite
    if path.isfile(filename_out):
        overwrite = mb.askquestion("File already exists", "Overwrite --> " + filename_out + " <-- ?? ")
        if overwrite == "no":
            mb.showinfo("No Changes made", " Exiting\t\t")
            return 1

    # Check for write access
    try:
        # Try to open file to check for write permission
        f = open(filename_out, "wb")
        f.close()
    except IOError as ex_IO:
        mb.showinfo(" Error writing file:", "File: \n" + filename_out + "\n Error: " + str(ex_IO))
        return 1

    # Create a csv with the cleaned data frame
    df.to_csv(filename_out, encoding='utf-8', index=False)

    # Ask user whether to keep the downloaded ".tsv" file
    keep_original_files = mb.askquestion("Keep Downloaded File ?",
                                         "KEEP : " + filename + "\t\t")
    if keep_original_files == "no":
        try:
            remove(filename)
        except IOError as ex_IO:
            mb.showinfo(" Error Deleting file:", "File: \n" + filename + "\n Error: " + str(ex_IO))

    #  Function Returns
    # 1) The " cleaned " pandas dataframe
    # 2) The user appointed title
    # 3) The original file name from eurostat
    return df, user_title, original_name
