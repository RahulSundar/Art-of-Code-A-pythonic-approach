import sys, os

sys.path.append("/home/ratnamaru/Documents/Acads/OnlineCourses/GITHUB/MY_REPOS/Art-of-Code-A-pythonic-approach/Projects/Project_1/Modules")


#prerequisite modules
import pyEnc.Binary.base_a_decryption as basdec
import pyEnc.Binary.base_a_encryption as basenc
import pyEnc.Character.Character_encryptor as charenc
import pyEnc.Palindrome.Palindrome_generator as palgen 
import pyEnc.Palindrome.Palindrome_decryptor as paldec
import pyEnc.Utils.filehandling as fhandle



if __name__ == "__main__":
    print(basenc.base_a_encrypt())
    print("Modules were imported successfully ")
