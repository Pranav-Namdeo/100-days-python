import csv

with open("./day 25/weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
