#mutual information
#Mutual Information (MI) measures how much information one variable provides about 
#another,regardless of whether the relationship is linear or nonlinear.

import pandas as pd
from sklearn.feature_selection import mutual_info_classif

df = pd.DataFrame({
    "Age": [22,25,30,35,40,45],
    "Salary": [25000,30000,45000,60000,80000,100000],
    "Experience": [1,2,4,6,8,10],
    "Purchased": [0,0,0,1,1,1]
})

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

scores = mutual_info_classif(X, y)

mi_scores = pd.Series(scores, index=X.columns)

print(mi_scores)