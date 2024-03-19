"""
A simple Python script to receive messages from a client over
Bluetooth using Python sockets (with Python 3.3 or above).
"""

import socket

hostMACAddress = 'A4:C3:F0:51:C0:AB' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 6 # 6 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)


prev_name = ""
img_name = ""
directory_to_write = "C:/Users/admin/Documents/Repos/CubeSat-2024/Images/"


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
                   
                    is_set = False

                if(img_name != ""):
                    
                    if not opened:
                        file = open(directory_to_write + img_name, "wb+")
                        opened = True
                        print("open")
                    if not is_set:
                        file.write(data)
                        
                        
                data = client.recv(size)

        file.close()


except:	
        print("Closing socket")	
        client.close()
        s.close()



# try:
#     client, address = s.accept()
#     while 1:
#         data = client.recv(size)
#         if data:
#             print(data)
#             # client.send(data)
# except:	
#     print("Closing socket")	
#     client.close()
#     s.close()