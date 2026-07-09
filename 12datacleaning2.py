#outlier
# An outlier is a value that is much larger 
# or much smaller than the rest of the data.

# IQR (Interquartile Range)

import pandas as pd

df = pd.DataFrame({
    "Salary": [30000, 32000, 31000, 29000, 35000, 33000, 500000]
})
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Salary"] < lower) | (df["Salary"] > upper)]

print(outliers)
