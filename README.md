# Steps for setup:

1. Connect to raspberry over bluetooth
2. Run hciconfig in the raspberry terminal
3. Find your laptop's bluetooth address
4. Copy that address
5. Ensure that you connect to your laptop's bluetooth automatically
6. Go to Config.py, and paste that address into `server_bluetooth_address = [Your address here]`
7. OPTIONAL: Change the write directory to change the folder in which images are stored

No need to install, as all packages used are within python standard library

# Steps to running:

1. Connect to Raspberry PI over bluetooth
2. Ensure you have some way of SSHing or VNCing into it, and do it
3. Send SatServer.py, FlatSat_student.py, Config.py, Buffer.py, and some dummy images over through SSH or VNC:
   scp /Users/raheyo/CubeSat-2024/SatServer.py olympians@grapefruitpi.local:/home/olympians/Olympian/
   scp /Users/raheyo/CubeSat-2024/Config.py olympians@grapefruitpi.local:/home/olympians/Olympian/
   scp /Users/raheyo/CubeSat-2024/Buffer.py olympians@grapefruitpi.local:/home/olympians/Olympian/
   scp /Users/raheyo/CubeSat-2024/FlatSat_student.py olympians@grapefruitpi.local:/home/olympians/Olympian/

   scp /Users/raheyo/CubeSat-2024/Images/timessquare0.jpeg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/
   scp /Users/raheyo/CubeSat-2024/Images/timessquare1.png olympians@grapefruitpi.local:/home/olympians/Olympian/Images/
   scp /Users/raheyo/CubeSat-2024/Images/timessquare2.jpeg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/
   scp /Users/raheyo/CubeSat-2024/Images/timessquare3.jpg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/
   scp /Users/raheyo/CubeSat-2024/Images/timessquare4.jpg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/

4. Send the cubesat server environment configurations over scp:
   scp /Users/raheyo/CubeSat-2024/sat_req.txt olympians@grapefruitpi.local:/home/olympians/Olympian/

   Then run this on the pi:
   pip install -r sat_req.txt

5. Run Server.py on your host machine (laptop)
6. Run Client.py on PI to start the image transfer

# Install bluetooth dependencies

## Additional for cubesat server (REQUIRED) - create bluetooth.h header files before installing for pybluez

On your pi, run:
sudo apt-get install libbluetooth-dev

## For both cubesat server and Mac ground station client install PyBluez:

pip install pybluez

# Troublshooting

## SSH connection refused/unable to establish

ssh-keygen -R grapefruitpi.local

## Bluetooth error: raise \_socket.error(result, OSError: [Errno -536870212] Cannot connect to 1 on D8:3A:DD:8E:CE:FA

That just means soemthing is wrong with your code, bad programmer skill issue!!! @\_@

## Error while installing pybluez on the Pi: <bluetooth.h> file not found

You forgot to do the REQUIRED part before installing pybluez, refer back to it and don't be lazy~
