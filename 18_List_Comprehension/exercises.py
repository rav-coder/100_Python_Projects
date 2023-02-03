# LIST COMPREHENSION
import random
import pandas

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = [num*2 for num in numbers]
# new_list_2 = [num+1 for num in numbers]
# print(new_list)
# print(new_list_2)
#
# name = 'testing'
# new_list_3 = [letter for letter in name]
# print(new_list_3)
#
# new_list_4 = [i*2 for i in range(1, 6)]
# print(new_list_4)
#
# new_list_5 = [num for num in numbers if num % 2 == 0]
# print(new_list_5)
#
# new_6 = [num**2 for num in numbers]
# print(new_6)

with open('file1.txt') as data:
    list_1 = [int(line.strip('\n')) for line in data.readlines()]

with open('file2.txt') as data:
    list_2 = [int(line.strip('\n')) for line in data.readlines()]

result = [num for num in list_1 if num in list_2]
print(result)

# DICTIONARY COMPREHENSION
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

names = ['alex', 'matt', 'john', 'max']
students_score = {name: random.randint(1, 4) for name in names}
print(students_score)

passed_students = {name: score for (name, score) in students_score.items() if score > 2}
print(passed_students)

sentence = 'this is for testing dict comprehension'
sen_dict = {word: len(word) for word in sentence.split(' ')}
print(sen_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

student_dict = {
    'student': ['alex', 'matt', 'john', 'max'],
    'score': [1, 2, 3, 4]
}
df = pandas.DataFrame(student_dict)
# print(df)

for (index, row) in df.iterrows():
    # print(row)
    print(row.student)
