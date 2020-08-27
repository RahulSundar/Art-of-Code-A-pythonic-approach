# this is basically a palindrome decoder/decrypter
def palindrome_decryptor(palindrome):
	"""this function returns the original word or sentence of a palindrome.
	Arguments: i(the input)
	Example: palindrome_retriever('helloolleh')
	output: 'hello'
		"""
	# returns the half of or simply the original input of a string or number.
	palindrome = str(palindrome)
	string = palindrome[0:len(palindrome)//2]
	if string.isnumeric() == True:
	    return int(string)
	else:
	    return string



def palindrome_sentence_decryptor(palindrome_sentence):

    palindrome_sentence = str(palindrome_sentence)
    palindrome_list     = palindrome_sentence.split()
    sentence = ""
    for palindrome in palindrome_list:
        if palindrome_list.index(palindrome) == (len(palindrome_list) - 1):
            sentence += palindrome[0:len(palindrome)//2]
        else:
            sentence += palindrome[0:len(palindrome)//2] + " "
        
    return sentence

