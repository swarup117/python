# import the library 
import pandas as pd

# we have use pd,.dataframe  because it is alrady located in python 
data={"name":"swarup", 
      "email":"swarup123@gmail.com",
      "job":[{"title1":"developer" , "title2":"analysis"}]}
print (type(data))

df=pd.DataFrame(data)
print(df)

# using json data is in jason format 
df = pd.read_json("student.json", orient='index')
print(df)