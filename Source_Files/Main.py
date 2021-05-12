from directory_selection import *
from downloader import *
import tkinter as tk
from tkinter import messagebox as mb

root = tk.Tk()
# root.withdraw()

root.iconbitmap("../Images/favicon.ico")
root.title("Ody's Downloader")
root.geometry("600x300+650+400") #Width x Height


directory_change()
downloader()



# extractor()


mb.showinfo("Job done", "Great Success!\t\t")