#preload modules

import Modules.pyEnc.Binary.base_a_encryption as basenc
import Modules.pyEnc.Character.Character_encryptor as charenc
import Modules.pyEnc.Palindrome.Palindrome_generator as palgen 
import Modules.pyEnc.Utils.filehandling as fhandle

#Import user defined classes
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
        
