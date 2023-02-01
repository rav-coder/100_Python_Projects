
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

NAME_PLACEHOLDER = '[name]'

with open('./Input/Letters/starting_letter.txt', mode='r') as in_file:
    letter = in_file.read()

with open('./Input/Names/invited_names.txt', mode='r') as in_file:
    names = in_file.readlines()

for name in names:
    new_name = name.strip('\n')
    with open(f"./Output/ReadyToSend/out_{new_name}.txt", mode='w') as out_file:
        out_file.writelines(letter.replace(NAME_PLACEHOLDER, new_name))
