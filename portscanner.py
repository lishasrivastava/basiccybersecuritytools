import socket

#prompting user for the website URL they want to scan
target = input("Enter website URL to scan: ")

#set the range of the ports we'll scan
port_range = range(1, 1025)

#creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#set the timeout for the socket connection
s.settimeout(5)

#function scan_port(port) -> bool, checks if a port is open
def scan_port(port):
    try:
        s.connect((target, port))
        return True
    except:
        return False

#scan all the ports in the range to check if a port is open or not
for port in port_range:
    if scan_port(port):
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))

#close the socket connection
s.close()
