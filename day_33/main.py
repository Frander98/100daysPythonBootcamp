import requests
import smtplib
import time

MY_CORD = (10.4564, -84.5538)
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_position = (longitude, latitude)

my_email = "francalvr@outlook.com"
password = "LosAngeles123"


while True:
    time.sleep(15)
    if MY_CORD == iss_position:
        with smtplib.SMTP("outlook.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="franderadriel1998@gmail.com",
                msg=f"Subject:ISS position\n\nThe ISS is just above you, look up to the sky and see."
            )
    else:
        with smtplib.SMTP("outlook.office365.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="franderadriel1998@gmail.com",
                msg=f"Subject:ISS position\n\nThe ISS is in coordinates {iss_position}."
            )
