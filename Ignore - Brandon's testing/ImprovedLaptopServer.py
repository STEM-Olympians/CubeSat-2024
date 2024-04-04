"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""

import socket
import struct
import time


size = 2048

prev_name = ""
img_name = ""
# directory_to_write = "C:/Users/admin/Documents/Repos/CubeSat-2024/Test/"
directory_to_write = "C:/Users/user/Documents/CubeSat-2024/Test/"

prev_msg = ""

prev_mode = ""
mode = "message"

aaa = ""
bbb = "a"

def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

def recv_msg(sock):
    global bbb
    
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        if(bbb != "sad"):
            print("sad")
            bbb = "sad"
        return None
    print("woo?")
    
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)

def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    print(data)
    return data

while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            s.bind(("127.0.0.1",1002))
            s.listen()
            client, address = s.accept()
        
            with client:
                print(f"Connected by {address}")
                file = None
                opened = False 
                data = client.recv(4096)

                while data:
                    try:  
                        msg = data.decode("utf-8")
                        print(msg)

                    except:
                        mode = "image"
                    print("woo")


               
                while True:
                    data = recv_msg(client)
                    if not data:
                        if(aaa != "no"):
                            print("no")
                            aaa = "no"
                        continue
                
                    try:  
                        msg = data.decode("utf-8")
                        print(msg)
                        aaa = msg
                        if(msg[:4] == "MSG:") and prev_msg != msg:
                            mode = "message"
                            
                        else: 
                            mode = "name"

                    except:
                        mode = "image"
                    
                    # if(prev_mode != mode):
                        
                    #     if(prev_mode == "image"):
                    #         file.close()
                    #         print("closed")
                    #         opened = False

                    #     prev_mode = mode
                    #     print(mode)
                    # match mode:
                                                
                    #     case "name":
                    #         img_name = data.decode("utf-8")                        
                    #         print(img_name)
                    #     case "image":
                                
                    #         if(img_name != ""):
                    #             # print("ok")
                    #             if not opened:
                    #                 file = open(directory_to_write + img_name, "wb+")
                    #                 opened = True
                    #                 print("open")
                            
                    #             file.write(data)
                    #             # print("Write")
                    #     case "message" | _:
                    #         print(data.decode("utf-8"))


    print("dead")