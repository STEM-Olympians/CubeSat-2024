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

#AUTHOR: 
#DATE:

#import libraries
import time
import board
from adafruit_lsm6ds.lsm6dsox import LSM6DSOX as LSM6DS
from adafruit_lis3mdl import LIS3MDL
from picamera2 import Picamera2
from queue import Queue

#VARIABLES
THRESHOLD = 0      #Any desired value from the accelerometer
REPO_PATH = "/home/olympians/Olympian"     #Your github repo path: ex. /home/pi/FlatSatChallenge
FOLDER_PATH = "Images"   #Your image folder path in your GitHub repo: ex. /Images

queue = Queue()
#imu and camera initialization
i2c = board.I2C()
#accel_gyro = LSM6DS(i2c)
#mag = LIS3MDL(i2c)
picam2 = Picamera2()


def img_gen(name):
    """
    This function is complete. Generates a new image name.

    Parameters:
        name (str): your name ex. MasonM
    """
    t = time.strftime("_%H%M%S")
    imgname = (f'{REPO_PATH}/{FOLDER_PATH}/{name}{t}.jpg')
    return imgname


def take_photo():
    """
    This function is NOT complete. Takes a photo when the FlatSat is shaken.
    Replace psuedocode with your own code.
    """
    while True:
        # accelx, accely, accelz = accel_gyro.acceleration

        #CHECKS IF READINGS ARE ABOVE THRESHOLD
            #PAUSE


        name = "Aerodynamic Grapefuits^3"

        filePath = img_gen(name)

        picam2.start_and_capture_file(filePath)
            #TAKE PHOTO
            #PUSH PHOTO TO GITHUB
        
        #PAUSE

        return filePath


def transmit_photo(filePath):
    # decode img from file
    # convert to byte stream
    # use stream to transmit data over bluetooth

    return False


def main():
    # while true, follow state machine
    time.sleep(3)
     # FIXME: queue.add(take_photo())
    
    queue.put(take_photo())
    # maybe transmit photo on different thread?

    # there's a lot of asynchronous stuff going on here...



if __name__ == '__main__':
    main()