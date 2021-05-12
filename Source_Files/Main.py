from directory_selection import *
from downloader import *
from data_processor import *
from db_store import *

import tkinter as tk
from tkinter import messagebox as mb


# Initialize tkInter
root = tk.Tk()
# root.withdraw()

root.iconbitmap("../Images/favicon.ico")
root.title("Ody's Downloader")
root.geometry("600x300+650+400")  # Width x Height + Padding left + Padding top

# directory_change()

# downloader()

#
# extractor()
db_stuff()
mb.showinfo("Job done", "Great Success!\t\t")
