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
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./day 25/new_data.csv")
