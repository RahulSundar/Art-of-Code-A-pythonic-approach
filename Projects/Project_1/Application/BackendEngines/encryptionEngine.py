#preload modules
import sys, os

sys.path.append("/home/ratnamaru/Documents/Acads/OnlineCourses/GITHUB/MY_REPOS/Art-of-Code-A-pythonic-approach/Projects/Project_1/Modules")


#prerequisite modules
import pyEnc.Binary.base_a_decryption as basdec
import pyEnc.Binary.base_a_encryption as basenc
import pyEnc.Character.Character_encryptor as charenc
import pyEnc.Palindrome.Palindrome_generator as palgen 
import pyEnc.Palindrome.Palindrome_decryptor as paldec
import pyEnc.Utils.filehandling as fhandle


sys.path.append("/home/ratnamaru/Documents/Acads/OnlineCourses/GITHUB/MY_REPOS/Art-of-Code-A-pythonic-approach/Projects/Project_1/Application")

#IMport user defined classes
from Utils.filehandler import FileHandler

class EncryptionEngine():
    
    def __init__(self, password):
        self.password = password

    def singleLayerEncryption(self):
        """
        This function does a 3 way encryption using a sequence of Binary + Palindrome + Character (123)
        """
        
        encrypted_pwd = charenc.character_encryptor(palgen.palindrome_generator_v2(basenc.binary_encryptor(self.password)))
        
        if encrypted_pwd.isnumeric():
            return int(encrypted_pwd)
        else:
            return None
            
    def TwoLayerEncryption(self):
        """
        This function operates on the output of the single layer encryption
        """
        
        encrypted_signature = singleLayerEncryption(singleLayerEncryption(self.password))
        if encrypted_signature.isnumeric():
            return int(encrypted_signature)
        else:
            return Nones        
        
        
        
if __name__ == "__main__":
    print("modules loaded successfully")
