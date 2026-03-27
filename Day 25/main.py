import pandas


data = pandas.read_csv("./day 25/weather_data.csv")
print(data["temp"])

avg_temp = data["temp"].mean()
#print(avg_temp)

max_temp = data["temp"].max()
print(max_temp)

# Get data in rows

print(data[data.temp == max_temp])
