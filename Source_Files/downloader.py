# This Python function
# Downloads a compressed file from eurostat,
# extracts the file from the gzip
# and saves it to disk.
#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz
#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00174.tsv.gz

import tkinter as tk
from tkinter import messagebox as mb
import gzip
import requests
from os import path


def downloader(url, title,original_name):

    # url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
    print("Downloading" , title )
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
    filename = "Data_"+title+".tsv"

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

    return (filename, title, original_name)
