#The following exercise will suggest as to why NumPy works best in data science

#This is the decorator to map time for how long a function works
import numpy as np
import time 
from functools import wraps

#creating decorator
def timer(func):
    @wraps(func) #makes sure any func using this wrapper does not lose it original identity
    #default function created to calculate and return time 
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

data = np.random.randint(1, 101, size = 1_000_000)  #creating a list of 1 million random numbers

#SQUARE TEST

#checking as to how long it would take to square each number in the data list using loop
@timer
def square_Loop(arr):
    out = []
    for x in arr:
        out.append(x**2)
    return out

#vectorization basically mean passing the entire list all at once rather than looping and sending each element
#checking as to how long it would take to square each number in the data list using vectorization
@timer
def square_vectorized(arr):
    return arr**2

square_Loop(data)
square_vectorized(data)


#SUM TEST

@timer
def sum_loop(arr):
    out = []
    for x in arr:
        out.append(x+10)
    return out

@timer
def sum_vectorized(arr):
    return arr+10

sum_loop(data)
sum_vectorized(data)

#DOT PRODUCT

arr1 = np.random.rand(1_000_000)
arr2 = np.random.rand(1_000_000)

@timer 
def dotProd_loop(arr1, arr2):  #zip(arr1, arr2) basically pairs the corresponding elements of respective arrays like(x1,y1) where x1 is first element of arr1 and y1 is first element of arr2
    out = 0.0
    for x,y in zip(arr1, arr2):
        out += x*y
    return out

@timer
def dotProd_vectorized(arr1, arr2):
    return arr1 @ arr2

dotProd_loop(arr1, arr2)
dotProd_vectorized(arr1, arr2)


#MEAN TEST

@timer
def mean_loop(arr):
    total = 0.0
    for x in arr:
        total += x
    #print(total/arr.size)
    return total/arr.size

@timer
def mean_vectorized(arr):
    #print(np.mean(arr))
    return np.mean(arr)

mean_loop(data)
mean_vectorized(data)


#FILTER TEST (finding even nums)

@timer
def filter_loop(arr):
    out = []
    for x in arr:
        if x%2==0:
            out.append(x)
    print(out)
    return out

@timer
def filter_vectorized(arr):
    #Masking here
    arrIn = arr[arr % 2 == 0]
    print(arrIn)
    return arrIn

filter_loop(data)
filter_vectorized(data)
