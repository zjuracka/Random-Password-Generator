import random
from random_word import Wordnik

# Package for generating random words:
wordnik_service = Wordnik()
word_list = wordnik_service.get_random_words(hasDictionaryDef = "true", minLength = 5, maxLength = 10)
number_list = list(range(1, 999))
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*']

# Can add as many variables as you'd like:
word1 = random.choice(word_list)
word2 = random.choice(word_list)
word3 = random.choice(word_list)

digit1 = random.choice(number_list)
digit2 = random.choice(number_list)

symbol1 = random.choice(symbols_list)

# If the words are repeated, it will re-run until they are not:
if word1 != word2 != word3:
    pass
else:
    word1 = random.choice(word_list)
    word2 = random.choice(word_list)
    word3 = random.choice(word_list)

if digit2 != digit1:
    pass
else:
    digit1 = random.choice(number_list)
    digit2 = random.choice(number_list)

# Uppercase and lowercase word randomization:
A1 = word1.title()
B1 = word1.lower()

A2 = word2.title()
B2 = word2.lower()

A3 = word3.title()
B3 = word3.lower()

# Randomizes the variables, then prints the password:
created_pass = [random.choice((A1, B1)), random.choice((A2, B2)), random.choice((A3, B3)), digit1, digit2, symbol1]
random.shuffle(created_pass)
randomized_pass = ''.join(map(str, created_pass))
print(f"Random password is: {randomized_pass}")
