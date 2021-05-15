import pandas as pd
import re
filename = "Data_Arrivals.tsv"

print("Data processor working on: " + filename)

# load the tsv into a pandas dataframe
df = pd.read_table(filename)

print(df)

print("---------------------------------------------")

Selected_countries_RE = "(EL|ES|AT)"


mask = (df['c_resid,unit,nace_r2,geo\\time'].str.contains(Selected_countries_RE))

print("Mask is: \n",mask)
df = df[mask]

print(df)


