#Featurre selection 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age":[22,25,30,35,40],
    "Salary":[25000,30000,50000,70000,90000],
    "Experience":[1,2,4,6,8],
    "CreditScore":[650,680,700,730,760]
})

corr = df.corr(numeric_only=True)

print(corr)

plt.figure(figsize=(6,4))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.show()
## if the corelation is strnger the we have to remove one among two
#  which have inconsistance data