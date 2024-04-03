# Steps for setup:

1. Connect to raspberry over bluetooth
2. Run hciconfig in the raspberry terminal
3. Find your laptop's bluetooth address
4. Copy that address
5. Ensure that you connect to your laptop's bluetooth automatically
6. Go to Server.py, line 8 and paste that address into: "hostMACAddress = [your address here]"
7. Create a new folder where you want images to be stored
8. Copy the absolute file path
9. Go to Server.py, line 12 and paste it into "directory_to_write = [address here]"\
   ^^ the address wouldn't work for me, without using forward slashes

No need to install, as all packages used are within python standard library

# Steps to running:

1. Connect to Raspberry PI over bluetooth
2. Ensure you have some way of SSHing or VNCing into it, and do it
3. Send Client.py, FlatSat_student.py, and some dummy images over through SSH or VNC:
   scp /Users/raheyo/CubeSat-2024/Client.py olympians@grapefruitpi.local:/home/olympians/Olympian/
   scp /Users/raheyo/CubeSat-2024/FlatSat_student.py olympians@grapefruitpi.local:/home/olympians/Olympian/

   scp /Users/raheyo/CubeSat-2024/Images/timessquare1.jpeg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/
   scp /Users/raheyo/CubeSat-2024/Images/timessquare2.jpeg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/

4. Run Server.py on your host machine (laptop)
5. Run Client.py on PI to start the image transfer
