# exploratory data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importing data
train=pd.read_csv('titanic_train.csv')
print(train.head())

print(train.info())

print(train.isnull().sum())
print((train.isnull().sum()/len(train))*100)

#visualization
sns.heatmap(train.isnull())
plt.show()

#data cleaning 
#here data is missing data is not remove from data set insted it is replace 
#the average of the data

#boxplot is used to know the avg with other data
sns.boxplot(x='Pclass' ,y='Age', data=train)
plt.show()

# function to change the data
def input_age(cols):
    Age = cols["Age"]
    Pclass = cols["Pclass"]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age
train['Age']=train[['Age', 'Pclass']].apply(input_age,axis=1) 
sns.heatmap(train.isnull())
plt.show()

# drop the coloum 
#if there is more null valuse either drop the coloum or feature engineering

train.drop('Cabin',axis=1, inplace=True)
train.drop(['Name','PassengerId'], axis=1, inplace=True)
print(train.head(10))

#Duplicates 
print(train.duplicated().sum())
print(train.drop_duplicates(inplace=True))

# categorial feature 
print(train.select_dtypes(include="object").columns)
print(train.select_dtypes(include="object"))
#here we use object because string is stored as object

#feature engineering for ml 

print(pd.get_dummies(train["Sex"]))# output is true and false 

train1 = pd.get_dummies(train, columns=["Sex"], dtype=int)
print(train1.head())

train1 = pd.get_dummies(train, columns=["Sex", "Embarked"], dtype=int)
print(train1.head())

