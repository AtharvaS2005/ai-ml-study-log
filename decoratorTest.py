#Decorator basically means like adding an extra feature at the top of a function
#This is like adding extra features to the function without modifying it actual code by just adding @decoratorName
#This is a wrapper tool and can be used on top of various functions if needed

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


@timer #slow_sum will have this counter over it 
def slow_sum(n):
    return sum(range(n))

slow_sum(10_000_000)


