import pandas

data = pandas.read_csv('228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')

color = "Primary Fur Color"
# print(data.PrimaryFurColor)
# print(data[color])

color_count_dict = {
    'Fur Color': ['gray', 'red', 'black'],
    'Count': [len(data[data[color] == 'Gray']), len(data[data[color] == 'Cinnamon']),
              len(data[data[color] == 'Black'])]
}

pandas.DataFrame(color_count_dict).to_csv('color.csv')
