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

#      The inputs are:
#       url: The url that has the file we need
#       user_title: A user decided string, that will help identify the downloaded data
#       original_name: The original file name


def downloader(url, user_title,original_name):

    # url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
    print("Downloading" , original_name, " as: " , user_title )
    try:
        requests.get(url, timeout=9.00)   # Expect a response within 9 seconds
    except requests.exceptions:
        # print("ERROR! \n Unable to reach Website", url)
        # print(a_ex)                         # Return the error type
        # exit(0)
        mb.showerror("Downloader Error", "URL unreachable.\t\t\n " + "Exiting")
        exit(0)

    # Download the gz to memory
    gz_file = requests.get(url, allow_redirects=True)

    # Extract the gz to memory
    extracted_data = gzip.decompress(gz_file.content)

    #  Create a title for the downloaded file based on the string the function received
    filename = "Data_"+user_title+".tsv"

    # tkinter stuff
    root = tk.Tk()
    root.withdraw()

    # Check if files with the same name exists. If it does, ask to overwrite or quit.
    if (path.isfile(filename)):
        overwrite = mb.askquestion("File already exists", "Overwrite -> " + filename + " <- ?? ")
        if (overwrite == "no"):
            mb.showinfo("No Changes made ","File-> " + filename + "<- not saved \t\t\t")
            # exit(0)
            return None
    try:
        # Write the files to disk
        f = open(filename, "wb")
        f.write(extracted_data)
        f.close()
    except IOError as ex_IO:
        mb.showinfo(" Problem writing file:", filename + "\n Error: " + str(ex_IO))
        # exit(0)
        return None

    # Return the filename on the disk  and the data that was given to the function
    return (filename, user_title, original_name)
