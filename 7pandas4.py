# pandas with Html
# it only read the table head in the html file and print only that in 
# our output


#check weather the url is blocking our request or not 
import requests

url = "https://www.w3schools.com/html/html_tables.asp"

response = requests.get(url)

print(response.status_code)

# if output is 200 the not blocking and if output is 403 the blocking



# if not bloking the request then 
# pandas with Html
import pandas as pd

url = "https://www.w3schools.com/html/html_tables.asp"

tables1 = pd.read_html(url)

print(type(tables1))
print(len(tables1))
print(tables1[0].head())



# if the request is blockin then 
#check weather the url is blocking our request or not 
import requests

url = "https://en.wikipedia.org/wiki/Mobile_country_code"

response = requests.get(url)

print(response.status_code)

# data should be converted into in memeory file

import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/Mobile_country_code"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

tables = pd.read_html(StringIO(response.text))

print(type(tables))
print(len(tables))
print(tables[0])
print(tables[0])# to print first table 
print(tables[2]) #  to print  third table 

# data should be converted into in memeory file

import pandas as pd
import requests
from io import StringIO

url = "https://en.wikipedia.org/wiki/Mobile_country_code"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# to get the specific table in the ouptur we use matche option and one of the heading 
tables = pd.read_html(StringIO(response.text), match="MNC")

print(type(tables))
print(len(tables))
print(tables[0])


# converting data into html 
tables[0].to_html('demo.html')



