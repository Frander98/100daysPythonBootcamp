# How to send emails using SMTP library
import smtplib
import datetime as dt
import random


now = dt.datetime.now()
year = now.year
weekday = now.weekday()
# date_of_birth = dt.datetime(year=1998, month=1, day=30, hour=13)
if weekday == 1:
    with open("quotes.txt", "r") as motivational_quotes:
        list_of_quotes = motivational_quotes.readlines()
        quote = random.choice(list_of_quotes)

    my_email = "francalvr@outlook.com"
    password = "LosAngeles123"
    with smtplib.SMTP("outlook.office365.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="franderadriel1998@gmail.com",
            msg=f"Subject:Cita motivacional\n\n{quote}\nFrom Frander, to Frander. Dear, you're doing great. "
                f"with Python."
                f"Dear, you're doing great."
        )





