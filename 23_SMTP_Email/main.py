import datetime as dt
import pandas
import random
import smtplib

MONTH = "month"
DAY = "day"
NAME = "name"
EMAIL = "email"


# 2. Check if today matches a birthday in the birthdays.csv
def check_if_birthday():
    try:
        bd_file = pandas.read_csv("birthdays.csv")
    except FileNotFoundError as fe_:
        print(fe_)
    else:
        bd_list = bd_file.to_dict(orient="records")

        current_month = dt.datetime.now().month
        current_day = dt.datetime.now().day

        for bd_dict in bd_list:
            if bd_dict.get(MONTH) == current_month and bd_dict.get(DAY) == current_day:
                return bd_dict

    return False


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
matched_bd = check_if_birthday()
if matched_bd:
    name = matched_bd.get(NAME)
    to_email = matched_bd.get(EMAIL)
    letter_num = random.randint(1, 3)

    try:
        with open(f"letter_templates/letter_{letter_num}.txt", "r") as letter:
            letter_body = letter.read().replace("[NAME]", name)
    except FileNotFoundError as fe:
        print(fe)
    else:
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user="email", password="pass")
            connection.sendmail(
                from_addr="email",
                to_addrs=to_email,
                msg=f"Subject:Happy Birthday!\n\n"
                    f"{letter_body}"
            )

