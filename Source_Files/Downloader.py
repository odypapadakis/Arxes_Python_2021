# This file contains the code for downloading the csv files.

#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz

# import zipfile
# from my_importer import *


# module_name = "requests"
# import requests
# importer(module_name)

# test = __import__( module_name )




url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
try:
    response = requests.get(url, timeout=5.00)   # Expect a response within 5 seconds
except Exception as a_ex:
    print("ERROR! \n Unable to reach Website", url)
    print("-----------------------------")
    print(a_ex)                         # Return the error type
    print("-----------------------------")
    exit(0)

print("-------------- DONE -----------------------")