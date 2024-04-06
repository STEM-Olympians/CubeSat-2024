import bluetooth
from os import listdir
from os.path import isfile, join, getsize

import Config
import Buffer
from Nominal import nominal

PORT = Config.PORT

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind((Config.server_bluetooth_address, PORT))
server_sock.listen(1)  # Listen for connections made to the socket

def Server():
    # Create a socket and bind it to the port, the socket is configured to be bluetooth with Radio Frequency Communication type
    connection, client_address = server_sock.accept()
    print("Message Connected to", client_address)

    # Receiv Client Request Command through the msg port
    msgMiddlewear = Buffer.Buffer(connection)
    request = int(msgMiddlewear.get_utf8())
    print("Message Connection Received:", request)

    # Switch to the data connection port now, then receive and write logic here (refer to documentation for details)
    print("Responding Request...")
    dataMiddlewear = Buffer.Buffer(connection)
    
    match int(request):
        # Communication Mode: Send all the stored pictures
        case Config.Mode.COMM:
            print("Request Received: COMMUNICATION")
                    
            imgs = [img for img in listdir(Config.directory_to_read) if isfile(join(Config.directory_to_read, img))]

            for img in imgs:
                img_path = join(Config.directory_to_read, img)
                print(f"Transferring Image at: {img_path}")

                dataMiddlewear.put_utf8(img)

                file_size = getsize(img_path)
                dataMiddlewear.put_utf8(str(file_size))

                with open(img_path, 'rb') as f:
                    dataMiddlewear.put_bytes(f.read())
                
                print('File Sent')
        
        # Nominal Mode: Take Pictures Every 12 Second
        case Config.Mode.NOMINAL:
            print("Request Received: NOMINAL")

            nominal()
            

        case Config.Mode.SLEEP:
            print("Request Received: SLEEP")


# Always accepting connections forever, waits for client requests for data streams!
while True:
    Server()
