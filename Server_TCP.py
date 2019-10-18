import socket
import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5001

# establish connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bing the IP address and the port
s.bind((TCP_IP, TCP_PORT))

# server is up and ready to listen
s.listen(1)

# get connection and address from the client
conn, addr = s.accept()

# get year
current_year = str(datetime.datetime.now().year)

# get month
current_month = str(datetime.datetime.now().month)

# get day
current_day = str(datetime.datetime.now().day)

# get hour
current_hour = str(datetime.datetime.now().hour)

# get minute
current_minute = str(datetime.datetime.now().minute)

# get second
current_second = str(datetime.datetime.now().second)

# setup string output
current_time = current_month + "/" + current_day + "/" + current_year + " " + current_hour + ":" + current_minute + ":" + current_second

# convert to string
time = str(current_time)

# build message
msgFromServer = "Current Date and Time - " + time

# convert to byte
bytesToSend = str.encode(msgFromServer)

# error message
errormsg = "Invalid request"

# convert to byte
errorToSend = str.encode(errormsg)

while 1:
    # data received, buffer size is 1024 bytes
    data = conn.recv(1024)
    if not data:
        break
    # data validation
    if data == "What is the current date and time?":
        print("From client:")
        print(data)
        print("Replying to client...")
        # reply to client
        conn.sendall(bytesToSend)
    else:
        # return error message to client
        conn.sendall(errorToSend)
# close the connection
conn.close()
