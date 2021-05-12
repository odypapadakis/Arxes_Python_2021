import os

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb
from tkinter import *


def directory_change():




    current_directory = os.getcwd()

    dir_change = mb.askquestion("Directory selection", "Current directory is :\n" + str(current_directory) + "\nChange Directory ?" )

    if dir_change == 'yes':
        requested_directory = tk.filedialog.askdirectory()
        if( requested_directory ):
            os.chdir(requested_directory)
        else:
            mb.showerror("Error", "No directory selected\n " + "Exiting")
            exit(0)
    else:
        pass

