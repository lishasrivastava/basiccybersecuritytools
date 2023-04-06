import socket

# Prompt user for website URL to scan
target = input("Enter website URL to scan: ")

# Define the range of ports to scan
port_range = range(1, 1025)

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set a timeout for the socket connection
s.settimeout(5)

# Function to check if a port is open
def scan_port(port):
    try:
        s.connect((target, port))
        return True
    except:
        return False

# Scan all ports in the range
for port in port_range:
    if scan_port(port):
        print("Port {} is open".format(port))
    else:
        print("Port {} is closed".format(port))

# Close the socket connection
s.close()
