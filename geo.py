import googlemaps
from datetime import datetime
import math

import Config

gmaps = googlemaps.Client(key=Config.publicKey)

# Geocoding an address
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
address = 'Times Square, NY'
geocode_result = gmaps.geocode(address)

lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']
print(f"Geocode Results for Lillly's Address: Latitude={lat}; Longitude={lng}")
print("\n")

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((lat, lng))
# print(f"Reversed Geocode: {reverse_geocode_result}")

# # Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Burlingame Main Public Library, CA",
#                                      address,
#                                      mode="walking",
#                                      departure_time=now)

# steps = directions_result[0]['legs'][0]['steps']
# instructions = [step['html_instructions'] for step in steps]
# print("Direction Results to Lillly's Address from Burlingame Public Library: ",)
# for instruction in instructions:
#     print(f"\t{instruction}")
# print("\n")

# # Validate an address with address validation
# addressvalidation_result =  gmaps.addressvalidation([address], 
#                                                     regionCode='US',
#                                                     locality='Burlingame', 
#                                                     enableUspsCass=True)
# valid_confirmation = addressvalidation_result['result']['address']['addressComponents'][0]['confirmationLevel']
# print(f"Is Lillly's House a Valid Address: {valid_confirmation}")

inclination = 51
earthRadius = 6366707.0195
altitude = 450000
orbitRadius = earthRadius + altitude
earthCircumference = 2 * math.pi * earthRadius
orbitCircumference = 2 * math.pi * orbitRadius

# Arclength / circumference * 360 degrees = the degree change
satVelocity = 7666.11111111
dTheta = satVelocity / orbitCircumference * 360

# Calculate the rate of change in ground location as the Cubesat flies over
groundVelocity = dTheta * orbitCircumference / 360

# The degree direction of the Cubesat, measured from North, assuming in the same direction as the 7th Avenue for our demo
# cos(-150 degrees from North) = sin(240 degrees from the horizon)
heading = -150.77531380391113
lng_change_rate = math.sin(math.radians(heading))
lat_change_rate = math.cos(math.radians(heading))

def geo_step(dt):
    location = "Times Square, New York"
    ds = groundVelocity * dt # Assuming CubeSat moving in the direction of 7th avenue, which in real-life is dynamic
    
    start_geocode = gmaps.geocode(location)
    start_lat = geocode_result[0]['geometry']['location']['lat']
    start_lng = geocode_result[0]['geometry']['location']['lng']

    current_lat = start_lat + lat_change_rate * dt
    current_lng = start_lng + lng_change_rate * dt

    return (current_lat, current_lng)
