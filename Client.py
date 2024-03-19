"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""

import socket
import time

from os import listdir
from os.path import isfile, join

# Calculate the start time
start = time.time()

serverMACAddress = 'A4:C3:F0:51:C0:AB'
port = 6
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

image_folder_path = "/home/olympians/Olympian/Images/"
imgs = [img for img in listdir(image_folder_path) if isfile(join(image_folder_path, img))]

for img_name in imgs :
   
   print(image_folder_path + img_name)

   name = bytes(img_name, 'utf-8')

   s.send(name)


   file = open(image_folder_path + img_name, 'rb')
   
   img_data = file.read(2048)

  
   while img_data:
      s.send(img_data)
      img_data = file.read(2048)
      time.sleep(0.001)

   time.sleep(0.001)
  
   file.close()

# Calculate the end time and time taken
end = time.time()

# Show the results : this can be altered however you like
print(len(imgs),"photos took", end - start, "seconds!")
