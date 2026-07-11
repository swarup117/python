#Ordinal encoding
# Ordinal Encoding is a feature engineering technique used to convertcategorical
# data into numbers when the categories have a meaningfulorder or ranking.

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.DataFrame({
    "Size":  ["Medium","Small", "Large", "Medium", "Small"]
})

encoder = OrdinalEncoder(
    categories=[["Small", "Medium", "Large"]]
)

df["Encoded"] = encoder.fit_transform(df[["Size"]])

print(df)

## more then one categories

df1 = pd.DataFrame({
    "Size": ["Medium", "Small","Large" ,"Small", "Medium"],
    "Education": [ "Master", "Bachelor","Master","High School","Bachelor"]
})

encoder1 = OrdinalEncoder(categories=[
    ["Small", "Medium", "Large"],
    ["High School", "Bachelor", "Master"]
])

df1[["Size", "Education"]] = encoder1.fit_transform(
    df1[["Size", "Education"]]
)

print(df1)