import time
import math
# import googlemaps
from picamera2 import Picamera2, Preview

import Config
from Nominal import take_photo

# gmaps = googlemaps.Client(key=Config.publicKey)


# lat0 = 40.758924
# lng0 = -73.985787
# lat1 = 40.758094
# lng1 = -73.98613499999999
# lat2 = 40.757216
# lng2 = -73.986391

# dlat = lat1 - lat0
# dlng = lng1 - lng0
# print(dlat)

# earthRadius = 6366707.0195
# latRadian = math.radians(dlat)
# lngRadian = math.radians(dlng)

# latLength = earthRadius * latRadian
# lngLength = earthRadius * lngRadian

# print(latLength)
# print(lngLength)

# demoVel = math.sqrt(latLength ** 2 + lngLength ** 2)
# print(demoVel)

t0 = time.time()

#VARIABLES
THRESHOLD = 0      #Any desired value from the accelerometer
REPO_PATH = "/home/olympians/Olympian"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = Config.directory_to_read   #Your image folder path in your GitHub repo: ex. /Images

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)

picam2.start()

while True:
    current_lat, current_lng = geo.geo_step(dt)
    filepath = img_path_gen(f"{current_lat}/{current_lng}")
    print(filepath)
    picam2.capture_file(filepath)

    # time.sleep(2)

    dt = time.time() - t0
    print("Change in Time: ", dt)