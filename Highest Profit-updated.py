import pandas as pd
import json
import numpy as np

# Read into memory
df = pd.read_csv("data.csv")
df.head()

# Print # of rows in the CSV data.
print(df.shape[0])

#Profit column should be a float like Revenue
#change object -> numeric
#Using errors="coerce". It will replace all non-numeric values with NaN.
df["Profit (in millions)"] = pd.to_numeric(df["Profit (in millions)"], errors='coerce')

#Remove all rows with 'profit' that is not numerical value.
df2 = df.dropna()

#Then print out how many rows of data are left, after removing all the rows with 
#invalid non-numeric profit column data
print(df2.shape[0])

json_str = df2.to_json(orient="records")
json_arr = json.loads(json_str)

# write to file
with open("data2.json", "w") as outfile:
    json.dump(json_str, outfile)

json_arr.sort(key=lambda x: x["Profit (in millions)"], reverse = True)
print(json_arr[:20])