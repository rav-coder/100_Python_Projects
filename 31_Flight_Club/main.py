# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

FLIGHT_START_CITY = "Calgary"
CURRENCY = "CAD"
TODAY_DATE = datetime.today().strftime("%d/%m/%Y")
SIX_MONTHS_FROM_TODAY = (datetime.today() + timedelta(days=180)).strftime("%d/%m/%Y")

flight_search = FlightSearch()
data_manager = DataManager()
flight_data = FlightData()
notification = NotificationManager()
sheet_data = data_manager.get_sheet()
flight_start_code = flight_search.get_iata_city_code(FLIGHT_START_CITY)


#### Add user to flight club
# def flight_club():
#     print("Welcome to the Flight Club!")
#     print("We email the best flight deals to you.")
#     f_name = input("What is your first name?").title()
#     l_name = input("What is your last name?").title()
#     running = True
#
#     while running:
#         email_f = input("What is your email?").lower()
#         email_s = input("Please confirm your email.").lower()
#
#         if email_f == email_s:
#             row_data = {
#                 "user": {
#                     "firstName": f_name,
#                     "lastName": l_name,
#                     "email": email_s,
#                 }
#             }
#             data_manager.add_user(row_data)
#             print("You are in the club!")
#             running = False
#         else:
#             print("Email did not match. Please retry!")
#             running = True
#
#
# flight_club()

#### Find iota code from city name
def add_iota_code_for_city_name():
    for val_flight in sheet_data.get("prices"):
        if val_flight.get("iataCode") == '':
            city_code = flight_search.get_iata_city_code(val_flight.get("city"))
            row_id = val_flight.get("id")
            row_data = {
                "price": {
                    "iataCode": city_code,
                }
            }

            data_manager.update_row(row_id, row_data)


add_iota_code_for_city_name()

#### SEND email or SMS
email_message = ""

for val in sheet_data.get("prices"):
    flight_params = {
        "fly_from": f"city:{flight_start_code}",
        "fly_to": f"city:{val.get('iataCode')}",
        "date_from": TODAY_DATE,
        "date_to": SIX_MONTHS_FROM_TODAY,
        "nights_in_dst_from": 10,
        "nights_in_dst_to": 15,
        "curr": CURRENCY,
        "price_to": val.get("lowestPrice"),
        "flight_type": "round",
    }

    flight_json = flight_search.get_flights_data(flight_params)
    # print(flight_json)
    data_to_sms = flight_data.structured_flight_data(flight_json)
    # print(data_to_sms)

    if data_to_sms:
        # notification.send_msg_flight(data_to_sms)
        email_message += f"-------\n\n" \
                  f"Flight from {data_to_sms.get('from')} to {data_to_sms.get('to')} found for " \
                  f"{data_to_sms.get('price')} {data_to_sms.get('currency')}\n\n" \
                  f"Local Depart Date: {data_to_sms.get('local_departure')}\n\n" \
                  f"Return Date: {data_to_sms.get('return_date')}\n\n" \
                  f"See Deal: {data_to_sms.get('link')}\n\n"

all_users = data_manager.get_users_sheet().get("users")
email_message += f"Regards - SA Flight Club"
# print(email_message)

for user in all_users:
    notification.send_email_to_club(email_message, user)
