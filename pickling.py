# picking an f unpicl=kling

import pandas as pd

data = {
    "ID": [101, 102, 103],
    "Name": ["Ram", "Sita", "Hari"],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# Save DataFrame as pickle file
df.to_pickle("students.pkl")

print("\nDataFrame saved successfully!")

#unplicking
import pandas as pd

df = pd.read_pickle("students.pkl")

print("Data Loaded from Pickle File")
print(df)

#modified 
import pandas as pd

df = pd.read_pickle("students.pkl")

# Add new column
df["Result"] = ["Pass", "Pass", "Pass"]

# Save updated DataFrame
df.to_pickle("updated_students.pkl")

print(df)


## using csv and pickle together

import pandas as pd

# Read CSV
df = pd.read_csv("students.csv")

# Save as Pickle
df.to_pickle("students.pkl")

# Read Pickle
new_df = pd.read_pickle("students.pkl")

print(new_df)