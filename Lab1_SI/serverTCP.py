#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

#creating the tcp socket, sockstream indicating its type
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the server to the indicated port/addr
s.bind((TCP_IP, TCP_PORT))

#indicates the number of queued connections
s.listen(5)

#conn is a new socket to send/recieve data on this connection and addr is the addr bound to this connection
#actually creates a new socket(??)
conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data)
    conn.send(data)  # echo
'''
    filename = 'mytext.txt'
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print('Sent ', repr(l))
        l = f.read(1024)
    f.close()
'''

conn.close()