import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

#pie notation
@my_decorator  
def say_hello():
    print("Hola! Amigos!")


#hithere = my_decorator(say_hello)
say_hello()



def do_ntimes(func):
    @functools.wraps(func)
    def wrapper():
        n = int(input("Enter the number of calls"))
        i = 0
        while i < n:
            func()
            i += 1
    return wrapper

@do_ntimes
def say_hello_n():
    print("Hola! Amigos!")

say_hello_n()


def acceptintreturnfloat(func):
    @functools.wraps(func) # helps preserve the identity of the function func()
    def wrapper(*args, **kwargs): #(*args, **kwargs)
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper

