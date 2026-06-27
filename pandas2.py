from io import StringIO
import pandas as pd

# importing csv files
df= pd.read_csv('mercedesbenz.csv')
print(df.head())

# coverting string in to in memory file formate
stdata=('col1,col2,col3 \n'
        'x,y,1 \n' 'a,b,2 \n' 'c,d,3 \n')
print(stdata)
print (type(stdata))

#covert into in memmory file format
# string data to file formate data  for gainiing useful insight 
StringIO(stdata)
df1= pd.read_csv(StringIO(stdata))
print(df1)

## opearation in data
# use  of "usecols" --> when we have to read onlu few coloumn in large dataset

df= pd.read_csv('mercedesbenz.csv' , usecols=['X0','X1','X2'])
print(df.head())
