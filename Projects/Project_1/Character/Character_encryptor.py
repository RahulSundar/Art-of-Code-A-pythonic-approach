class CharEnc:


    def character_counter(self, string):
        string = str(string)
        dict_char_count = dict({i:string.count(i) for i in string})
        
        return dict_char_count


    def character_counter_v2(self, string):
        string = str(string)
        dict_char_count = dict({i:string.count(i) for i in string if string.count(i) > 1})
        
        return dict_char_count

    def character_count_encryptor_v2(self, string):
        dictionary = self.character_counter(string)
        code = ""
        for keys,values in dictionary.items():
            code += keys + str(values)
            
        return code

    def character_count_encryptor_v4(self):
        string = input("Enter data to be codified: ")
        dictionary = self.character_counter(string)
        code = ""
        for keys,values in dictionary.items():
            code += keys + str(values)
            
        return code


    def character_count_encryptor_v3(self,sentence):

        word_list = sentence.split()
        sentence_code = ""
        for index in range(len(word_list)):
            sentence_code += self.character_count_encryptor_v2(word_list[index]) + " "
        return sentence_code




