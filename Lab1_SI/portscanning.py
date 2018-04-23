from socket import *
import sys, time
from datetime import datetime

#declaring programm settings
#numbers are for the range on the scanned port

host = 'localhost'
max_port = 100
min_port = 1

#scan_host function

def scan_host (host, port, r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host,port))

        if code == 0:
            r_code = code
        s.close()
    except Exception, e:
        pass
    return r_code


#initiating the program. This is the part when we ask the user the host addres
#The address can be a URL or a direct IP address

try:
    host = raw_input("[*] Enter Target Host Address: ")
except KeyboardInterrupt:
    print("\n\n [*]User Requested an Interrupt.")
    print("[*]Application shutting down.")
    sys.exit(1)

#get host by name
#this function returns the ip numeric values of an address/url
hostip = gethostbyname(host)
print("\n Host: %s IP: %s" %(host, hostip))
print("Scanning Started at %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()


#port scanning

for port in range(min_port, max_port):
    try:
        response = scan_host(host, port)

        if response == 0:
            print("Port %d: Open" %(port))
    except Exception, e:
        pass

stop_time = datetime.now()
total_time_duration = stop_time - start_time
print ("\n Scanning finished at %s ..." %(time.strftime("%H:%M:%S")))
print("Scanning duration is :%s..." %(total_time_duration))


