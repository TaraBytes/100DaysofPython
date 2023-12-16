import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 47.606209
MY_LNG = -122.332069
my_email = "emailgoeshere@gmail.com"
password = "passwordgoeshere"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # response codes: https://www.webfx.com/web-development/glossary/http-status-codes/
    # # 1XX - hold on,
    # # 2XX - successful,
    # # 3XX - invalid perm,
    # # 4XX - doesn't exist, user side error
    # # 5XX - server side error
    # print(response.status_code)
    response.raise_for_status()
    data = response.json()["iss_position"]

    iss_longitude = float(data["longitude"])
    iss_latitude = float(data["latitude"])
    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LNG - 5 < iss_longitude < MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lmg": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if sunset < time_now < sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )
