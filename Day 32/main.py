import smtplib

my_email = "kiromaster0@gmail.com"
password = "xznn lwhd hffh eizz"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="anaynamdeo18@gmail.com", msg="Subject:Hello!\n\nThis is the body of my email.")
