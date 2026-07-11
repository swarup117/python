# frequency Encoding 
# it replaces each category with how many times it appears in the dataset.

import pandas as pd

df = pd.DataFrame({
    "Department": [
        "HR",
        "IT",
        "Finance",
        "IT",
        "HR",
        "IT",
        "Sales"
    ],
    # "counted": [1,0,1,0,1,0,1] # use if we have to display this also 
})

freq = df["Department"].value_counts()

df["Department_FE"] = df["Department"].map(freq)

print(df)