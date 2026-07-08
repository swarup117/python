# visualization using seaborn

import seaborn as sns
import matplotlib.pyplot as plt


df =sns.load_dataset("tips")
print(df.head())

# correlation with heatmap
# Correlation tells us how two variables are related.
# heatmap uses colors to represent numbers and show the relatioship.

corr1=df.corr(numeric_only=True)
print(corr1)
sns.heatmap(corr1 , annot=True)
plt.show()

#jointplot
# The relationship between two variables (Scatter Plot)
# The distribution of the first variable (Histogram)
# The distribution of the second variable (Histogram)
# #univariant analysis

sns.jointplot(data=df, x='tip' , y='total_bill' , kind='hex')
plt.show()

sns.jointplot(data=df, x='tip' , y='total_bill' , kind='reg')
plt.show()

# pairplot
# A Pair Plot compares every numerical column with every other numerical
#  column Think of it as creating many scatter plots automatically.

sns.pairplot(df)
plt.show()
# histogram shows only density bcause no need to compare with itself

sns.pairplot(df, hue='sex')
plt.show()

# distplot
# A distribution plot shows how your data is distributed.
# Which values occur most frequently

sns.histplot(df['tip'],bins=10,kde=True)
plt.show()

sns.kdeplot(df['tip'])
plt.show()

# countplot

sns.countplot(x='sex',data=df)
plt.show()

sns.countplot(y='smoker',data=df)
plt.show()

sns.countplot(x='sex',hue='smoker',data=df)
plt.show()

# barplot
sns.barplot(x='sex', y='total_bill' , data=df)
plt.show()

# boxplot
# Box Plot summarizes a numerical column using 5 important values

sns.boxplot(x='day' , y='total_bill', data=df)
plt.show()

sns.boxplot(x='sex' , y='total_bill', data=df)
plt.show()

sns.boxplot(data=df, orient='v')
plt.show()



## use iris dataseta and perform tis task