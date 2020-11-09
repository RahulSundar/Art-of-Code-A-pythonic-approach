
class FileHandler():

    def readfromfile(modulename = "Binary", File = "base_a_code.txt", linenumber=0):
        with open(File, mode = 'r') as filename:
            A = filename.readlines()
            if modulename == "Binary":
                return {"BE": A[linenumber-1].split()[0], "LE":A[linenumber-1].split()[1]} 
            else:
                return A[linenumber-1][:-1]
         
    def readuserfile(File):
        with open(File, mode = 'r') as filename:
            A = filename.readlines()
            UserNameList = []
            PasswordList = []
            for i in range(len(A)):
                UserNameList.append(A[i].split()[0])
                PasswordList.append(A[i].split()[1])
            return UserNameList, PasswordList
            
                      
    def writecodetofilebrute(code, modulename = "Binary", File = "base_a_code.txt"):
        with open(File, mode = 'a') as filename:
            A = code
            print(A)
            if modulename == "Binary":
                filename.write(str(A['BE']) +" " + str(A['LE']))
                filename.write('\n')
            else:
                filename.write(str(A))
                filename.write('\n')
                
                
                
    def readUserCredentials(self):
        pass
        
    def appendUserCredentials(self):
        pass
        
    def rewriteUserCredentials(self):
        pass
        
        
