import socket
import datetime

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# initialize new socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

# bind the port to the correct address
sock.bind((UDP_IP, UDP_PORT))

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
    data, address = sock.recvfrom(1024)
    if not data:
        break
    # data validation
    if data == "What is the current date and time?":
        print("From client:")
        print(data)
        print("Replying to client...")
        # reply to client
        sock.sendto(bytesToSend, address)
    else:
        # return error message to client
        sock.sendto(errorToSend, address)

# no closing needed
