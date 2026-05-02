#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data.day[0]))
#
# max_tmp = data.temp.max()
# print(data[data.temp == max_tmp])
#
# data_dict = {
#     "student": ["Amy", "James", "Ngoc"],
#     "score": [3, 5, 9]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("student.csv")
import numpy as np
import pandas
data = pandas.read_csv('Squirrel_Data.csv')
all_colors = data["Primary Fur Color"]
all_colors = set(all_colors)
arr_colors = []
arr_counts = []


for color in all_colors:
    arr_colors.append(color)
    if pandas.isnull(color):
        arr_counts.append(len(data[pandas.isnull(data["Primary Fur Color"])]))
    else:
        arr_counts.append(len(data[data["Primary Fur Color"] == color]))

print(arr_colors)
print(arr_counts)
data_dict = {
    "colors": arr_colors,
    "count": arr_counts
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel.csv")