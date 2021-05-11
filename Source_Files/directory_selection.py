import os

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
from tkinter import *


def directory_change():


    root = tk.Tk()
    root.withdraw()

    # canvas1 = tk.Canvas(root, width = 300, height = 300)
    # canvas1.pack()

    current_directory = os.getcwd()

    dir_change = mb.askquestion("Change directory ?", "Current directory is  " + str(current_directory) )

    if dir_change == 'yes':
        requested_directory = tk.filedialog.askdirectory()
        if( requested_directory ):
            os.chdir(requested_directory)
        else:
            mb.showerror("Error", "No directory selected\n " + "Exiting")
            exit(0)


    # elif (dir_change == "no") :
    #     pass
    # else:
    #     exit(1)

    # f= open("asdf.txt","w+")
    # for i in range(10):
    #      f.write("This is line %d\n" % (i+1))
    # f.close()
    #