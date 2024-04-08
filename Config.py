from enum import IntEnum


# Where you want to store all your images (on your laptop)
# This will be in local directory of the repo 
directory_to_write = "Uploads/"

# Directory images should be read from on the PI
# (shouldn't have to change this one unless something changes on the PI)
directory_to_read= "Images/"

# Bluetooth address of your server
# You can find this by running hciconfig
# It will return a list of connected devices (your laptop)
# Copy and paste that address here
server_bluetooth_address = 'D8:3A:DD:8E:CE:FA'
client_bluetooth_address = '10:9F:41:C0:9E:E6'

# Geolocation API
publicKey = 'AIzaSyBnVRLDNtY07sCicWFoXdmVLn07G-hXDso'

# Port: Any number that is not being used by another service
PORT = 1

# CubeSat Modes
class Mode(IntEnum):
    NOMINAL=0
    COMM=1
    SLEEP=2