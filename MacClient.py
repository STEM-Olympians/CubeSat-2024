import bluetooth
import os
import time

import Buffer
import Config

PORT = Config.PORT

def writeFiles(middlewear):
    # Will NOT run forever, only runs until there are no more files to receive
    while True:
        # The first thing we receive should be the file name
        file_name = middlewear.get_utf8()
        
        if (not file_name) or (not ".jpg" in file_name):
            # If no more files to receive, automatically break and then close the connection
            print('No more files to receive. Closing connection.')
            break
        filePath = os.path.join(Config.directory_to_write, file_name)
        print('Receiving File Path: ', filePath)

        # The second thing we receive should be the file size
        file_size = int(middlewear.get_utf8())
        print('File Size: ', file_size)

        with open(filePath, 'wb') as f:
            # Algorithm to write our files in chunks, thanks genius Brandon!!!
            remaining = file_size
            while remaining:
                chunk_size = 4096 if remaining >= 4096 else remaining
                chunk = middlewear.get_bytes(chunk_size)
                if not chunk: break
                f.write(chunk)
                remaining -= len(chunk)
            if remaining:
                print('File incomplete.  Missing',remaining,'bytes.')
            else:
                print('File received successfully.')



# Conect to the message channel (port) and send our command, disconnect after to make room for data connection channel (port)
client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client_sock.connect((Config.server_bluetooth_address, PORT))

def ClientRequest():
    # Ask our ground station console what command we want to use
    control = input("Command to the CubeSat Server: ")
    msgMiddlewear = Buffer.Buffer(client_sock)
    msgMiddlewear.put_utf8(control, False)
    control = int(control)

    # Send and receive logic here (refer to documentation for details)
    middlewear = Buffer.Buffer(client_sock)

    if control == Config.Mode.COMM:
        writeFiles(middlewear)
        commConfirm = middlewear.get_utf8()
        print(commConfirm)

    elif control == Config.Mode.NOMINAL:
        nominalConfirm = middlewear.get_utf8()
        print(nominalConfirm)

while True:
    ClientRequest()