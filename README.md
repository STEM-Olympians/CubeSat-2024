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
3. Send SatServer.py, FlatSat_student.py, Config.py, Buffer.py, sat_req.txt, and some dummy images over through SSH or VNC:
   scp /Users/raheyo/CubeSat-2024/sat_req.txt olympians@grapefruitpi.local:/home/olympians/Olympian/

   scp /Users/raheyo/CubeSat-2024/SatServer.py olympians@grapefruitpi.local:/home/olympians/Olympian/
   scp /Users/raheyo/CubeSat-2024/Config.py olympians@grapefruitpi.local:/home/olympians/Olympian/
   scp /Users/raheyo/CubeSat-2024/Buffer.py olympians@grapefruitpi.local:/home/olympians/Olympian/
   scp /Users/raheyo/CubeSat-2024/Nominal.py olympians@grapefruitpi.local:/home/olympians/Olympian/

   If you want dummy images on the Pi just to test out the Bluetooth file transfers, here are some you can use!
   scp /Users/raheyo/CubeSat-2024/Images/square0.jpeg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/
   scp /Users/raheyo/CubeSat-2024/Images/square1.png olympians@grapefruitpi.local:/home/olympians/Olympian/Images/s
   scp /Users/raheyo/CubeSat-2024/Images/square2.jpeg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/

   Suggest not using these ones, file too large to transfer over bluetooth:
   scp /Users/raheyo/CubeSat-2024/Images/square3.jpg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/
   scp /Users/raheyo/CubeSat-2024/Images/square4.jpg olympians@grapefruitpi.local:/home/olympians/Olympian/Images/

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

### For for mac ground station it's easy:

pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez

### For the cubesat server: download pybluez zip file from https://pybluez.readthedocs.io/en/latest/install.html to your computer:

for me it's in the /user/raheyo/Downloads/ folder on my mac, file location different on Windows

then scp over to the pi:
scp /Users/raheyo/Downloads/pybluez-master.zip olympians@grapefruitpi.local:/home/olympians/Olympian/

lastly on the Pi, in your repo directory unzip the file, cd into the folder and run the setup.py:
unzip pybluez-master.zip
cd pybluez-master
sudo python setup.py install

DON'T FORGET THE "SUDO" IN THE LAST COMMAND OR ELSE IT WOULDN'T WORK

# Troublshooting

## SSH connection refused/unable to establish

ssh-keygen -R grapefruitpi.local

## Error while installing pybluez on the Pi: <bluetooth.h> file not found

You forgot to do the REQUIRED part before installing pybluez, refer back to it and don't be lazy~

## Bluetooth error: subprocess-exited-with-error; × python setup.py egg_info did not run successfully.

This means your pybluez package has some error. Reinstall it completely and install it again with the desired command with "egginfo" specified
sudo pip uninstall pybluez
pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez

## Bluetooth error: File "/Users/raheyo/.pyenv/versions/3.9.18/lib/python3.9/site-packages/lightblue/_bluetoothsockets.py", line 787, in initWithDelegate_: self = super().init(); AttributeError: 'super' object has no attribute 'init'

## Bluetooth error: raise \_socket.error(result, OSError: [Errno -536870212] Cannot connect to 1 on D8:3A:DD:8E:CE:FA

That just means soemthing is wrong with your code, bad programmer skill issue!!! @\_@

## Bluetooth error: raise \_socket.error(errno.ECONNRESET, os.strerror(errno.ECONNRESET)) ConnectionResetError: [Errno 54] Connection reset by peer

That means you are closing the connection EARLY from one end of the socket (server or client), which cause the other code to fall short and not able to run.
TO FIX:
Check that you don't use the socket.close() function too much in the middle of the code for either the server or the client~

## Permission denied on the Pi: [Errno 13] Permission denied: '/usr/local/lib/python3.11/dist-packages/test-easy-install-2831.write-test'

Use "sudo" before your linux command on the Pi. The system doesn't trust you right now because you're remotely controlling it through ssh~

## Camera Preview Error: qt.qpa.xcb: could not connect to display qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found. This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

### This one is a bit annoying, cuz YOU HAVE TO THIS EVERY NEW TIME YOU SSH INTO IT AND CONNECT

export QT_QPA_PLATFORM=offscreen
sudo apt update
sudo apt upgrade -y
sudo rpi-update pulls/5691s
