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

# 3 dimensional array
dim_3=np.array([[1,2],[3,4],[5,6]])
print(dim_3) # 3 dimensional array
