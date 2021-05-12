from directory_selection import *
from downloader import *
from data_processor import *
from db_store import *
from charts import *

import tkinter as tk
from tkinter import messagebox as mb




URL_list =[
    ["https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz","Nights"]
    ,
    ["https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00174.tsv.gz","Arrivals"]
    ]
print("aaaaaaaaaaaaaaaaa")

# Initialize tkInter
root = tk.Tk()
# root.withdraw()

root.iconbitmap("../Images/favicon.ico")
root.title("Ody's Downloader")
root.geometry("600x300+650+400")  # Width x Height + Padding left + Padding top

directory_change()


for i in range(len(URL_list)):
    downloader(URL_list[i][0],URL_list[i][1])

# db_stuff()
# draw_charts()
# data_processor()


mb.showinfo("Job done", "Great Success!\t\t")
