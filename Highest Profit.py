import pandas as pd
import json

# Read into memory
df = pd.read_csv("data.csv")
df.head()

# Print # of rows in the CSV data.
print(df.shape[0])

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

#Remove all rows with 'profit' that is not numerical value.

df[pd.to_numeric(df["Profit (in millions)"], errors="coerce").notnull()]

df1 = df[pd.to_numeric(df["Profit (in millions)"], errors="coerce").notnull()]
pd.concat([df1,df]).drop_duplicates(keep=False)

#Then print out how many rows of data are left, after removing all the rows with 
#invalid non-numeric profit column data
print(df1.shape[0])

json_str = df1.to_json(orient="records")
json_arr = json.loads(json_str)

# write to file
with open("data2.json", "w") as outfile:
    json.dump(json_str, outfile)

json_arr.sort(key=lambda x: x["Profit (in millions)"], reverse = True)
print(json_arr[:20])