import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "This is a UDP message!"

print ("UDP target IP:", UDP_IP)
print ("UDP targer port:", UDP_PORT)
print ("message:", MESSAGE)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
s.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
