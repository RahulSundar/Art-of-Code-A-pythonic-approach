
# Main function:

def base_a_encrypt(base_number):
    """
    Returns an encrypted code in big and litte endian formats for a user chosen number.
    The encryption is performed using a specific base number provided as an input. 
    Arguments:
        : base_number: The base to which the given number is to be converted to.
    Returns:
        : A dictionary containing the big and little endian format of the encoded number. 
    Example:
        >>> base_a_encrypt(2)
        Input[0] Enter the number of your choice: 8
        Ouput[0]8
                4
                2
                1
                0

        output[1]: {LE: "1000", BE: "0001"}   
    """
    # Check whether the base_number is less than or equal to 10
    if base_number <= 10:
        # Initialise the Code as an empty string 
        Code = ""
        # Take user input of a number
        Number = int(input("Enter the number of your choice: "))
        if Number == 0:
            return {'BE': '0', 'LE': '0'}
        else:
        # Encryption to the given 'base_number' system:
            while (Number!= 0):
                Remainder = int(Number % base_number)
                Number = int((Number - Remainder) / base_number)
                #print(Number)
                Code += str(Remainder)
            # Big endian format
            Code_BE = Code
            #print(Code_BE)
            # Little endian format
            Code_LE = Code[len(Code)::-1] 
            #print(Code_LE)
            return {'BE': Code_BE, 'LE':Code_LE}
    else:
        print("Hey! The base number <= 10 always in my code. Gotcha! You messed up. Take a number less than 10")

def base_a_encrypt_v2(input_number, base_number):
    """
    Returns an encrypted code in big and litte endian formats for a user chosen number.
    The encryption is performed using a specific base number provided as an input. 
    Arguments:
        : input_number: Must be a positive integer
        : base_number: The base to which the given number is to be converted to. base_number <= 10
    Returns:
        : A dictionary containing the big and little endian format of the encoded number. 
    Example:
        >>> base_a_encrypt(8, 2)
        
        Ouput[0]8
                4
                2
                1
                0

        output[1]: {LE: "1000", BE: "0001"}   
    """
    # Check whether the base_number is less than or equal to 10
    if base_number <= 10:
        # Initialise the Code as an empty string 
        Code = ""
        # Take user input of a number
        Number = int(input_number)
        # Encryption to the given 'base_number' system:
        if Number == 0:
            return {'BE': '0', 'LE': '0'}
        else:
            while (Number!= 0):
                Remainder = int(Number % base_number)
                Number = int((Number - Remainder) / base_number)
                #print(Number)
                Code += str(Remainder)
            # Big endian format
            Code_BE = Code
            #print(Code_BE)
            # Little endian format
            Code_LE = Code[len(Code)::-1] 
            #print(Code_LE)
            return {'BE': Code_BE, 'LE':Code_LE}
    else:
        print("Hey! The base number <= 10 always in my code. Gotcha! You messed up. Take a number less than 10")


def binary_en_rec(number, base,code):
    if int(number)==0: 
        code += str(0) 
        return code 
    else: 
        remainder = int(number % base) 
        quotient = int((number - remainder)/base) 
        print(quotient, remainder) 
        return  str(binary_en_rec(quotient, base, code+str(remainder))) 



def writecodetofilebrute(inputnumber, base_number):
    with open('base_a_code.txt', mode = 'a') as filename:
        A = base_a_encrypt_v2(inputnumber, base_number)
        filename.write(str(A['LE']) +" " + str(A['BE']))
        filename.write('\n')
        
        
def readfromfile():
    pass
        

# 1. For a single input:
#A = base_a_encrypt(2)
#print(A)

# 2. For a list of values:
# 2.1V1 of base encryption
## 2.1.1. Method 1 - Without list comprehensions
#Empty_list = []
#List_codes_1 = Empty_list
#for i in range(10):
#    List_codes_1 += [base_a_encrypt(2)]
#print(List_codes_1)

## 2.1.2. Method 2: With list comprehensions
#List_codes_2 = [base_a_encrypt(2) for i in range(10)]
#print(List_codes_2)

#print(List_codes_1 == List_codes_2)


# 2.2 V2 of base_encrpytion:

## Initialise a list of numbers:
#Numbers = [10, 20, 44, 564, 543, 130, 232, 432, 5, 0, 13]
#2.2.1 Method 1: w/o list comprehension
#List_codes_1 = []
#for Number in Numbers:
#    List_codes_1 += [base_a_encrypt_v2(Number, 2)]
#print(List_codes_1)

#2.2.2 Method 2: With list comprehension

#List_codes_2 = []
#List_codes_2 = [base_a_encrypt_v2(Number,2) for Number in Numbers]
#print(List_codes_2)

#print(List_codes_1 == List_codes_2)
