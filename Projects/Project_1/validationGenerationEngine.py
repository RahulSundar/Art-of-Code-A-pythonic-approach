#Prereqs:
import json

#prerequisite modules
import Modules.pyEnc.Binary.base_a_decryption as basdec
import Modules.pyEnc.Binary.base_a_encryption as basenc
import Modules.pyEnc.Character.Character_encryptor as charenc
import Modules.pyEnc.Palindrome.Palindrome_generator as palgen 
import Modules.pyEnc.Palindrome.Palindrome_decryptor as paldec
import Modules.pyEnc.Utils.filehandling as fhandle

#User defined classes
from Utils.filehandler import FileHandler
from encryptionEngine import EncryptionEngine


class ValidationGenerationEngine(EncryptionEngine, FileHandler):
    
    def __init__(self, userid, password):
        self.userid = userid
        self.password = password
        self.usercred = {userid:self.oneLayerEncryption(password), userid + "_sign": self.uniqueSignature(self.password)}
        
        
    def uniqueSignature(self):
        return self.twoLayerEncryption(self.password)
    
    def validateCredentials(self):    
        with open("UserCredentials.json", mode = "r") as ucred:
            ucredcontent = ucred.readlines()
            ucredDict = json.loads(ucredcontent[0])
        #Remember ucredDict[self.userid] gives us the encrypted password
        if ucredDict[self.userid] == self.oneLayerEncryption(self.password):
            return True
        else:
            print("Wrong user ID/Password. Do you have your account registered?")
            return False
        
            
    def generateCredentials(self):
        with open("UserCredentials.json", mode = "r") as ucredread:
            ucredcontent = ucredread.readlines()
            ucredDict = json.loads(ucredcontent[0])
        ucredDict[self.userid] =  self.oneLayerEncryption(self.password)
        ucredDict[self.userid + "_sign"] =  self.uniqueSignature(self.password)      
        with open("UserCredentials.json", mode = "w") as ucredwrite:
            ucredwrite.write(json.dumps(ucredDict))
        print("Generated new user credentials")
        return True    
        
        
        
        

            
        
        
    
