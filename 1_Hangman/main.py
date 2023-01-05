
# from hangman_words import word_list, ...

word_list = ['runner','cable','drivers','checkboard']

import random

chosen_word = random.choice(word_list)

# print("the word is: " + chosen_word)

display_list = list(map(lambda num:'_',chosen_word))

end_game = False

count = 6

while not end_game:

    user_guess = input("Pls guess a letter: ").lower()

    if user_guess not in chosen_word:
        count -= 1
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_guess:
                display_list[i] = chosen_word[i]

    # for letter in chosen_word:
    #     if letter == user_guess:
    #         print("Correct")
    #     else:
    #         print("Incorrect")

    # print(display_list)

    print(f"{' '.join(display_list)}")

    if '_' not in display_list:
        end_game = True
        print("You Won!")
    elif count==0:
        end_game = True
        print("You Lost!")
    else:
        print("You have " + str(count) + " lives remaining.")
