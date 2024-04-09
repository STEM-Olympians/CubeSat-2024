"""
The Python code you will write for this module should read
acceleration data from the IMU. When a reading comes in that surpasses
an acceleration threshold (indicating a shake), your Pi should pause,
trigger the camera to take a picture, then save the image with a
descriptive filename. You may use GitHub to upload your images automatically,
but for this activity it is not required.

The provided functions are only for reference, you do not need to use them. 
You will need to complete the take_photo() function and configure the VARIABLES section
"""

import os
import time
import board
# from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS
# from adafruit_lis3mdl import LIS3MDL
from picamera2 import Picamera2, Preview

import Config
from Geo import geo_step

#VARIABLES
THRESHOLD = 0      #Any desired value from the accelerometer
REPO_PATH = "/home/olympians/Olympian"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = Config.directory_to_read   #Your image folder path in your GitHub repo: ex. /Images

# IMU and camera initialization
# i2c = board.I2C()
# accel_gyro = LSM6DS(i2c)
# mag = LIS3MDL(i2c)
picam2 = Picamera2()

def img_path_gen(name):
    """
    This function is complete. Generates a new image name.

    Parameters:
        name (str): your name ex. MasonM
    """
    t = time.strftime("%H%M%S_")
    imgname = t + name

    save_dir = os.path.join(REPO_PATH, FOLDER_PATH)
    imgPath = (f'{os.path.join(save_dir, imgname)}.jpg')

    return imgPath

def take_photo():
    """
    This function is NOT complete. Takes a photo when the FlatSat is shaken.
    Replace psuedocode with your own code.
    """
    t0 = time.time()
    time_limit = 3.6
    # Captures approximately 3 pictures~

    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    
    picam2.start_preview(Preview.QT)
    picam2.start()

    while True:
        dt = time.time() - t0
        # accelx, accely, accelz = accel_gyro.acceleration
        # print(f"Acceleration X-axis: {accelx}")
        # print(f"Acceleration Y-axis: {accely}")
        # print(f"Acceleration Z-axis: {accelz}")

        current_lat, current_lng = geo_step(dt)
        filepath = img_path_gen(f"{current_lat}*{current_lng}")
        print(filepath)
        picam2.capture_file(filepath)

        time.sleep(0.6)

        if dt >= time_limit:
            break

    picam2.stop_preview()
    picam2.stop()

    print("PICTURES COMPLETED~")
    
        
def nominal():
    take_photo()
