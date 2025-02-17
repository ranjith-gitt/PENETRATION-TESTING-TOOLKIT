
from port_scanner import port_scanner

def main_menu():
    print("Penetration Testing Toolkit")
    print("[1] Port Scanner")
    print("[2] Exit")
    option = int(input("Select an option: "))
    
    if option == 1:
        target = input("Enter target IP: ")
        ports = [22, 80, 443, 8080]  # Common ports to scan
        port_scanner(target, ports)
    elif option == 2:
        print("Exiting...")
    else:
        print("Invalid option!")

# Start the program
main_menu()