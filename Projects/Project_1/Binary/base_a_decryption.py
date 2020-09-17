# Decrypts any code given in a string format and obtains the encoded number. 

def binary_decryptor(code, system = 'LE'):
    """
    Returns the encoded number provided the binary code string is given.
    Arguments:
        : 1. code: A string containing the binary digits
        : 2. system: A flag to specify either big or little endian systems
    Return:
        : number    
    """

    number = 0
    code = str(code)
    if system  == 'BE':
        for index in range(len(code)):
            number += int(code[index])*(2**index)
        return number
    elif system == 'LE':
        for index in range(len(code)):
            number += int(code[index])*(2**(len(code)-1-index))
        return number
    else:
        print("ERROR: Choose a valid system")

def binary_decryptorV2( system = 'LE'):
    """
    Returns the encoded number provided the binary code string is given.
    Arguments:
        : 1. code: A string containing the binary digits
        : 2. system: A flag to specify either big or little endian systems
    Return:
        : number    
    """
    code =input("Enter the binary code: ")
    number = 0
    if system  == 'BE':
        for index in range(len(code)):
            number += int(code[index])*(2**index)
        return number
    elif system == 'LE':
        for index in range(len(code)):
            number += int(code[index])*(2**(len(code)-1-index))
        return number
    else:
        print("ERROR: Choose a valid system")



def base_a_decryptor(code, base, system = 'LE'):
    """
    Returns the encoded number provided the base and the code string is given.
    Arguments:
        : 1. code: A string containing the encoded digits
        : 2. base: The base in the number has been encoded
        : 3. system: A flag to specify either big or little endian systems
    Return:
        : number    
    """
    
    number = 0
    if base <= 10:
        if system  == 'BE':
            for index in range(len(code)):
                number += int(code[index])*(base**index)
            return number
        elif system == 'LE':
            for index in range(len(code)):
                number += int(code[index])*(base**(len(code)-1-index))
            return number
    else:
        print("Base greater than 10. Please choose a base less than 10")
        
#import gradio as gr 

#base = gr.inputs.Slider(minimum=0, maximum=10, default=2, label="base")
#system = gr.inputs.Radio(['BE', 'LE'], label="System")
#    gr.Interface(fn=base_a_decryptor, inputs=["text", base, system], outputs = "text").launch()                                                   
