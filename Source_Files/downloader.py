# This Python files Downloads a file from eurostat.
# It also extracts the file from the gzip.
#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz
import tkinter as tk
from tkinter import messagebox as mb
import gzip
import requests
import os.path
from os import path

def downloader():

    url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"

    try:
        response = requests.get(url, timeout=9.00)   # Expect a response within 9 seconds
    except Exception as a_ex:
        # print("ERROR! \n Unable to reach Website", url)
        # print(a_ex)                         # Return the error type
        # exit(0)
        mb.showerror("Downloader Error", "URL unreachable.\t\t\n " + "Exiting")
        exit(0)

    # Download the content of the gz to memory
    gz_data = requests.get(url, allow_redirects=True)

    # Extract the gz to memory
    extracted_data = gzip.decompress(gz_data.content)

    filename = "Data.tsv"


    root = tk.Tk()
    root.withdraw()

    if (  path.isfile(filename)    ):
        overwrite = mb.askquestion("File already extists","Overwrite --> " + filename + " <-- ?? " )
        if (overwrite == "no"):
            mb.showinfo("No Changes made", " Exiting\t\t")
            exit(0)


    # Write the data to disk, in the file named filename
    f = open(filename, "wb")
    f.write(extracted_data)
    f.close()
