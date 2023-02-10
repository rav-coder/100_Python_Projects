# import smtplib
#
# my_email = "email"
# password = "pass"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="email",
#         msg="Subject:Hello\n\n"
#             "This is the body of the email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# print(now.year)
# print(now.weekday())
#
# if now.year == 2023:
#     print(now)
#
# dob = dt.datetime(year=1820, month=2, day=2, hour=18)
# print(dob)
