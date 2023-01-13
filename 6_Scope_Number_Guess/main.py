
import random
from art import logo

num_list = [val for val in range(1,101)]

magic_number = random.choice(num_list)

print(logo)
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    run = 10
elif difficulty == 'hard':
    run = 5

for index in range(run):
    print(f"You have {run-index} attempts remaining to guess the number.")
    user_select = int(input("Make a guess: "))

    if user_select == magic_number:
        print(f"You win! The number was {magic_number}")
        break
    elif user_select < magic_number:
        print("Too low.")
    elif user_select > magic_number:
        print("Too high.")
else:
    print(f"You lose. The number was {magic_number}")

