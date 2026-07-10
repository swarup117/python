# # Feature Engineering
# # Feature Engineering is the process of creating new features (columns) from 
# # existing data to help a machine learning model learn better.

import pandas as pd

df = pd.DataFrame({
    "Math": [80, 75, 90],
    "Science": [70, 85, 95]
})

print(df)

#adding new column
df["Total"] = df["Math"] + df["Science"]
print(df)

df["Average"] = (df["Math"] + df["Science"]) / 2
print(df)

#feature extraction


df = pd.DataFrame({
    "Purchase_Date": [
        "2025-01-15",
        "2025-07-20",
        "2025-12-25"
    ]
})

#here pandas understand data and time 
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])
print(df.dtypes)

df["Year"] = df["Purchase_Date"].dt.year
print(df["Year"])

df["Month"] = df["Purchase_Date"].dt.month
print(df["Month"])

df["Day"] = df["Purchase_Date"].dt.day
print(df["Day"])

df["Weekday"] = df["Purchase_Date"].dt.day_name()
print(df["Weekday"])


# binding 
# cover the numerical data in categoies

# Manual(cut)
df = pd.DataFrame({
    "Age": [18, 22, 25, 31, 45, 67]
})
df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 20, 40, 60, 100],
    labels=["Teen", "Adult", "Middle Age", "Senior"]
)

print(df)

#qcut
df = pd.DataFrame({
    "Salary":[20000,35000,50000,70000,100000]
})

df["Group"] = pd.qcut(
    df["Salary"],
    q=4,
    labels=["Q1","Q2","Q3","Q4"]
)
print(df)
