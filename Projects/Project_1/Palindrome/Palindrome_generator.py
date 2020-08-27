# Palindrome generator for a string/number:

import sys

def palindrome_generator(string_number):
    
    string = str(string_number)
    palindrome = string + string[::-1]
    if string.isnumeric()==False:     
        return palindrome 
    else:
        return int(palindrome)


# palindromic sentence generator;

def palindrome_sentence_generator(sentence): 
    
    sentence = str(sentence)
    word_list = sentence.split()
    palindrome_sentence = ""
    for i in range(len(word_list)):
        if i == len(word_list) - 1:
            palindrome_sentence += word_list[i] + word_list[i][::-1]
        else:
            palindrome_sentence += word_list[i] + word_list[i][::-1] + " "
    return palindrome_sentence
            

def palindrome_generator_v2(string_number): 
     ctr=0 
     ctr += sys.getsizeof(string_number) 
     string = str(string_number) 
     palindrome = string + string[::-1] 
     ctr += sys.getsizeof(string) + sys.getsizeof(palindrome) 
     if string.isnumeric()==False:      
         print(ctr) 
         return palindrome , ctr 
     else: 
         print(ctr) 
         ctr += sys.getsizeof(int(palindrome)) 
         return int(palindrome) , ctr 
