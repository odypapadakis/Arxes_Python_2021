# This file contains the code for downloading the csv files.

#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz


import gzip
import requests


url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"
try:
    response = requests.get(url, timeout=5.00)   # Expect a response within 5 seconds
except Exception as a_ex:
    print("ERROR! \n Unable to reach Website", url)
    print(a_ex)                         # Return the error type
    exit(0)

file = requests.get(url, allow_redirects=True)
open("Data" + ".tsv.gz", "wb").write(file.content)

