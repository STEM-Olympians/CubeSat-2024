import googlemaps
from datetime import datetime

import Config

gmaps = googlemaps.Client(key=Config.publicKey)

# Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
address = '1901 Hillside Drive, Burlingame, CA'
geocode_result = gmaps.geocode(address)

lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']
print(f"Geocode Results for Lillly's Address: Latitude={lat}; Longitude={lng}")
print("\n")

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Burlingame Main Public Library, CA",
                                     address,
                                     mode="walking",
                                     departure_time=now)

steps = directions_result[0]['legs'][0]['steps']
instructions = [step['html_instructions'] for step in steps]
print("Direction Results to Lillly's Address from Burlingame Public Library: ",)
for instruction in instructions:
    print(f"\t{instruction}")
print("\n")

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation([address], 
                                                    regionCode='US',
                                                    locality='Burlingame', 
                                                    enableUspsCass=True)
valid_confirmation = addressvalidation_result['result']['address']['addressComponents'][0]['confirmationLevel']
print(f"Is Lillly's House a Valid Address: {valid_confirmation}")

inclination = 51
velocity = 7666.11111111


