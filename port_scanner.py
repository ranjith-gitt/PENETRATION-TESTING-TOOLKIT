import socket

def port_scanner(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)  # Set timeout for each connection
            # Try connecting to the target IP and port
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is CLOSED")
            s.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        