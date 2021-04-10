import numpy as np
import functools

def do_twice(func):
    @functools.wraps(func)
    def wraparound(*args, **kwargs):
        print(func(*args, **kwargs))
        print(func(*args, **kwargs))
    return wraparound


def cube(list):
    return [list[i]**3 for i in range(len(list))]

def square(list):
    return [list[i]**2 for i in range(len(list))]

def powern(list):
    n = float(input("Enter the power:"))
    return [list[i]**n for i in range(len(list))]

def sum_func_large(list):
    n = float(input("Enter the power:"))
    listnew = [list[i]**n for i in range(len(list))]
    return np.sum(listnew)

@do_twice
def sum_func(list, func):
    listnew = func(list)
    return np.sum(listnew)

#1. Functions within a function
#2. Pass functions as arguments
#3. Functions as decorators to modify the behaviour of an existing function
#4. args, kwargs 


#List = [1,2,3]
#sum_func(List, func = cube)
#print(sum_func(List, powern), sum_func_large(List))

#do_twice(sum_func_large)(List)