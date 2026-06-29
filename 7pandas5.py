# use of xml file to read the data

import pandas as pd

df=pd.read_xml("test.xml")# tes.xml file should exist in the folder

print(df)

# covert to xml 
df.to_xml('test1.xml')