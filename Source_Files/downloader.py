# This Python script
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


def downloader(url, title):

    # url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"

    try:
        requests.get(url, timeout=9.00)   # Expect a response within 9 seconds
    except Exception:
        # print("ERROR! \n Unable to reach Website", url)
        # print(a_ex)                         # Return the error type
        # exit(0)
        mb.showerror("Downloader Error", "URL unreachable.\t\t\n " + "Exiting")
        exit(0)

    # Download the gz to memory
    gz_file = requests.get(url, allow_redirects=True)

    # Extract the gz to memory
    extracted_data = gzip.decompress(gz_file.content)

    filename = "Data_"+title+".tsv"

    root = tk.Tk()
    root.withdraw()

    if (path.isfile(filename)):
        overwrite = mb.askquestion("File already exists", "Overwrite --> " + filename + " <-- ?? ")
        if (overwrite == "no"):
            mb.showinfo("No Changes made", " Exiting\t\t")
            exit(0)

    # Write the data to the disk
    f = open(filename, "wb")
    f.write(extracted_data)
    f.close()
