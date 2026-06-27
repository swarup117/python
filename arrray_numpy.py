## import library
import numpy as np

lst = [1,2,3,4,5,6]

# converting lst to array
 
arr=np.array(lst)
print(type(arr))


#  two dimentional array
lst1=[1,2,3,4,5]
lst2=[6,7,8,9,1]
lst3=[2,4,6,8,0]
newarr=np.array([lst1,lst2,lst3])
print (newarr)
print (type(newarr))

"""
#indexing in array 
arr
print(arr[3])

#changing the element
arr[3]=6
print(arr)

# selecting the element
print(arr[1:4])


# opperation on 2 dimentional array
print(newarr[:,1])
print(newarr[1:,1:3])

# reshaping the array
print(newarr.reshape(5,3))

"""

## EDA in array 
#mechanish to crate new array 
#np.arange(1,20,1) here (start , stop and step)
create_array=np.arange(1,21,1).reshape(2,10)
print(create_array)

# operation in array
#print(lst * lst)
print(newarr*2)

# inbuilt functio in array
print(np.ones((3,4)))
print(np.zeros((4,4)))
print(np.random.randint(10,50,5))# ramber number bewtween 10 and 50 any 5


