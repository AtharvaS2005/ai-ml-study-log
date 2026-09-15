import numpy as np

#creating an array as np.array means we can have the benefit of using all nump methods on array as 
#but also the array can consist of elements of same datatype
a = np.array([1,2,3])
print(a.dtype)  #finding datatype
print(a.shape)  #finding (length, shape) i.e if a 1D, 2D or 3D array

b = np.array([[1,2],[2,3],[7,8]], dtype = np.float32) #here we make the data type of float 64 to float 32 (useful when traning on limit GPU memory)
print(b.dtype)
print(b.shape)  #here length = 3 , shape = 2D this ans is (3,2)

#using sum() to add all elements in any dimensional array
m = np.array([[1,2,3],
             [4,5,6]])
print(m.sum())

#using axis to collapse i.e find sum for per row or column
#axis = 0 , find sum per column i.e collapse rows
print(m.sum(axis=0)) #like adding 1+4, 2+5, 3+6
#axis = 1 , find sum per row i.e collapse columns
print(m.sum(axis=1)) #like adding 1+2+3, 4+5+6


#Broadcasting 
#when a np.array is created with 'X' dimension and another 'Y' dimensional array/list is passed on to add to it.
#NumPy automatically broadcasts it to 'X' dimension to add it. 
#Example 1
arr1 = np.array([1,2,3])
print(arr1 + 10)  #broadcasting makes [10] to be added as [10,10,10]
#Example 2
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2+[10,10,10]) #broadcasting makes [10,20,30] to be in 2D to add like [[10,20,30],[10,20,30]]




