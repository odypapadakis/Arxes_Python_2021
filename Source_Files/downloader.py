# This Python function
# Downloads a compressed file from eurostat,
# extracts the file from the gzip
# and saves it to disk.
#
#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz
#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00174.tsv.gz

import tkinter as tk
from tkinter import messagebox as mb
import gzip
import requests
from os import path

#      The 3 inputs are:
#       1) url: The url that has the file we need
#       2) user_title: A user decided string, that will help identify the downloaded data
#       3) original_name: The original file name


def downloader(url, user_title,original_name):


    print("Downloading" , original_name, " as: " , user_title )
    try:
        requests.get(url, timeout=9.00)   # Expect a response within 9 seconds
    except requests.exceptions:
        # print("ERROR! \n Unable to reach Website", url)
        # print(a_ex)                         # Return the error type
        # exit(0)
        mb.showerror("Downloader Error", "URL unreachable.\t\t\n " + "Exiting")
        return 1

    # Download the gz to memory
    gz_file = requests.get(url, allow_redirects=True)

    # Extract the gz to memory
    extracted_data = gzip.decompress(gz_file.content)

    # The Data in the gzip is stored as a .tsv file
    #  Create a title for file to be extracted from the user title
    filename = "Data_"+user_title+".tsv"

    # tkinter stuff
    root = tk.Tk()
    root.withdraw()

    # Check for existing files. If they exist, ask to overwrite.
    if (path.isfile(filename)):
        overwrite = mb.askquestion("File already exists", "Overwrite -> " + filename + " <- ?? ")
        if (overwrite == "no"):
            mb.showinfo("No Changes made ","File-> " + filename + "<- not saved \t\t\t")
            return None
    # If the files don't exist
    try:
        # Write the files to disk
        f = open(filename, "wb")
        f.write(extracted_data)
        f.close()
    except IOError as ex_IO:
        mb.showinfo(" Problem writing file:", filename + "\n Error: " + str(ex_IO))
        return None

    # Return
    # 1) the filename of the .tsv file on the disk
    # 2,3)  the data that was given to the function
    return (filename, user_title, original_name)
