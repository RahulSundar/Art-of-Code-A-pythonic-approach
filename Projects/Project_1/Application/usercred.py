import Binary.base_a_encryption as basenc
import Character.Character_encryptor as charenc
import Palindrome.Palindrome_generator as palgen 
import Binary.base_a_decryption as basdec 
import Palindrome.Palindrome_decryptor as paldec
import Utils.filehandling as fhandle


class UserCredentials():

    def __init__(self, username, password, usertype = "existing", userchoice = "login",  credentials_save_path = "./usercredentials.txt", key_save_path = "./keys.txt" ):
        self.username = username
        self.password = password
        self.usertype = usertype
        self.credentials_save_path = credentials_save_path
        self.key_save_path = key_save_path


        self.__UsernameList, self.__PasswordList = fhandle.readuserfile('Input.txt')    
        
        self.credentials_local = {}
        
        self.__update_credentials()
        
        
        if self.usertype == "new" && self.userchoice == "register":
            self.create_new_user()
            self.update_credentials()
        elif self.usertype == "existing" && self.userchoice == "forgotpwd":
            self.reset_password()
        else:
            pass

        
    def get_user_choice(self):
        user_input = input('Your choice:')
        return user_input
                        
    def create_new_user(self):
        self.__UsernameList += [self.username] 
        self.__PasswordList += [basenc.binary_encryptor_v2(int(input("Enter the username: ")))]
        
    def reset_password(self):
        #Check the index of the username:
        try:
            index = self.__UsernameList.index(self.username)
            self.__PasswordList[index] = basenc.binary_encryptor_v2(int(input("Enter the new password: ")))
        except(ValueError):
            print("User doesn't exist")
            a = input("Do you want to create an account?[y/n]")
            if a == "y":
                self.create_new_user()
            else:
                print("Error: You are not registered as a user! ")
            #self.UsernameList += [self.username] 
            #index = self.UsernameList.index(self.username)  
    def validate_user_credentials(self):
        try:
            index = self.__UsernameList.index(self.username)
            flag = ( self.__PasswordList[index] == basenc.binary_encryptor_v2(self.password) )
            if flag == True:
                print("Login Successful")
            else:
                print("Kindly check your password")
        except(ValueError):
            print("Username and password don't exist in the database. Either reset the password or register.")
        
    def update_credentials()
        with open('Usercredentials.txt', mode = 'w') as filename:
            for i in range(len(self.__UsernameList)):
                filename.write(self.__UsernameList[i] + " " + str(self.__PasswordList[i]))
                filename.write('\n')
                
                
    def listen_for_input():
    
    
        print("Available userchoices\n")
        print("1. Login")
        print("2. Forgot password")
        print("3. New user registration")
        
        user_choice = self.get_user_choice()
        
        if user_choice == "1":
            pass
        pass
    
