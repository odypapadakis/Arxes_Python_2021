# This file contains the code for downloading the csv files.

#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz


import zipfile
import requests
from directory_selection import *

directory_change()


mb.showinfo("Download Completed", "  Success!\t\t")






# url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
# try:
#     response = requests.get(url, timeout=5.00)   # Expect a response within 5 seconds
# except Exception as a_ex:
#     print("ERROR! \n Unable to reach Website", url)
#     print(a_ex)                         # Return the error type
#     exit(0)
#
# print("-------------- DONE -----------------------")