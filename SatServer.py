import bluetooth
from os import listdir
from os.path import isfile, join, getsize

import Config
import Buffer

PORT = Config.PORT  # Any unused port number

# Create a socket and bind it to the port, the socket is configured to be bluetooth with Radio Frequency Communication type
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind((Config.server_bluetooth_address, PORT))
server_sock.listen(1)  # Listen for connections made to the socket

# Always accepting connections forever, waits for client requests for data streams!
while True:
    # Always accepting connections forever
    connection, client_address = server_sock.accept()
    print("Connected to", client_address)
    
    # Receive and write logic here (refer to documentation for details)
    middlewear = Buffer.Buffer(connection)

    imgs = [img for img in listdir(Config.directory_to_read) if isfile(join(Config.directory_to_read, img))].sort(reverse=True)

    for img in imgs:
        img_path = join(Config.directory_to_read, img)
        print(f"Transferring Image at: {img_path}")

        middlewear.put_utf8(img)

        file_size = getsize(img_path)
        middlewear.put_utf8(str(file_size))

        with open(img_path, 'rb') as f:
            middlewear.put_bytes(f.read())
        
        print('File Sent')
    
    connection.close()
server_sock.close()