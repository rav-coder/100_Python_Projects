
import pandas

data = pandas.read_csv('226 weather-data.csv')
# print(data)
# print(data['temp'])
# print(type(data))
# print(type(data['temp']))

data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].tolist()
# print(temp_list)
# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)
# print(data['temp'].mean())
#
# # Data in columns
# print(data['temp'].max())
# print(data.temp)  # case matters
#
# # Get data in row
# # print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday.condition)

data_dict = {
    'students': ['q', 'r', 's'],
    'scores': [2, 3, 4]
}

student_data = pandas.DataFrame(data_dict)
print(student_data)
student_data.to_csv('grades.csv')


# with open('226 weather-data.csv') as weather_data:
#     data = weather_data.readlines()
#     print(data[1:])

# import csv
# with open('226 weather-data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     # print(data)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if temp.isnumeric():
#             temperatures.append(int(temp))
#         # print(row)
#
#     print(temperatures)
