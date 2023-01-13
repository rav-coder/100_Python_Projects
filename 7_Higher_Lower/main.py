from game_data import data
import random

guess_bool = True
current_score = 0
print("Higher Lower game")
first_choice_dict = random.choice(data)

def character_info(char_dict):
    return f"{char_dict['name']}, a {char_dict['description']}, from {char_dict['country']}."

def get_follower_count(char_dict):
    return char_dict["follower_count"]

def correct_guess(dict_A,dict_B,guess):
    if guess == 'A':
        if get_follower_count(dict_A) > get_follower_count(dict_B):
            return True
    if guess == 'B':
        if get_follower_count(dict_B) > get_follower_count(dict_A):
            return True
    return False

while guess_bool:

    print(f"Compare A: {character_info(first_choice_dict)}")

    print("Vs.")

    second_choice_dict = random.choice(data)

    if first_choice_dict == second_choice_dict:
        second_choice_dict = random.choice(data)

    print(f"Against B: {character_info(second_choice_dict)}")

    user_select_str = input("Who has more followers? Type 'A' or 'B': ").upper()

    guess_bool = correct_guess(first_choice_dict,second_choice_dict,user_select_str)

    if guess_bool:
        current_score+=1
        print(f"You're right. Current Score: {current_score}")
        print("-----")
        if user_select_str == 'B':
            first_choice_dict = second_choice_dict
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")


