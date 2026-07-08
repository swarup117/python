# exploratory data analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importing data
train=pd.read_csv('titanic_train.csv')
print(train.head())

# #to see missing data
print(train.isnull())

# visualization for missing data

sns.heatmap(train.isnull())
plt.show()
 
 # visualization 
sns.countplot(x='Survived', data=train)
plt.show()

sns.set_style('whitegrid')
sns.countplot(x='Survived', hue='Pclass' , data=train)
plt.show()

sns.countplot(x='Survived', hue='Sex' , data=train)
plt.show()

sns.histplot(train['Age'].dropna(), kde=True)
plt.show()

sns.countplot(x='SibSp', data=train)
plt.show()
 

