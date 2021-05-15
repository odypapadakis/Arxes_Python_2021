import pandas as pd
import re
filename = "Data_Arrivals.tsv"

print("Data processor working on: " + filename)

# load the tsv into a pandas dataframe
df = pd.read_table(filename)

print(df)

print("---------------------------------------------")

selected_countries_RE = "EL|ES|AT\Z"

#In the dataframe df, return true if the RE:Selected_countries_RE is true
mask = (df['c_resid,unit,nace_r2,geo\\time'].str.contains(selected_countries_RE,regex = True))

# Apply the mask to the dataframe to filter
df = df[mask]
print(df)
selected_years_RE = "2016|2017|2018|2019"
# mask = df[selected_years_RE]
# df.drop(selected_years_RE, inplace=True, axis=1)
# df = df[df.columns.drop(list(df.filter(regex=selected_years_RE)))]
# df.find(list(df.filter(regex = selected_years_RE)), axis = 1, inplace = True)
print("++++++++++++++++++++++++++++++++++++++++++++++")
# df = df[[2018,2019]]
df = df.filter(regex=selected_years_RE, axis=1)
print(df)


