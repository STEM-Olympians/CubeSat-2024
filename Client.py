import socket
import time

from os import listdir, stat
from os.path import isfile, join

# CONFIG: ======================================

# Bluetooth address of YOUR LAPTOP
# Run hciconfig on the raspberry pi while your laptop is connected over bluetooth to find this address
serverMACAddress = 'D8:3A:DD:8E:CE:FA'

# ==============================================



# Calculate the start time
start = time.time()

# 6 is an arbitrary choice. However, it must match the port used by the server.
port = 6 
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

image_folder_path = "/home/olympians/Olympian/Images/"

imgs = [img for img in listdir(image_folder_path) if isfile(join(image_folder_path, img))]

print(imgs)
totalBytes = 0

size = 4096

# Iterate over all the images we found
for img_name in imgs :
   
   # Confirm image path
   print(image_folder_path + img_name)

   # Send the name over to server
   s.send(("NAME: " + img_name).encode())



   totalBytes += stat(image_folder_path + img_name).st_size


   # Open file 
   file = open(image_folder_path + img_name, 'rb')
   
   # Begin reading data 
   img_data = file.read(size)

   # While there's still more data, send the data over
   while img_data:
      s.send(img_data)
      
      img_data = file.read(size)
      time.sleep(0.01)


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
