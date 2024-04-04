import socket
import os
import Config

import Buffer

HOST = Config.server_bluetooth_address
PORT = 2345


try:
    os.mkdir(Config.directory_to_write)
except FileExistsError:
    pass


with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    print("Waiting for a connection.....")

    while True:
        conn, addr = s.accept()
        print("Got a connection from ", addr)
        connbuf = Buffer.Buffer(conn)

        while True:
        

            file_name = connbuf.get_utf8()
            if not file_name:
                break
            file_name = os.path.join(Config.directory_to_write, file_name)
            print('file name: ', file_name)

            file_size = int(connbuf.get_utf8())
            print('file size: ', file_size )

            with open(file_name, 'wb') as f:
                remaining = file_size
                while remaining:
                    chunk_size = 4096 if remaining >= 4096 else remaining
                    chunk = connbuf.get_bytes(chunk_size)
                    if not chunk: break
                    f.write(chunk)
                    remaining -= len(chunk)
                if remaining:
                    print('File incomplete.  Missing',remaining,'bytes.')
                else:
                    print('File received successfully.')
        print('Connection closed.')
        conn.close()