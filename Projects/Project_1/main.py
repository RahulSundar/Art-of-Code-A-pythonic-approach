import Modules.pyEnc.Binary.base_a_decryption as basdec
import Modules.pyEnc.Binary.base_a_encryption as basenc
import Modules.pyEnc.Character.Character_encryptor as charenc
import Modules.pyEnc.Palindrome.Palindrome_generator as palgen 
import Modules.pyEnc.Palindrome.Palindrome_decryptor as paldec
import Modules.pyEnc.Utils.filehandling as fhandle

if __name__ == "__main__":


    waiting_for_input = True

    while waiting_for_input:


        print("-------------------------------- ")
        print('1: Choose encryption ')
        print('2: Choose decryption ')
        print('q: Quit\n')


        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            print("1: Base 'a' encryption")
            print("2: Palindrome generation")
            print("3: Character count encryption ")
            print("12: Base 'a' encryption + Palindrome generation")
            print("21: Palindrome generation + Base 'a' encryption ")
            print("23: Palindrome generation + character count encryption")
            print("32:  character count encryption + Palindrome generation \n")
            print("1W:  Binary encryption + file writeq \n")
            print("---------------------------------") 

            user_choice_method = input("Enter your choice of method from above: ")
 
            if user_choice_method == '1':
                user_base = int(input("Enter the base number: "))
                print(basenc.base_a_encrypt(base_number = user_base))
            elif user_choice_method == '2':
                print(palgen.palindrome_generatorV3())
            elif user_choice_method == '3':
                #string = input()
                print(charenc.character_count_encryptor_v4())
            elif user_choice_method == '12':
                user_base = int(input("Enter the base number: "))
                print(palgen.palindrome_generator(basenc.base_a_encrypt(base_number = user_base)['LE']))
            elif user_choice_method == '21': 
                user_base = int(input("Enter the base number: "))
                print(basenc.base_a_encrypt_v2(int(palgen.palindrome_generatorV3()))['LE'])
            elif user_choice_method == '23':
                print(charenc.character_count_encryptor_v2(palgen.palindrome_generatorV3()))
            elif user_choice_method == '32':
                string = input("Enter ata to be codified: ")
                print(palgen.palindrome_generator(charenc.character_count_encryptor_v2(string)))
            elif user_choice_method == '1W':
                code = basenc.base_a_encrypt()
                fhandle.writecodetofilebrute(code, modulename = "Binary")
            elif user_choice_method == '1R':
                linenumber = int(input("Enter line number to read from: "))
                print(fhandle.readfromfile(linenumber = linenumber, modulename='Binary' ))
            elif user_choice_method == '2W':
                code = palgen.palindrome_generatorV3()
                fhandle.writecodetofilebrute(code, modulename = "Palindrome", File = 'palindrome_code.txt')
            elif user_choice_method == '2R':
                linenumber = int(input("Enter line number to read from: "))
                print(fhandle.readfromfile(linenumber = linenumber, modulename = 'Palindrome',  File = 'palindrome_code.txt'))
            elif user_choice_method == '3W':
                string = input()
                code = charenc.character_count_encryptor_v2(string)
                fhandle.writecodetofilebrute(code, modulename = "Char", File = 'char_code.txt')
            elif user_choice_method == '3R':
                linenumber = int(input("Enter line number to read from: "))
                print(fhandle.readfromfile(linenumber = linenumber, modulename = 'Char',  File = 'char_code.txt'))

            else:
                print("Not a valid choice of method. Valid choices are as follows: \n")
                print("1: Base 'a' encryption")
                print("2: Palindrome generation")
                print("3: Character count encryption ")
                print("12: Base 'a' encryption + Palindrome generation")
                print("21: Palindrome generation + Base 'a' encryption ")
                print("23: Palindrome generation + character count encryption")
                print("32:  character count encryption + Palindrome generation \n")
                print("Begin again from start")
                print("---------------------------------")
                continue

        elif user_choice == '2':
            print("Valid choices are as follows: \n")
            print("1: Base 'a' decryption")
            print("2: Palindrome decryption")
            print("21: Base 'a' decryption + Palindrome decryption")
            print("12: Palindrome gdecryption + Base 'a' decryption \n")
            print("---------------------------------") 
            user_choice_method = input("Enter your choice of method: ")
            if user_choice_method == '1':
                print(basdec.binary_decryptorV2())
            elif user_choice_method == '2':
                print(paldec.palindrome_decryptorV2())
            elif user_choice_method == '12':
                print(basdec.binary_decryptor(paldec.palindrome_decryptorV2()))
            elif user_choice_method == '21':
                print(paldec.palindrome_decryptor(basdec.binary_decryptorV2()))
            else:
                print("Not a valid choice of method. Valid choices are as follows: \n")
                print("1: Base 'a' decryption")
                print("2: Palindrome decryption")
                print("21: Base 'a' decryption + Palindrome decryption")
                print("12: Palindrome gdecryption + Base 'a' decryption \n")
                print("Begin again from start")
                print("---------------------------------")
                continue

        elif user_choice == 'q':
            waiting_for_input = False
        else:
            print("Decide whether to decrypt or encrypt! Make up your mind! ")
