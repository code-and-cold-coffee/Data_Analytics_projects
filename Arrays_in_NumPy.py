'''
Covering basics of Numpy 

'''
import pandas as pd
import numpy as np

#difference between simple list and np.array
lst=[1,2,3]
'''
Types of Dimensions:
1) 0-dim, 2) 1-dim, 3) 2-dim, 4) 3-dim, 5) n-dim
'''
# 0 dimensional array
dim_0 =np.array(1)
print(dim_0)

# 1 dimensional Array in Numpy 
# We use np.array() to store values
my_list=np.array([1,2,3])#1 dimensional array
print(my_list)

# 2 dimensional array
dim_2=np.array([[1,2,3],
       [4,5,6]])
print(dim_2) 
'''
creating arrays of only 'Zeroes'

'''
zeroes=np.zeros(3) # No of elements for  zeroes in 1-D Array
zeroes=np.zeros((3,2)) # Creating r by c Table of zeroes in 1-D Array
'''
creating arrays of only 'Ones' in 1-D

'''
ones_methode=np.ones(3) # No of elements for ones in 1-D Array
ones_methode=np.ones((3,2))# Creating r by c Table of ones in 1-D Array

'''
eye methode in Array
'''
identity3=np.eye(3) # -> creating identity matrix of 3 by 3
identity2=np.eye(2) # -> creating identity matrix of 2 by 2

'''
arange methode in NumPy:
       np.arange(start,stop,step)
'''
print(np.arange(10)) # Print Numbers from 0 to 9 while 10 is the stoping index that is excluded

# 3 dimensional array
dim_3=np.array([[1,2],[3,4],[5,6]])
print(dim_3) # 3 dimensional array

'''
Properties of Array :
'''
# Shape attribute -> Returns no of Row and Column of an Array
arr=np.array([1,2,3,4,5])
print(arr.shape) # -> (5,)
arr2=np.array([[1,2,3,4],[5,6,7,8]]) # -> 2-Dimensional Array
print(arr2.shape) # -> (2,4) -> 2 rows and 4 columns

'''
Size of an Array:
'''
no_of_el=np.array([[1,2],[3,4],[5,6]])
print(no_of_el.size) # -> returns number of elements in array -> 6
dim1=np.array([1,2,3])
print(dim1.size) # -> 3

'''
ndim() Methode in Array:
Returns Dimension of an Array
'''
no_of_el=np.array([[[1,2],[3,4],[5,6]]])
print(no_of_el.ndim) # -> returns Dimension of an array -> 3
dim1=np.array([1,2,3])
print(dim1.ndim) # ->  Dimenion 1

'''
Data type of an Array:
array.dtype -> Returns data type of an Array
'''
type_of_arr=np.array([[[1,2],[3,4],[5,6]]])
print(type_of_arr.dtype) # -> returns Data type of this array -> int64
dim1=np.array([1.1,2.4,3.8])
print(dim1.dtype) # ->  float64

