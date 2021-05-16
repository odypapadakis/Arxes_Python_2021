import pandas as pd
import re
from os import path
from os import remove
from tkinter import messagebox as mb


def data_processor(filename,title,original_name):
    print("Processing ", filename)

    # filename = "Data_Arrivals.tsv"

    # Select years
    start_year = 2016
    end_year = 2019

    # Select countries to keep data for
    selected_countries = "EL|ES"

    # Slect visitor type to keep data for. options are (FOR|LOC|TOTAL)
    visitor_type_RE= "FOR|TOTAL"

    # Create the regular expression that holds the years to be kept in the dataframe
    selected_years = str(start_year)
    for i in range(start_year+1, end_year + 1):
        selected_years = selected_years + "|" + str(i)

    # Add the ends with character for the regex
    selected_countries_RE = selected_countries + "\Z"

    # Keep the COUNTRY column, in addition to the selected years column
    selected_years_RE = re.compile(selected_years + "|COUNTRY")

    # load the tsv into a pandas dataframe
    df = pd.read_table(filename)

    # Change the first column's name, because it has silly characters and causes problems.
    df = df.rename(columns={df.columns[0]: 'COUNTRY'})

    # --- Filter out rows of countries ---------------
    # Clear rows that do not math the coutries Regex
    df = df[(df['COUNTRY'].str.contains(selected_countries_RE, regex=True))]

    # # Apply the mask to the dataframe to filter
    # df = df[mask]

    # Clar rows that do not start with the visitor type Regex
    df = df[(df['COUNTRY'].str.match(visitor_type_RE))]

    # --- Filter out columns by year ( and keep the COUNTRY column)------
    # Filter out the columns that do not match the selected years Regex
    df = df.filter(regex=selected_years_RE, axis=1)

    # --- Rename the file to csv ---
    size = len(filename)
    filename_out = filename[:size - 4]
    filename_out = filename_out + ".csv"

    # Check for file existence and ask to write / overwrite
    if path.isfile(filename_out):
        overwrite = mb.askquestion("File already exists", "Overwrite --> " + filename_out + " <-- ?? ")
        if overwrite == "no":
            mb.showinfo("No Changes made", " Exiting\t\t")
            exit(0)
    # Check for write access
    try:
        # Try to open file to check for write permission
        f = open(filename_out, "wb")
        f.close()
    except IOError as ex_IO:
        mb.showinfo(" Error writing file:", "File: \n" + filename_out + "\n Error: " + str(ex_IO))
        return None

    # Create a csv with the cleared data frame
    df.to_csv(filename_out, encoding='utf-8', index=False)

    keep_original_files = mb.askquestion("Do you want to keep " + filename + " ?",
                                         "Selecting no will delete the above file\t\t")
    if keep_original_files == "no":
        try:
            remove(filename)
        except IOError as ex_IO:
            mb.showinfo(" Error Deleting file:", "File: \n" + filename + "\n Error: " + str(ex_IO))

    return df,title,original_name
