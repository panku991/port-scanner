import socket

# Get user input for target IP address
target = input("Enter target IP address: ")

# Scan all ports on target
ports = '1-65535'

# Create socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Disable console output for connection attempts
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Set timeout for connection attempts
sock.settimeout(1)

# Attempt to connect to each port
for port in range(1, 65536):
    try:
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        sock.close()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    except socket.gaierror:
        print("\nHostname could not be resolved. Exiting...")
        exit()
    except socket.error:
        print("\nCould not connect to server. Exiting...")
        exit()
