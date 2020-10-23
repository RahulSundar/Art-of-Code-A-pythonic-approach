
# Main function:
class BaseEncrypt:

    def __init__(self, system = "LE", base_number = 2):
        self.system = system 
        self.base_number = base_number

    def base_a_encrypt(self):
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
        if self.base_number <= 10:
            # Initialise the Code as an empty string 
            Code = ""
            # Take user input of a number
            Number = int(input("Enter the number of your choice: "))
            if Number == 0:
                return {'BE': '0', 'LE': '0'}
            else:
            # Encryption to the given 'base_number' system:
                while (Number!= 0):
                    Remainder = int(Number % self.base_number)
                    Number = int((Number - Remainder) / self.base_number)
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

    def base_a_encrypt_v2(self, input_number):
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
        if self.base_number <= 10:
            # Initialise the Code as an empty string 
            Code = ""
            # Take user input of a number
            Number = int(input_number)
            # Encryption to the given 'base_number' system:
            if Number == 0:
                return {'BE': '0', 'LE': '0'}
            else:
                while (Number!= 0):
                    Remainder = int(Number % self.base_number)
                    Number = int((Number - Remainder) / self.base_number)
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


    def binary_en_rec(self,number,code, binary_en_rec):
        if int(number)==0: 
            code += str(0) 
            return code 
        else: 
            remainder = int(number % self.base_number) 
            quotient = int((number - remainder)/self.base_number) 
            print(quotient, remainder) 
            return  str(binary_en_rec(quotient, self.base_number, code+str(remainder)))  
