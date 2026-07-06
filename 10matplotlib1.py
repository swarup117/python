# using matplotlib for visualization 

# import the library
import matplotlib.pyplot as plt

import numpy as np

x=np.arange(1,10)
y=np.arange(11,20)
y=x*x
print(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('2d graph ')


a=np.arange(40,50)
b=np.arange(50,60)

# single plot 
plt.scatter(x,y,c='r')
plt.show()

plt.plot(x,y,c='g')
plt.show()

# ploting multiple diagram in 1
plt.subplot(2,2,1)
plt.scatter(x,y,c='r')
plt.show()

plt.subplot(2,2,2)
plt.plot(x,y,c='g')
plt.show()

plt.subplot(2,2,3)
plt.scatter(a,b,c='b')
plt.show()

# ploting waaves 
p=np.arange(0,5*np.pi,0.1)
q_sin=np.sin(p)
q_cos=np.cos(p)
print(p,q_sin,q_cos)

#for sin wave
plt.subplot(2,1,1)
plt.plot(p,q_sin)
plt.title('sin wave')

#for cos wave
plt.subplot(2,1,2)
plt.plot(p,q_cos)
plt.title('cos wave')
plt.show()


#bar chart
x1=[12,13,16,22,24,34,51]
y1=[2,4,6,8,10,12,14]

x2=[22,32,42,12,45,32,12]
y2=[3,5,7,9,11,13,15]

plt.bar(x1,y1,color='r')
plt.bar(x2,y2,color='b')
plt.show()

# histrogram
a=[22,4,3,12,34,56,43,66,33,77,12,44,53,65,76,87,54,76,54,43]
plt.hist(a, bins=10)
plt.title('histrogram')
plt.show()

# pie chart

lables=['python', 'jave', 'c++', 'ruby']
size=[231,125,110,85]
explode=[0.1,0,0,0]
color=['red', 'blue','green', 'yellow']

plt.pie(size,explode=explode,labels=lables,colors=color,
        autopct='%1.1f%%', shadow=True)
plt.axis('equal')
plt.show()

#box plot

data=[np.random.normal(0, std, 100) for std in range(1,4)]
plt.boxplot(data, vert=True, patch_artist=True) 
plt.show()