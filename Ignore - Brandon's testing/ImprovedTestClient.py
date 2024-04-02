"""
A simple Python script to send messages to a sever over Bluetooth using
Python sockets (with Python 3.3 or above).
"""
import socket
from os import listdir, stat
from os.path import isfile, join
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1002))

# Calculate the start time
start = time.time()

# image_folder_path = "C:/Users/admin/Documents/Repos/CubeSat-2024/Images/"
image_folder_path = "C:/Users/user/Documents/CubeSat-2024/Images/"

imgs = [img for img in listdir(image_folder_path) if isfile(join(image_folder_path, img))]

totalBytes = 0

# Iterate over all the images we found
for img_name in imgs :
   
   # Confirm image path
   print(image_folder_path + img_name)

   
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect(("127.0.0.1",1002))

      # Send the name over to server
      s.send(bytes(img_name, 'utf-8'))



   totalBytes += stat(image_folder_path + img_name).st_size


   # Open file and begin reading data in 2048 byte chunks
   file = open(image_folder_path + img_name, 'rb')
   

   img_data = file.read(2048)
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect(("127.0.0.1",1002))
      # While there's still more data, send the data over
      while img_data:
         s.send(img_data)
         img_data = file.read(2048)
         time.sleep(0.001)
  


  
  
   # Close the file
   file.close()

# Calculate the end time and time taken
end = time.time()

# Show the results

line1 = "It took " +  str(round(end-start, 5)) + " seconds to send:"
line2 = str(len(imgs)) + " photos, or"
line3 = f"{totalBytes:,}" + " total bytes, or"
line4 = str(totalBytes / 10**6) + " megabytes"

print(line1)
print(line2)

print(line3)
print(line4)

s.send(bytes("MSG: " + line1, 'utf-8'))
time.sleep(0.01)
s.send(bytes("MSG: " + line2, 'utf-8'))
time.sleep(0.01)
s.send(bytes("MSG: " + line3, 'utf-8'))
time.sleep(0.01)
s.send(bytes("MSG: " + line4, 'utf-8'))
time.sleep(0.01)