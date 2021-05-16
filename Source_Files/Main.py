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
from charts import *

import tkinter as tk
from tkinter import messagebox as mb

# The list below contains the url for each file we want to download, and a name to be appended to the file
URL_list = [
            [
                "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
                ,
                "Nights"
            ]
            ,
            [
                "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00174.tsv.gz"
                ,
                "Arrivals"
            ]
           ]


# Initialize tkInter
root = tk.Tk()
# root.withdraw()

# Tkinter window miscellaneous stuff
root.iconbitmap("../Images/favicon.ico")
root.title("Αρχές Γλωσσών Python 2021")
root.geometry("600x300+650+400")  # Width x Height + Padding left + Padding top

# Ask for a location to download the data
# directory_change()

# List of downloaded files, will be fed to the downloader
# Holds lists with 2 items, filename and name
dl_files = []

# Holds datafranes of cleaned files and names. Will be fed to the chart creator
cleaned_files = []

#------------------  DEBUG---------------
dl_files.append(['Data_Arrivals.tsv','Arrivals'])
dl_files.append(['Data_Nights.tsv','Nights'])


# Feed the downloader with: 1)the url for each file 2)a string to append to each file
# for i in range(len(URL_list)):
#     dl_files.append (downloader(URL_list[i][0],URL_list[i][1]))
#


for i in range(len(dl_files)):
    cleaned_files.append(data_processor(dl_files[i][0],dl_files[i][1]))



# print(cleaned_files)

# draw_charts(cleaned_files)

# db_stuff()





mb.showinfo("Job done", "Great Success!\t\t")
