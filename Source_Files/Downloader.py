# This file contains the code for downloading the csv files.

#  https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz

import zipfile


try:
    import requests
except Exception as e:
    print("Error! importing module!!")
    print(e)
    exit(0)


Folder_Name = "Statistics_Downloads"
url = "https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/tin00175.tsv.gz"

try:
    response = requests.get(url, timeout=15.00)   # Expect a response within 15 seconds
except Exception as a_ex:
    print("ERROR! \n Unable to reach Website", url)
    print(a_ex)                         # Return the error type
    exit(0)


path_to_zipfile = ""
path_to_extracted_zipfile = ""