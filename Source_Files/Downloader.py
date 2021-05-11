# This file contains the code for downloading the csv files.

#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz

import os
import zipfile
import requests

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
from tkinter import *


root = Tk()
root.withdraw()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

current_directory = os.getcwd()
dir_change = mb.askquestion("Change directory ?", "Current directory is  " + str(current_directory) )

# print(dir_change)

if(dir_change == "yes") :
    requested_directory = filedialog.askdirectory()
    os.chdir(requested_directory)

f= open("guru99.txt","w+")
for i in range(10):
     f.write("This is line %d\n" % (i+1))
f.close()




url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
try:
    response = requests.get(url, timeout=5.00)   # Expect a response within 5 seconds
except Exception as a_ex:
    print("ERROR! \n Unable to reach Website", url)
    print(a_ex)                         # Return the error type
    exit(0)

print("-------------- DONE -----------------------")