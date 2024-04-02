# Steps for setup:

1) Connect to raspberry over bluetooth
2) Run hciconfig in the raspberry terminal
3) Find your laptop's bluetooth address
4) Copy that address
5) Ensure that you connect to your laptop's bluetooth automatically
6) Go to Server.py, line 8 and paste that address into: "hostMACAddress = [your address here]"
7) Create a new folder where you want images to be stored
8) Copy the absolute file path
9) Go to Server.py, line 12 and paste it into "directory_to_write = [address here]"\
^^ the address wouldn't work for me, without using forward slashes

No need to install, as all packages used are within python standard library


# Steps to running:

1) Connect to Raspberry PI over bluetooth
2) Ensure you have some way of SSHing or VNCing into it, and do it
3) Ensure that Client.py are the same in this repo, and in the PI
4) Run Server.py on your host machine (laptop)
5) Run Client.py on PI to start the image transfer
