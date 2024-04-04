"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""
import socket
from os import listdir
from os.path import isfile, join
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1002))


image_folder_path = "C:/Users/user/Documents/CubeSat-2024/Images/"
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
