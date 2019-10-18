import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5001

# establish connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the IP address and the port
s.connect((TCP_IP, TCP_PORT))

print("What's your request today?")

# get input
message = input()

# send message
s.sendall(str.encode(message))

# receive data from the server
data = s.recv(1024)

# display the server message
print(format(data))

# close the connection
s.close()
