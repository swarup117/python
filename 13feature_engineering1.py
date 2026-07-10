#encoding technique
#label encoding 
# Label Encoding converts categories into integers.

import pandas as pd

from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    "Education": [
        "Bachelor",
        "Master",
        "PhD",
        "Bachelor",
        "High School"
    ]
})

le = LabelEncoder()

df["Education_Encoded"] = le.fit_transform(df["Education"])

print(df)

# print(le.classes_)