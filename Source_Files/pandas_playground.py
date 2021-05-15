import pandas as pd
import re
filename = "Data_Arrivals.tsv"

# Below the selection of countries and years happens
selected_years = "2016|2017|2018|2019"
selected_countries = "EL|ES"

# The regular expressions for the selections are completed
selected_countries_RE = selected_countries + "\Z"
selected_years_RE = re.compile(selected_years + "|COUNTRY")

# load the tsv into a pandas dataframe
df = pd.read_table(filename)

# Change the first column name, because it has silly characters and causes problems
df = df.rename(columns={df.columns[0]: 'COUNTRY'})

#In the dataframe df, return true if the RE:Selected_countries_RE is true
mask = (df['COUNTRY'].str.contains(selected_countries_RE,regex = True))

# Apply the mask to the dataframe to filter
df = df[mask]

# Filter out the columns that do not match the selected years
df = df.filter(regex=selected_years_RE, axis=1)

print(df)

