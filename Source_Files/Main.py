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

import tkinter as tk
from tkinter import messagebox as mb

# The list below contains the url for each file we want to download,name to be appended to the file and The original name
URL_list = [
            [
                "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
                ,
                "Nights"
                ,
                "Nights spent at tourist accommodation establishments by residents/non-residents"
            ]
            ,
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

# List of downloaded files, will be fed to the downloader
# Holds lists with 2 items, filename  and name
dl_files = []

# Holds datafranes of cleaned files and names. Will be fed to the chart creator and the database creator
cleaned_files = []

# #------------------  DEBUG---------------
# dl_files.append(['Data_Arrivals.tsv','Arrivals',
# 'Arrivals of residents/non-residents at tourist accommodation establishments'])
# dl_files.append(['Data_Nights.tsv','Nights',
# 'Nights spent at tourist accommodation establishments by residents/non-residents'])

print("-------  DOWNLOADING -------")
for i in range(len(URL_list)):
    temp = downloader(URL_list[i][0], URL_list[i][1], URL_list[i][2])
    if temp is not None:
        dl_files.append(temp)


print("-------  PROCESSING DATA    -------")
for i in range(len(dl_files)):
    cleaned_files.append(data_processor(dl_files[i][0], dl_files[i][1], dl_files[i][2]))

print("-------  STORING TO DATABASE    -------")
db_stuff(cleaned_files)

print("-------  MAKING CHARTS    -------")
make_charts(cleaned_files)

mb.showinfo("Done!\t\t")
