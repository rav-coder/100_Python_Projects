# FIleNotFound Error
# with open('a_file.txt') as file:
#     file.read()

try:
    file = open('a_file.txt')
    a_dict = {'key': 'value'}
    print(a_dict['key'])
except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write("Testing")
except KeyError as error_message:
    print(f'That key {error_message} is non-existent')
else:
    print(file.read())
finally:
    # raise TypeError("Make up error")
    file.close()
    print('File closed.')


# Raise your own exception
height = float(input('Height: '))
weight = float(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not be above 3 meters.')

bmi = weight / height ** 2
print(bmi)

# # Key Error
# in dictionary when key specified does not exist
#

# #Index Error
# when index we are trying to get is out of range


# Type Error
# text = 'abc'
# print(text + 5) # TypeError: can only concatenate str (not "int") to str
