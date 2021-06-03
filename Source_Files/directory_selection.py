
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb

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
