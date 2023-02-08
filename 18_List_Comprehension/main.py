import pandas

running = True
while running:
    try:
        word_dict = {row.letter: row.code for (index, row)
                     in pandas.read_csv('nato_phonetic_alphabet.csv').iterrows()}
        name = input("Write your first name?").upper()
        out_list = [word_dict[letter] for letter in list(name)]
    except FileNotFoundError as msg:
        print(msg)
    except KeyError:
        print('Sorry only letters in the alphabet please')
    else:
        print(out_list)
        running = False
# print([code for (letter, code) in word_dict.items() if letter in list(name)])
