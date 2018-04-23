#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "Huehuehuehue!"

#creating the tcp socket, sockstream indicating its type
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connection to hostname on the port
s.connect((TCP_IP, TCP_PORT))
'''
with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break 
        # write data to a file
        f.write(data)

f.close()
'''

#send a message
s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)