"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""

import socket

hostMACAddress = 'A4:C3:F0:51:C0:AB' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 6 # 6 is an arbitrary choice. However, it must match the port used by the client.

size = 4096

prev_name = ""
img_name = ""
directory_to_write = "C:/Users/admin/Documents/Repos/CubeSat-2024/Images/"

prev_mode = ""
mode = "message"

with socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM) as s:
        
        s.bind((hostMACAddress, port))
        s.listen()
        client, address = s.accept()
    
        with client:
            print(f"Connected by {address}")
            file = None
            opened = False 
            while True:
                data = client.recv(size)
                if not data:
                    # print("no")
                    continue
            
                try:  
                    msg = data.decode("utf-8")
                    print(data)
                    print(msg)
                    
                    if msg[:4] == "MSG:":
                        mode = "message"
                            
                    elif msg[:5] == "NAME:": 
                        mode = "name"
                    else:
                        mode = "image"

                except:
                    
                    mode = "image"
                
                if(prev_mode != mode):
                    
                    if(prev_mode == "image"):
                        file.close()
                        print("closed")
                        opened = False

                    prev_mode = mode
                    print(mode)
                match mode:
                                            
                    case "name":
                        img_name = data.decode("utf-8")                        
                        print(img_name)
                    case "image":
                            
                        if(img_name != ""):
                            # print("ok")
                            if not opened:
                                file = open(directory_to_write + img_name, "wb+")
                                opened = True
                                print("open")
                        
                            file.write(data)
                            # print("Write")
                    case "message" | _:
                        print(data.decode("utf-8"))
                