import pandas as pd

df = pd.DataFrame({
    "Name": ["Ram", "Sita", "Hari", "Gita"],
    "Age": [22, None, 28, 100],
    "Salary": [25000, 30000, None, 35000],
    "City": ["ktm", "pkh" ,None ,"ktm"]
})

print(df)

print(df.dropna())

#fillna  insted of drop
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

df["Age"] = df["Age"].fillna(df["Age"].median())
print(df)

df["City"] = df["City"].fillna(df["City"].mode()[0])
print(df)


# incorrecrt data type 


df1 = pd.DataFrame({
    "Age": ["22", "25", "30"]
})
print(df1.dtypes)

#here the datatype is object(str) so cannot calculate mean
# df["Age"].mean()  --> error

df1["Age"] = df1["Age"].astype(int)
print(df1.dtypes)
print(df1["Age"].mean())

# next error
df3 = pd.DataFrame({
    "Age": ["22", "25", "Thirty", "30"]
})
# df3=df3["Age"].astype(int) # it will throw --> error
df3["Age"] = pd.to_numeric(df3["Age"], errors="coerce")
print(df3)


## professional way to do EDA
# # 1. Check the data
# df.head()

# # 2. Check data types
# df.info()

# # 3. Find missing values
# df.isnull().sum()

# # 4. Correct incorrect data types
# df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
# df["Date"] = pd.to_datetime(df["Date"])

# # 5. Handle missing values created during conversion
# df["Age"] = df["Age"].fillna(df["Age"].median())