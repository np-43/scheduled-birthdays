# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
import pandas
import smtplib
import datetime as dt
import random

##################### Extra Hard Starting Project ######################

sender_email = os.environ.get("MY_EMAIL")
sender_password = os.environ.get("MY_PASSWORD")

# 1. Update the birthdays.csv

data_frame = pandas.read_csv("birthdays.csv")
birthdays = data_frame.to_dict("records")

today = dt.datetime.now()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def get_random_letter(name):
    letter_number = random.randint(1, 3)
    filename = f"letter_templates/letter_{letter_number}.txt"
    with open(filename, "r") as f:
        letter = f.read()
        letter = letter.replace("[NAME]", name)
    return letter


# 4. Send the letter generated in step 3 to that person's email address.
def send_email(to, content):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(sender_email, sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=to,
            msg=f"Subject: Happy Birthday!\n\n{content}"
        )

# 2. Check if today matches a birthday in the birthdays.csv

today_birthdays = [birthday for birthday in birthdays if birthday["month"] == today.month and birthday["day"] == today.day]

for birthday in today_birthdays:
    letter = get_random_letter(birthday["name"])
    send_email(birthday["email"], letter)
