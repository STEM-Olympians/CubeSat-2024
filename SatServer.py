import bluetooth
from os import listdir
from os.path import isfile, join, getsize

import Config
import Buffer
from Nominal import nominal

PORT = Config.PORT

# Create a socket and bind it to the port, the socket is configured to be bluetooth with Radio Frequency Communication type
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind((Config.server_bluetooth_address, PORT))
server_sock.listen(1)  # Listen for connections made to the socket
connection, client_address = server_sock.accept()
print("Message Connected to", client_address)

def Server():
    # Receiv Client Request Command through the msg port
    msgMiddlewear = Buffer.Buffer(connection)
    request = int(msgMiddlewear.get_utf8())
    print("Message Connection Received:", request)

    # Switch to the data connection port now, then receive and write logic here (refer to documentation for details)
    print("Responding Request...")
    dataMiddlewear = Buffer.Buffer(connection)
    
    match request:
        # Communication Mode: Send all the stored pictures
        case Config.Mode.COMM:
            print("Request Received: COMMUNICATION")
            
            imgs = listdir(Config.directory_to_read)
            imgs.sort()
            imgs = [img for img in imgs if isfile(join(Config.directory_to_read, img))]

            for img in imgs:
                img_path = join(Config.directory_to_read, img)
                print(f"Transferring Image at: {img_path}")

                dataMiddlewear.put_utf8(img)

                file_size = getsize(img_path)
                dataMiddlewear.put_utf8(str(file_size))

                with open(img_path, 'rb') as f:
                    dataMiddlewear.put_bytes(f.read())
                
                print('File Sent')

            dataMiddlewear.put_utf8("COMMUNICATION MODE COMPLETED~")
        
        # Nominal Mode: Take Pictures Every 12 Second
        case Config.Mode.NOMINAL:
            print("Request Received: NOMINAL")
            
            nominal()
            dataMiddlewear.put_utf8("NOMINAL MODE COMPLETED~")
            

        case Config.Mode.SLEEP:
            print("Request Received: SLEEP")


# Always accepting connections forever, waits for client requests for data streams!
while True:
    Server()
