#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
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

for val in sheet_data.get("prices"):
    flight_params = {
        "fly_from": f"city:{flight_start_code}",
        "fly_to": f"city:{val.get('iataCode')}",
        "date_from": TODAY_DATE,
        "date_to": SIX_MONTHS_FROM_TODAY,
        "curr": CURRENCY,
        "price_to": val.get("lowestPrice"),
    }

    flight_json = flight_search.get_flights_data(flight_params)
    data_to_sms = flight_data.structured_flight_data(flight_json)
    # print(data_to_sms)

    if data_to_sms:
        notification.send_msg_flight(data_to_sms)

