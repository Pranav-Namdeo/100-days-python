##################### Extra Hard Starting Project ######################

from email.utils import quote
import smtplib
import datetime as dt
import random
import pandas

# 1. Update the birthdays.csv

birthdays = pandas.read_csv("D:/Code/100 days python/day 32/bday wisher/birthdays.csv")

my_email = "kiromaster0@gmail.com"
password = "xznn lwhd hffh eizz"

# 2. Check if today matches a birthday in the birthdays.csv

current_month = dt.datetime.now().month
current_day = dt.datetime.now().day
for index, row in birthdays.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        name = row["name"]
        email = row["email"]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        letter_path = f"D:/Code/100 days python/day 32/bday wisher/letter_templates/letter_{random.randint(1,3)}.txt"
        with open(letter_path) as letter_file:
            letter_contents = letter_file.read()
            letter_contents = letter_contents.replace("[NAME]", name)
            print(letter_contents)

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{letter_contents}")




