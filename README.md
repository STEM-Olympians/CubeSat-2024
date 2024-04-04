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

1) Connect to Raspberry PI over bluetooth
2) Ensure you have some way of SSHing or VNCing into it, and do it
3) Copy and paste Client.py and Config.py into the PI's Olympian folder
4) Run Server.py on your host machine (laptop)
5) Run Client.py on PI to start the image transfer
