import pandas as pd
import datetime as dt
from random import randint
import smtplib

my_email = "myemailgoeshere@gmail.com"
password = "passwordgoeshere"

now = dt.datetime.now()
today = (now.month, now.day)

bdays = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in bdays.iterrows()}
print(birthdays_dict)

if today in birthdays_dict:
    chosen_letter = f"./letter_templates/letter_{randint(1, 3)}.txt"
    with open(chosen_letter, "r") as letter:
        contents = letter.read()
        filled_letter = contents.replace("[NAME]", birthdays_dict[today]["name"])
        print(filled_letter)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthdays_dict[today]["email"],
                msg=f"Subject:Happy Birthday\n\n{filled_letter}"
            )
