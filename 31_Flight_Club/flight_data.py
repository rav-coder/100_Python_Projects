class FlightData:
    def __init__(self):
        pass

    def structured_flight_data(self, flight_data):

        if flight_data.get("data"):
            first_flight = flight_data.get("data")[0]
            return {
                "currency": flight_data.get("currency"),
                "price": first_flight.get("price"),
                "from": f"{first_flight.get('cityFrom')}-{first_flight.get('flyFrom')}",
                "to": f"{first_flight.get('cityTo')}-{first_flight.get('flyTo')}",
                "local_departure": first_flight.get('local_departure').split("T")[0],
                "return_date":  first_flight["route"][-1]["local_departure"].split("T")[0],
                "link": first_flight.get('deep_link'),
            }
        else:
            return False
