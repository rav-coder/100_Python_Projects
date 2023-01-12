import random

run = 'y'

LOWER_LIMIT = 1
UPPER_LIMIT = 10
MAGIC_NUMBER = 21

class MyRand(object):
    def __init__(self):
        self.last = None

    def __call__(self):
        r = random.randint(LOWER_LIMIT,13)
        while r == self.last:
            r = random.randint(LOWER_LIMIT,13)
        self.last = r
        return r

randint = MyRand()

def add_card(in_list):
    card = random.randint(LOWER_LIMIT,13)

    if card > UPPER_LIMIT:
        card = UPPER_LIMIT

    in_list.append(card)

def sum_cards(in_list):
    sum = 0

    for index in range(len(in_list)):
        sum += in_list[index]
    
    return sum

def user_winner(in_dict):
    if in_dict["user_sum"] > MAGIC_NUMBER:
        return 'n'
    elif in_dict["computer_sum"] > MAGIC_NUMBER:
        return 'y'
    elif in_dict["user_sum"] == in_dict["computer_sum"]:
        return 'd'
    elif (UPPER_LIMIT - in_dict["user_sum"]) < (UPPER_LIMIT - in_dict["computer_sum"]):
        return 'y'
    else:
        return 'n'

def ace_value_picker(in_list):
    for index in range(len(in_list)):
        if in_list[index] == 1:
            sum = 10 + sum_cards(in_list)
            if sum < MAGIC_NUMBER:
                in_list[index] == 11
                break

while run == 'y':

    run = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if run == 'n':
        break

    user_card_list = []
    computer_card_list = []
    card_sum = {
        "user_sum":0,
        "computer_sum":0,
    }

    for _ in range(0,2):
        add_card(user_card_list)

    add_card(computer_card_list)

    print(f"Your cards: {user_card_list}")
    print(f"Computer's first card: {computer_card_list[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == 'y':
        add_card(user_card_list)
    
    add_card(computer_card_list)

    if sum_cards(computer_card_list) < 17:
        add_card(computer_card_list)

    card_sum["computer_sum"] = sum_cards(computer_card_list)
    card_sum["user_sum"] = sum_cards(user_card_list)

    ace_value_picker(user_card_list)
    ace_value_picker(computer_card_list)

    print(f"Your final hand: {user_card_list}")
    print(f"Computer's final hand: {computer_card_list}")

    if user_winner(card_sum) == 'y':
        print("You Win!")
    elif user_winner(card_sum) == 'n':
        print("Computer Wins!")
    else:
        print("Draw!")

    







