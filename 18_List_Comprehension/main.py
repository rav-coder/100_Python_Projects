import pandas

word_dict = {row.letter: row.code for (index, row)
             in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}

# print(word_dict)

name = input("Write your first name?").upper()
print([word_dict[letter] for letter in list(name)])
# print([code for (letter, code) in word_dict.items() if letter in list(name)])
