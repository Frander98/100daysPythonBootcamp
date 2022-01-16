# Working with csv data
import pandas

# import csv
#
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # data_temp_list = data["temp"].to_list()
# # max_temp = data["temp"].max()
# # print(max_temp)
# monday = data[data.day == "Monday"]
# monday_c_temp = int(monday.temp)
# print((monday_c_temp * 9/5) + 32)


file_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
new_squirrel_data = pandas.DataFrame(file_data)
new_squirrel_data.to_csv("new_sqrell_data.csv")
gray_squirrels_total = len(new_squirrel_data[new_squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_total = len(new_squirrel_data[new_squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_total = len(new_squirrel_data[new_squirrel_data["Primary Fur Color"] == "Black"])


data_dict = {
    "Primary Fur Color": ["Gray", "Red", "Black"],
    "Quantity": [gray_squirrels_total, red_squirrels_total, black_squirrels_total]
}
data_frame = pandas.DataFrame(data_dict)
output_data = pandas.DataFrame(data_frame)
output_data.to_csv("output_data.csv")