class LetterFilter:

    def __init__(self, s):
        self.s = s

    # Enter your code here.
    # Complete the classes below.
    # Reading the inputs and writing the outputs are already done for you.


    def filter_vowels(self):
        vowels = ['a', 'e', 'i', 'o', 'u']
        word = self.s

        word = word.replace("a","")
        word = word.replace("e","")
        word = word.replace("i","")
        word = word.replace("o","")
        word = word.replace("u","")

        # word = word.replace(vowels, "")

        return word
        # for letter in word:
        #     print(letter)
        #     if letter not in vowels:

    # Enter your code here
    # Return a string

    def filter_consonants(self):
        word = self.s
        word = "".join([letter for letter in word if letter in "aeiou"])
        return word

# Enter your code here
# Return a string

# s = input()
s = "onomatopoeia"

f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())