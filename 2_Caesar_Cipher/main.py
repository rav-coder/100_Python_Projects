
end = False

ENCODE = 'encode'
DECODE = 'decode'

def caeser(user_input, msg,shift):
    
    out_msg = ''

    if user_input == DECODE:
        shift = -shift

    for char in msg:
        if char == ' ':
            out_msg += ' '
        elif char.islower():
            out_msg += chr( (ord(char) + shift - 97) % 26 + 97) # ASCII value: A is 65 and a is 97
        else:
            out_msg += chr( (ord(char) + shift - 65) % 26 + 65)
    
    return out_msg

while not end:
    
    user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

    if user_input in (ENCODE,DECODE):
        message = input("Type your message: \n")

        shift = int(input("Type the shift number: \n"))

        out_msg = caeser(user_input,message,shift)
        
        print("Here is the message " + user_input + "ed: " + out_msg)

        # print(f"Here is the message {user_input}ed: {out_msg}")
    else:
        print("Invalid input. Please try again.")


# end = False

# ENCODE = 'encode'
# DECODE = 'decode'

# def encode(msg,shift):
#     out_msg = ''

#     for char in msg:
#         if char == ' ':
#             out_msg += ' '
#         elif char.islower():
#             out_msg += chr( (ord(char) + shift - 97) % 26 + 97) # ASCII value: A is 65 and a is 97
#         else:
#             out_msg += chr( (ord(char) + shift - 65) % 26 + 65)
#     return out_msg

# def decode(msg,shift):
#     out_msg = ''

#     for char in msg:
#         if char == ' ':
#             out_msg += ' '
#         elif char.islower():
#             out_msg += chr( (ord(char) - shift - 97) % 26 + 97)
#         else:
#             out_msg += chr( (ord(char) - shift - 65) % 26 + 65)
#     return out_msg

# while not end:
#     user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

#     if user_input == ENCODE or user_input == DECODE:
#         message = input("Type your message: \n")

#         shift = int(input("Type the shift number: \n"))

#         out_msg = ''

#         if user_input == ENCODE:
#             out_msg = encode(message,shift)
#         elif user_input == DECODE:
#             out_msg = decode(message,shift)
        
#         print("Here is the message " + user_input + "ed: " + out_msg)

#         # print(f"Here is the message {user_input}ed: {out_msg}")
#     else:
#         print("Invalid input. Please try again.")