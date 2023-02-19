import requests
from decouple import config
from twilio.rest import Client


class NotificationManager:

    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    FROM_NUM = config('TWILIO_PHONE_NUM')
    TO_NUM = config('MOBILE_NUM')

    def send_msg_flight(self, flight_data):
        message = f"Low Price Alert! \n\n" \
                  f"Flight from {flight_data.get('from')} to {flight_data.get('to')} found for " \
                  f"{flight_data.get('price')} {flight_data.get('currency')}\n\n" \
                  f"Local Depart Time: {flight_data.get('local_departure')}\n\n" \
                  f"Url: {flight_data.get('link')}"
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=message,
            from_=self.FROM_NUM,
            to=self.TO_NUM,
        )
        print(message.status)
