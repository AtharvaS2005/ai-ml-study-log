#Normalization is basically comparing two different scales 
#Scale 1 ranks a topic from 1-10
#Scale 2 ranks the same topics from 50-5000
#The idea is to compare both ranking methods as to basically what rank could for eg. rank 500 mean in scale of 1-10

#Normalizing a array will basically move from it existing scale to a scale of 0 to 1.0

#Performing test on loop vs vectorized normalization as well


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


@timer
def norm_loop(arr):
    arr_max = max(arr)
    arr_min = min(arr)
    arr_range = arr_max - arr_min
    out = []
    for x in arr:
        normalized_x = (x-arr_min)/arr_range
        out.append(normalized_x)
    #print(out)
    return out 

@timer 
def norm_vectorized(arr):
    #print((arr - arr.min())/(arr.max() - arr.min()))
    return (arr - arr.min())/(arr.max() - arr.min())


norm_loop(data)
norm_vectorized(data)


