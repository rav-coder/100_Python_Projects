import datetime as dt
import random, smtplib

if dt.datetime.now().weekday() == 0:
    with open('quotes.txt', "r") as quotes_file:
        quotes = quotes_file.readlines()
        quote_of_the_day = random.choice(quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user="email", password="pass")
        connection.sendmail(
            from_addr="email",
            to_addrs="email",
            msg=f"Subject:Quote for the day\n\n"
                f"{quote_of_the_day}"
        )
