import Binary.base_a_encryption as basenc
import Character.Character_encryptor as charenc
import Palindrome.Palindrome_generator as palgen 
import Binary.base_a_decryption as basdec 
import Palindrome.Palindrome_decryptor as paldec
import Utils.filehandling as fhandle


UsernameList, PasswordList = fhandle.readuserfile('Input.txt')
#print(UsernameList, PasswordList)

Credentials = {}
for i in range(len(PasswordList)):
    if PasswordList[i].isnumeric() == True: 
        c1 = palgen.palindrome_generator(PasswordList[i]) 
        c2 = basenc.base_a_encrypt_v2(c1, base_number=5) 
        c3 = charenc.character_count_encryptor_v2(c2['BE'])
        with open('Usercredentials.txt', mode = 'a') as filename:
            filename.write(UsernameList[i] + " " + str(c3))
            filename.write('\n')
        Credentials[UsernameList[i]] = c3
        with open('Output.txt',mode = 'w') as filename:
            filename.write(str(Credentials))
            filename.write('\n')

get_username = input("Enter Username: \n")
try:
    ctr = 0
    #check username
    while Credentials[get_username]:
        get_password = input("Enter Password(only numerics): \n")
        if get_password.isnumeric() == True: 
            c1 = palgen.palindrome_generator(get_password) 
            c2 = basenc.base_a_encrypt_v2(c1, base_number=5) 
            Code = charenc.character_count_encryptor_v2(c2['BE'])
        #Check the password
        if Code == Credentials[get_username]:
            print("----------------\n")
            print("Login Successful!")
            print("----------------\n")
            break
        else:
            ctr = ctr + 1
            print(ctr)
            print("Wrong password")
            if ctr == 3:
                print("---------------------------------------\n")
                print("3 Unsuccessful attempts. Reset password?")
                print("---------------------------------------\n")
                break
#Error handling
except(KeyError):
    print("----------------------------------------------------------------\n")
    print("No user by the name " + get_username + " present! Please sign up\n" )
    print("----------------------------------------------------------------\n")
finally:
    print("All done")


#Generate a new userid, password.
#Reset a password
#Set a GUI interface
#File handling of dictionary output and reading dictionaries from files. (json, pickle, pycrypto)