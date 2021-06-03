# This is a program that downloads data from eurostat.
# It cleans it up
# Saves it as csv files
# Creates some charts
# And stores it into a mysql database
# Created by Odysseas papadakis

from directory_selection import *
from downloader import *
from data_processor import *
from db_store import *
from make_charts import *
from make_charts_v2 import *

import tkinter as tk
from tkinter import messagebox as mb

# The list "URL_list" below contains 2 lists that have 3  items:
# 1) The url for each file we want to download
# 2) A name to created by the user to easily distinguish the files
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
root.iconbitmap("../Images/favicon.ico")
root.title("Αρχές Γλωσσών Python 2021")
root.geometry("600x300+650+400")  # Width x Height + Padding left + Padding top

# Ask for a location to download the data into
directory_change()


# The list "downloaded_files" contains information about the files that the downloader has downloaded
# Holds lists, that have 3 items:
# 1) The filename of the .tsv file that was downloaded
# 3) The user created title
# 2) The original filename from the website
downloaded_files = []

# #------------------  DEBUG---------------
# downloaded_files.append(['Data_Arrivals.tsv','Arrivals',
# 'Arrivals of residents/non-residents at tourist accommodation establishments'])
# downloaded_files.append(['Data_Nights.tsv','Nights',
# 'Nights spent at tourist accommodation establishments by residents/non-residents'])

print("-------  DOWNLOADING -------")
for i in range(len(URL_list)):
    # Feed each item of the URL list to the downloader
    temp = downloader(URL_list[i])
    if temp is not None:
        downloaded_files.append(temp)


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
country_code = ['EL', 'ES']

# The equivalent names for the above country codes
# global country_name
country_name = ['Greece', 'Spain']


print("-------  MAKING CHARTS    -------")
make_charts(cleaned_files,country_code,country_name)

mb.showinfo("Done!\t\t")
