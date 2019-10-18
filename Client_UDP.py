import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# ask user input
print("What's your request today?")

# build message for server
message = str.encode(input())

# establish connection
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send message to server
sock.sendto(message, (UDP_IP, UDP_PORT))

# receive message from server
msgFromServer = sock.recvfrom(1024)

# display message from server
print("Message from Server:\n{}".format(msgFromServer[0]))
