import socket
import os
from os import listdir
from os.path import isfile, join
import Config

import Buffer

HOST = '127.0.0.1'
PORT = 2345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

with s:
    sbuf = Buffer.Buffer(s)

   
    image_folder_path = Config.directory_to_read
    imgs = [img for img in listdir(image_folder_path) if isfile(join(image_folder_path, img))]

    for img_name in imgs :
        print(img_name)
       
        sbuf.put_utf8(img_name)

        file_size = os.path.getsize(image_folder_path + img_name)
        sbuf.put_utf8(str(file_size))

        with open(image_folder_path + img_name, 'rb') as f:
            sbuf.put_bytes(f.read())
        print('File Sent')