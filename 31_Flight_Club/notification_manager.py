import requests
from decouple import config
from twilio.rest import Client
import smtplib


class NotificationManager:
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    FROM_NUM = config('TWILIO_PHONE_NUM')
    TO_NUM = config('MOBILE_NUM')
    USER = config("GMAIL_NAME")
    PASS = config("GMAIL_PASS")

    def send_msg_flight(self, flight_data):
        message = f"Low Price Alert! \n\n" \
                  f"Flight from {flight_data.get('from')} to {flight_data.get('to')} found for " \
                  f"{flight_data.get('price')} {flight_data.get('currency')}\n\n" \
                  f"Local Depart Date: {flight_data.get('local_departure')}\n\n" \
                  f"Return Date: {flight_data.get('return_date')}\n\n" \
                  f"Url: {flight_data.get('link')}"
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=message,
            from_=self.FROM_NUM,
            to=self.TO_NUM,
        )
        print(message.status)

    def send_email_to_club(self, flight_data, user):
        to_email = user.get("email")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.USER, password=self.PASS)
            letter_body = flight_data
            connection.sendmail(
                from_addr=self.USER,
                to_addrs=to_email,
                msg=f"Subject:Low Flight Price Alert!\n\n" \
                    f"Dear {user.get('firstName')} {user.get('lastName')},\n\n" \
                    f"{letter_body}"
            )
