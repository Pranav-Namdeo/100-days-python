import smtplib
import datetime as dt
import random

my_email = "kiromaster0@gmail.com"
password = "xznn lwhd hffh eizz"

with open("D:/Code/100 days python/day 32/quotes.txt") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotes)

day_of_week = dt.datetime.now().weekday()

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="anaynamdeo18@gmail.com", msg=f"Subject:Motivation Quote!\n\n{quote}")
