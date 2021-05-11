# This file contains the code for downloading the csv files.

#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox as mb

import gzip
import requests

def downloader():
    url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
    try:
        response = requests.get(url, timeout=5.00)   # Expect a response within 5 seconds
    except Exception as a_ex:
        # print("ERROR! \n Unable to reach Website", url)
        # print(a_ex)                         # Return the error type
        # exit(0)
        mb.showerror("Downloader Error", "URL unreachable.\t\t\n " + "Exiting")
        exit(0)

    file = requests.get(url, allow_redirects=True)
    gz_filename = "Data" + ".tsv.gz"
    open(gz_filename, "wb").write(file.content)

    filename = "Data.tsv"
    with gzip.open(gz_filename,'rb') as f:
        gz_content = f.read()
    # file = gzip.decompress(gz_filename)
    # open(filename, "wb").write(gz_content.content)
    filename.write()
    #https: // svaderia.github.io / articles / downloading - and -unzipping - a - zipfile /