
from socket import *

# create socket
sockfd = socket(AF_INET, SOCK_DGRAM)

# bind socket
sockfd.bind(("127.0.0.1", 9998))

server_addr = ('127.0.0.1', 9999)
# send message
message = "this is yuka"
msg = message.encode()
sockfd.sendto(msg, server_addr)

# recv message
data, addr = sockfd.recvfrom(1024)
print(data)
