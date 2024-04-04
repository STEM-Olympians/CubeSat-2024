# Steps for setup:

1) Connect to raspberry over bluetooth
2) Run hciconfig in the raspberry terminal
3) Find your laptop's bluetooth address
4) Copy that address
5) Ensure that you connect to your laptop's bluetooth automatically
6) Go to Config.py, and paste that address into ```server_bluetooth_address = [Your address here]```
7) OPTIONAL: Change the write directory to change the folder in which images are stored

No need to install, as all packages used are within python standard library

# Steps to running:

1. Connect to Raspberry PI over bluetooth
2. Ensure you have some way of SSHing or VNCing into it, and do it
3. Send Client.py, FlatSat_student.py, Config.py, and some dummy images over through SSH or VNC:
   scp /Users/raheyo/CubeSat-2024/Client.py olympians@grapefruitpi.local:/home/olympians/Olympian/
   scp /Users/raheyo/CubeSat-2024/FlatSat_student.py olympians@grapefruitpi.local:/home/olympians/Olympian/

   scp /Users/raheyo/CubeSat-2024/Images/timessquare1.jpeg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/
   scp /Users/raheyo/CubeSat-2024/Images/timessquare2.jpeg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/

4. Run Server.py on your host machine (laptop)
5. Run Client.py on PI to start the image transfer
