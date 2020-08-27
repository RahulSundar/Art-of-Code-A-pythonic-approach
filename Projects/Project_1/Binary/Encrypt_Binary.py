code = "" 
n = int(input("Enter a positive integer: ")) 
while n!=0: 
    rem = int(n%2) 
    n = int((n-rem)/2) 
    code+=str(rem) 
    print(n) 
code_new = code[len(code)::-1] 

Method = "LittleEndian"


#Decryptor
if Method == "LittleEndian":
    num = 0 
        for i in range(len(code_new)): 
        ind = len(code_new) -1- i 
        num += (2**(ind))*int(code_new[i]) 
        print(num)

else:
    num = 0 
        for i in range(len(code)): 
        num += (2**i)*int(code[i]) 
        print(num)
