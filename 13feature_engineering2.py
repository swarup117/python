#one hot encoding
#Instead of assigning one number, we create one column for each category.

import pandas as pd
from sklearn.preprocessing import OneHotEncoder # from not import

df=pd.DataFrame({
   "color": ["red","green","blue","yellow"]
})
print(df)

encoder = OneHotEncoder() # crating the object of onehotencoder

encoded = encoder.fit_transform(df[["color"]])

encoded_df = pd.DataFrame(
    encoded.toarray(),
    columns=encoder.get_feature_names_out()
)

print(encoded_df)

##for more them one coloum
import pandas as pd

df1 = pd.DataFrame({
    "color": ["red", "green", "blue", "yellow"],
    "city": ["Tokyo", "Delhi", "London", "Tokyo"]
})

print(df1)

encoder = OneHotEncoder(sparse_output=False)

encoded = encoder.fit_transform(df1[["color", "city"]])

encoded_df1 = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out()
)

print(encoded_df1)



## get_dummies

import pandas as pd

df2 = pd.DataFrame({
    "City":["Kathmandu","Pokhara","Butwal"]
})

newdf=pd.get_dummies(df2,dtype=int)
print(newdf)
