import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dict)

word = input("What word would you like to convert to NATO Alphabet?\n").upper()
try:
    converted = [nato_dict[letter] for letter in word]
except KeyError:
    print("Sorry only letters from the alphabet please.")
else:
    print(converted)