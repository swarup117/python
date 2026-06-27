# import the library 
import pandas as pd
import numpy as np

 ## crate data frame  with in the code 
df=pd.DataFrame(data=np.arange(0,10).reshape(5,2), index=["r1","r2","r3","r4","r5"],
              columns=["c1","c2"])
print (df)

# in built function of pandas

print(df.head(3) )
print(df.info(3))
print( df.describe())

#accessing the element in the data
# using coloum
print(df[['c1']])

# using location
print(df.loc[['r1','r2']])

# using bot row and cloumn 
print(df.iloc[1:3,0:1])

#converting dataframe into arrays
print(df.values)