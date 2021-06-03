# This Python function
# Downloads a compressed file from eurostat,
# extracts the file from the gzip
# and saves it to disk.
#

from tkinter import messagebox as mb
import gzip
import requests
from os import path

#      list_in contains 3 items which are :
#       1) url: The url that holds the file we want
#       2) user_title: A user decided string, that will help identify the downloaded data
#       3) original_name: The original file name ( The title from eurostat)


def downloader(list_in):

    url = list_in[0]
    user_title = list_in[1]
    original_name = list_in[2]

    print("Downloading", '"', original_name, '"', ' as: "', user_title, '.tsv"')

    try:
        # Download the gz to memory
        gz_file = requests.get(url, allow_redirects=True, timeout=9.00)   # Expect a response within 9 seconds
    except requests.exceptions:
        print("ERROR! \n Unable to reach Website", url)
        # print(a_ex)                         # Return the error type
        # exit(0)
        mb.showerror("Downloader Error", "URL unreachable.\t\t\n " + "Exiting")
        return 1

    # Extract the gz to memory
    extracted_data = gzip.decompress(gz_file.content)

    # The Data in the gzip is stored as a .tsv file
    #  Create a title for file to be extracted from the user title
    filename = "Data_"+user_title+".tsv"

    # Check for existing files. If they exist, ask to overwrite.
    if path.isfile(filename):
        overwrite = mb.askquestion("File already exists", "Overwrite -> " + filename + " <- ?? ")
        if overwrite == "no":
            mb.showinfo("No Changes made ", "File-> " + filename + "<- not saved \t\t\t")
            return 1
    # If the files don't exist or we want to overwrite
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
    # 2) The title set by the user
    # 3) The original name from eurostat
    return filename, user_title, original_name
