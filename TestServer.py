"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""

import socket
from queue import Queue

queue = Queue()

size = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",1002))
s.listen()

prev_name = ""
img_name = ""
directory_to_write = "C:/Users/admin/Documents/Repos/CubeSat-2024/Test/"


try:
        client, address = s.accept()
        data = client.recv(size)
        print(data)

        opened = False

        file = None
        while data:
                
        
                is_set = False

                name = False
                try:
                
                    t = data.decode("utf-8")
                    name = True
                    
                except:
                
                    name = False


                if name:
                
                    new_name = data.decode("utf-8")

                    print(new_name)
                    if(new_name != img_name):

                        prev_name = img_name
                        img_name = new_name
                        is_set = True
                        print(img_name)

                        print("changed")
                        # client.send(bytes(img_name, "utf-8"))

                        if(prev_name != "" and img_name != prev_name):
                            
                            file.close()
                            opened = False
                            print("closed")
                else:
                    print("img")
                    is_set = False

                if(img_name != ""):
                    print("ok")
                    if not opened:
                        file = open(directory_to_write + img_name, "wb+")
                        opened = True
                        print("open")
                    if not is_set:
                        file.write(data)
                        print("Write")
                        
                data = client.recv(size)

        file.close()


except:	
        print("Closing socket")	
        client.close()
        s.close()
