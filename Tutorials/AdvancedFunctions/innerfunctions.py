def innerfunctions():

    def firstone():
        print("Hi there")

    def secondone():
        print("This is the second function")

    return [firstone, secondone] # return a list
    #return(firstone, secondone) # return a tuple
    #return firstone, secondone # return an unpacked
    #return {"1": firstone, "2": secondone}


L = innerfunctions()

L[0]()
L[1]()