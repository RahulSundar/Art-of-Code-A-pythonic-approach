import sys, os

sys.path.append("/home/ratnamaru/Documents/Acads/OnlineCourses/GITHUB/MY_REPOS/Art-of-Code-A-pythonic-approach/Projects/Project_1/Modules")


#prerequisite modules
import pyEnc.Binary.base_a_decryption as basdec
import pyEnc.Binary.base_a_encryption as basenc
import pyEnc.Character.Character_encryptor as charenc
import pyEnc.Palindrome.Palindrome_generator as palgen 
import pyEnc.Palindrome.Palindrome_decryptor as paldec
import pyEnc.Utils.filehandling as fhandle


from BackendEngines.encryptionEngine import EncryptionEngine
from BackendEngines.validationGenerationEngine import ValidationGenerationEngine

from Utils.filehandler import FileHandler



#Login interface:
#---------------#

#Features:
#--------#
#1. Ask for UID, Pwd

if __name__ == "__main__":



    waiting_for_input = True
    

    while(waiting_for_input):
        print("-----------------------------------")    
        print("    Following are the options\n")
        print("-----------------------------------")
        print("1 - Login (Maximum three attempts)\n")
        print("2 - Reset Password\n")
        print("3 - Register as new user\n")
        print("Q - Quit\n")
        print("-----------------------------------")
        user_input = input("Enter your choice here: \n")
        
        # Login is buggy
        if user_input == "1":
            globals()['ctr'] = 1
            status = "Login"
            user_id = input("User ID:- ")
            password = int(input("Password:- "))
            validator = ValidationGenerationEngine(status = "Login", userid = user_id, password = password)
            while(ctr<3):
                #login validation bug free
                if validator.validateCredentials():
                    print("-----------------------------------")
                    print("      Logged in Successfully")
                    print("-----------------------------------")
                    ctr = 3
                    waiting_for_input = False
                #exception handling is buggy
                elif not validator.validateCredentials():
                    ctr = ctr + 1
                    print("---------------------------------------------------------------------------------------------------")
                    print("Please try again. Maximum three attempts are allowed. This is your " + str(ctr) + "th attempt.\n")
                    print("---------------------------------------------------------------------------------------------------")
                    status = "Login"
                    user_id = input("User ID:- ")
                    password = input("Password:- ")
                    validator = ValidationGenerationEngine(status = "Login", userid = user_id, password = password)
                    validator.validateCredentials()
                else:
                    break
        elif user_input == "2":
            status = "Reset"
            user_id = input("User ID:- ")
            reset_status = True
            while(reset_status):
                password = int(input("New Password:- "))
                confirm_password = int(input("Confirm Password:- "))
                if password == confirm_password:
                    reset = ValidationGenerationEngine(status = "Reset", userid = user_id, password = password)
                    reset.generateCredentials()
                    reset_status = False
                    print("---------------------------------------------------------------------------------------------------")
                    print("Credentials reset successfully\n")
                    print("---------------------------------------------------------------------------------------------------")
                else:
                    print("---------------------------------------------------------------------------------------------------")
                    print("Please try again. password and confirmation of the password don't match.\n")
                    print("---------------------------------------------------------------------------------------------------")
        # Generation bug free
        elif user_input == "3":
            status = "Register"
            user_id = input("User ID:- ")
            password = int(input("Password:- "))
            register = ValidationGenerationEngine(status = "Register", userid = user_id, password = password)
            register.generateCredentials()
        elif user_input == "Q":
            waiting_for_input = False
        else:
            print("Enter a valid choice.\n")            
    
