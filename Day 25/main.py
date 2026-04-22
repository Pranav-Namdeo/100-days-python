import pandas

#data = pandas.read_csv("./day 25/weather_data.csv")
#print(data["temp"])
#
#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data["temp"].to_list()
#print(temp_list)
#
#print(data["temp"].mean())
#print(data["temp"].max())
#
#print(data[data.day == "Monday"])
#
#print(data[data.temp == data.temp.max()])
#
#monday = data[data.day == "Monday"]
#monday_temp = monday.temp * 9/5 + 32
#print(monday_temp)

# create a dataframe from scratch
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}
#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("./day 25/new_data.csv")


data = pandas.read_csv("./day 25/Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
squirrels_data = pandas.DataFrame(data_dict)
squirrels_data.to_csv("./day 25/squirrels_count.csv")
print(squirrels_data)
