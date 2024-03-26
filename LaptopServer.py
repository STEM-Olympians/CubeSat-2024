"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""

import socket


size = 2048

prev_name = ""
img_name = ""
directory_to_write = "C:/Users/admin/Documents/Repos/CubeSat-2024/Test/"

prev_msg = ""

prev_mode = ""
mode = "message"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.bind(("127.0.0.1",1002))
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

                    if(msg[:4] == "MSG:") and prev_msg != msg:
                        mode = "message"
                        
                    else: 
                        mode = "name"

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