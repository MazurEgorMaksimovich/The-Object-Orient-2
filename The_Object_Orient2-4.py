class Alphabet:
    
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    
    def alphprint(self):
        alphlist = ""
        for letter in self.letters:
            alphlist += letter + " "
        return alphlist
    
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    import string
    
    _letters_num = 26
    
    def __init__(self, lang="English", letters=string.ascii_uppercase):
        super().__init__(lang, letters)
    
    def letters_num(self):
        return EngAlphabet._letters_num
    
    def is_en_letter(self, letter):
        if letter in self.letters:
            return True
        else:
            return False
    
    @staticmethod
    def example():
        return "London is the capital of the Great Britain."



engalph = EngAlphabet()
print(engalph.alphprint())
print(engalph.letters_num())
print(engalph.is_en_letter('F'))
print(engalph.is_en_letter('Щ'))
print('English Example:')
print(EngAlphabet.example())