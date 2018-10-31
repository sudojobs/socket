import socket

UDP_IP = "CHANGE TO PI'S IP"
UDP_Port = 5005
MESSAGE = "Hello, World!"


def send_data(UDP_IP,UDP_Port,MESSAGE):
    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "message:", MESSAGE
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Internet # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def recieve_data(UDP_IP,UDP_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet UDP
    sock.bind(MESSAGE, (UDP_IP, UDP_PORT))

    while True:
       data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
       print "received message:" data
       #Insert the UID and Gate Access in sqlite database
