from decouple import config
import requests


class FlightSearch:

    FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/"
    HEADER = {
        "apikey": config("FLIGHT_API_KEY"),
    }

    def __init__(self):
        pass

    def get_iata_city_code(self, city):

        location_params = {
            "term": city,
            "location_types": "city",
        }

        location_endpoint = self.FLIGHT_ENDPOINT + "locations/query"
        response = requests.get(url=location_endpoint, params=location_params, headers=self.HEADER)

        return response.json().get("locations")[0].get("code")

    def get_flights_data(self, flight_params):
        flight_search_url = self.FLIGHT_ENDPOINT + "v2/search"
        response = requests.get(url=flight_search_url, params=flight_params, headers=self.HEADER)
        return response.json()



