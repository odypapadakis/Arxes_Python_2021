# This is a program that downloads some  data from eurostat.
# It cleans it up
# Saves it as csv files
# Creates some charts
# And stores it into a mysql database
# Created by Odysseas papadakis
# papadako@ceid.upatras.gr
# AM: 104115
# 2021


import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog
import pandas as pd
import numpy as np
import gzip
import requests
from os import path
from os import remove
import os
import re

#  Use this !!!
#  pip install mysql-connector-python
import mysql.connector

#    _______________________________
#   |   Main code is at line 437    |
#   |_______________________________|

# ------------------------------   DIRECTORY SELECTOR -----------------------------------------------------------
# This Function asks the user to specify a directory to store the files.


def directory_change():

    # Get the current directory
    current_directory = os.getcwd()

    # Do you want to change directory ?
    dir_change = mb.askquestion("Directory selection", "Current directory is :\n" +
                                str(current_directory) +
                                "\n Change Directory ? ")

    if dir_change == 'yes':
        requested_directory = tk.filedialog.askdirectory()

        # If the user selects a directory
        if requested_directory:
            # Change to that directory
            os.chdir(requested_directory)

        # If the user presses the escape button or closes the directory selection window
        else:
            mb.showerror("DIRECTORY ERROR", "No directory selected. \n " + "Exiting...")
            exit(0)

# This Python function
# Downloads a compressed file from eurostat,
# extracts the file from the gzip
# and saves it to disk.

# ------------------------------   DOWNLOADER -----------------------------------------------------------
#      list_in contains 3 items which are :
#       1) url: The url that holds the file we want
#       2) user_title: A user decided string, that will help identify the downloaded data
#       3) original_name: The original file name ( The title from eurostat)


def downloader(list_in):

    url = list_in[0]
    user_title = list_in[1]
    original_name = list_in[2]

    print("Downloading", '"', original_name, '"', ' as: "', user_title, '.tsv"')

    try:
        # Download the gz to memory
        gz_file = requests.get(url, allow_redirects=True, timeout=9.00)   # Expect a response within 9 seconds
    except requests.exceptions:
        print("ERROR! \n Unable to reach Website", url)
        # print(a_ex)                         # Return the error type
        # exit(0)
        mb.showerror("Downloader Error", "URL unreachable.\t\t\n " + "Exiting")
        return 1

    # Extract the gz to memory
    extracted_data = gzip.decompress(gz_file.content)

    # The Data in the gzip is stored as a .tsv file
    #  Create a title for file to be extracted from the user title
    filename = "Data_"+user_title+".tsv"

    # Check for existing files. If they exist, ask to overwrite.
    if path.isfile(filename):
        overwrite = mb.askquestion("File already exists", "Overwrite -> " + filename + " <- ?? ")
        if overwrite == "no":
            mb.showinfo("No Changes made ", "File-> " + filename + "<- not saved \t\t\t")
            return 1
    # If the files don't exist or we want to overwrite
    try:
        # Write the files to disk
        f = open(filename, "wb")
        f.write(extracted_data)
        f.close()
    except IOError as ex_IO:
        mb.showinfo(" Problem writing file:", filename + "\n Error: " + str(ex_IO))
        return None

    # Return
    # 1) the filename of the .tsv file on the disk
    # 2) The title set by the user
    # 3) The original name from eurostat
    return filename, user_title, original_name

# ------------------------------   DATA PROCESSOR  -----------------------------------------------------------

# This function "Cleans" the data to keep just the years / countries / type of visitor we want.
# In this instance we will keep the data for:
# Countries: Greece , Spain
# Years : 2016,2017,2018,2019
# Types of visitors: Foreigners and Total.
# It also stores the cleaned data in a csv file.

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

# -----------------------------------  DATABASE STORAGE-----------------------------------------------------

# This function creates mySQL database from the input data
# This function requires a MySQL database to be up and running.

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
        # print(sql)
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

# -------------------------------- CHART CREATOR --------------------------------------------------------

# This function takes 4 inputs:
# 1) A list that contains:
#   1.1) a pandas dataframe
#   1.2) The user title
#   1.3) The original file name to be used as the subplot title
# 2) The number of the subplot
# 3) The list of country codes
# 4) The list of country names


def make_charts_2(list_in, subplot_number, country_code, country_name):

    # There will be 4 plots, in a 2 x 2  grid
    plot = plt.subplot(2, 2, subplot_number)

    # Set the plot title as the original file name
    plot_title = list_in[2]

    # Set the title of the subplot
    plot.set_title(plot_title + "\n" + country_name, fontsize=14)

    # set the subplot background color for better readability
    plot.set_facecolor("gainsboro")

    # Set the label for the y axis
    plot.set_ylabel('People', fontsize=14)

    # Set the label for the x axis
    plot.set_xlabel('YEAR', fontsize=14)

    # Get the dataframe from the list
    df = list_in[0]

    # Get the names of all the columns into a list
    # ( will be used to title each bar for the bar plot )
    years = df.columns.tolist()
    # drop the first column  from the list
    years.pop(0)

    # Return evenly spaced values based on the length of the list supplied
    # example: For 4 years, x will be [ 0 1 2 3]
    x = np.arange(len(years))  # the label locations

    # Place  ticks(labels) on the x axis, on the evenly spaced values
    plot.set_xticks(x)

    # Source for labels text  to attach to each tick is the years
    plot.set_xticklabels(years)

    # -------------   Code to keep the correct country rows  -------------

    # Keep only the rows that have the country column ends with  the country code we want
    # example : keep only the rows in which the country column ends with 'EL'
    df1 = df[(df['COUNTRY'].str.endswith(country_code))]

    # -------------   Code to keep the  number of Foreign visitors -------------

    # Keep only the row that have the country column BEGIN with FOR
    # To keep the foreigners = non residents
    data_foreign = df1[(df1['COUNTRY'].str.startswith('FOR'))]
    # Convert the  dataframe into a list of lists
    data_foreign = data_foreign.values.tolist()
    #  Keep the only item of the list
    data_foreign = data_foreign[0]
    # Delete the first item of the list, which is the country code and data type ( FOR|TOTAL)
    data_foreign.pop(0)
    # Make the list of strings into a list of integers
    data_foreign = [int(i) for i in data_foreign]

    # -------------   Code to keep the total number of visitors -------------

    # Keep in a dataframe only the row that has the country column that begins with TOTAL
    # To keep the total number of visitors
    data_total = df1[(df1['COUNTRY'].str.startswith('TOTAL'))]
    # Convert the  dataframe into a list of lists
    data_total = data_total.values.tolist()
    #  Keep the only item of the list
    data_total = data_total[0]
    # Delete the first item of the list, which is the country code and data type ( FOR|TOTAL)
    data_total.pop(0)
    # Make the list of strings into a list of integers
    data_total = [int(i) for i in data_total]

    width = 0.3  # the width of the bars of the plot

    # The two bars are created
    rect1 = plot.bar(x - width / 2, data_foreign, width, label='Non Residents')
    rect2 = plot.bar(x + width / 2, data_total, width, label='Total')

    #  The labels for the two bars are created
    plot.bar_label(rect1, padding=5, fmt="%d", color='#1f77b4', backgroundcolor='0.8', rotation=10, size=9)
    plot.bar_label(rect2, padding=5, fmt='%d', color='#ff7f0e', backgroundcolor='0.8', rotation=10, size=9)

    # Create the formatting for the vertical axis
    # This code was taken from stackoverflow
    # https://stackoverflow.com/questions/40511476/how-to-properly-use-funcformatterfunc
    def millions(x, pos):
        return '%1.1fM' % (x * 1e-6)
    # Create the formatting for the vertical axis
    formatter = FuncFormatter(millions)

    # Set the formatting for the vertical axis
    plot.get_yaxis().set_major_formatter(formatter)

    # Show a legend
    plot.legend()


# This function takes as input
# 1) A list of lists, each list consists of 3 items
#   1.1) A pandas data frame
#   1.2)  The user appointed name
#   1.3) The original name of the tsv file
# 2) The number of the subplot to be created
# 3) A list of country codes ['EL', 'ES']
# 4) A list of country names ['Greece', 'Spain']


def make_charts(in_list, country_codes, country_names):

    nigths_list = in_list[0]
    arrivals_list = in_list[1]

    make_charts_2(nigths_list,     1, country_codes[0], country_names[0])
    make_charts_2(nigths_list,     3, country_codes[1], country_names[1])
    make_charts_2(arrivals_list,   2, country_codes[0], country_names[0])
    make_charts_2(arrivals_list,   4, country_codes[1], country_names[1])

    plt.show()

# ------------------------------   MAIN CODE  -----------------------------------------------------------

# The list "URL_list"  contains  lists that have 3  items each :
# 1) The url for each file we want to download
# 2) A name created by the user to easily distinguish the file
# 3) The original file name from eurostat
#  This list will be passed to the downloader function, to download the data.


URL_list = [
            # list 1
            [
                "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
                ,
                "Nights"
                ,
                "Nights spent at tourist accommodation establishments by residents/non-residents"
            ]
            ,
            # list 2
            [
                "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00174.tsv.gz"
                ,
                "Arrivals"
                ,
                "Arrivals of residents/non-residents at tourist accommodation establishments"
            ]
           ]

# Initialize tkInter
root = tk.Tk()
# root.withdraw()

# Tkinter window miscellaneous options
# root.iconbitmap("../Images/favicon.ico")
root.title("Αρχές Γλωσσών Python 2021")
root.geometry("600x300+650+400")  # Width x Height + Padding left + Padding top

# Ask for a location to download the data into
directory_change()

# The list "downloaded_files" contains information about the files that the downloader has downloaded
# It Holds lists, that have 3 items each:
# 1) The filename of the .tsv file that was downloaded
# 3) The user created title
# 2) The original filename from the website
downloaded_files = []

print("-------  DOWNLOADING -------")
for i in range(len(URL_list)):
    # Feed each item of the URL list to the downloader
    temp = downloader(URL_list[i])
    if temp is not None:
        downloaded_files.append(temp)

# IF no files have been downloaded, abort
if not downloaded_files:
    print("No Data Downloaded, Exiting....")
    mb.showerror("No Data Downloaded", "No Data. \n " + "Exiting...")
    exit(0)

# Ask user whether to continue with processing the data
continue_after_download = mb.askquestion("Continue to data processing ?",
                                         "You can stop here and just keep the downloaded files."  "\t\t")
if continue_after_download == "no":
    exit(0)

# The list "cleaned_files" contains the cleaned pandas dataframes + additional info
# Holds lists that have 3 items :
# 1) pandas dataframe that has been " cleaned "
# 2) The user created title
# 3) The original filename from the website
cleaned_files = []

print("-------  PROCESSING DATA    -------")
for i in range(len(downloaded_files)):
    cleaned_files.append(data_processor(downloaded_files[i]))

if not cleaned_files:
    print("No Data, Exiting....")
    mb.showerror("No Data", "No Data. \n " + "Exiting...")
    exit(0)

print("-------  STORING TO DATABASE    -------")
db_store(cleaned_files)


#  The list of country codes the data will be plotted for
# global country_code
country_codes = ['EL', 'ES']

# The equivalent names for the above country codes
# global country_name
country_names = ['Greece', 'Spain']

print("-------  MAKING CHARTS    -------")
make_charts(cleaned_files, country_codes, country_names)

mb.showinfo("Done!\t\t")
