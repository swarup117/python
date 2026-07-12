#target encoding
# Target Encoding replaces each category with the average value
# of the target variable for that category

import pandas as pd

df = pd.DataFrame({
    "City": [
        "Kathmandu",
        "Pokhara",
        "Kathmandu",
        "Butwal",
        "Pokhara",
        "Kathmandu"
    ],
    "Purchased": [1,0,1,0,1,0]
})
target_mean = df.groupby("City")["Purchased"].mean()
#it make group od categories and the calculate the mean
print(target_mean)

df["City_TE"] = df["City"].map(target_mean)

print(df)

##data leckage is the problem
