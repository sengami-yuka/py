
from socket import *
import time

# create socket
sockfd = socket(AF_INET, SOCK_DGRAM)

# bind socket
sockfd.bind(("127.0.0.1", 9999))

# recv message
while 1:
    time.sleep(10)
    data, client_addr = sockfd.recvfrom(1024)
    print data
    # send message
    message = "hi from server"
    msg = message.encode()
    sockfd.sendto(msg, client_addr)

