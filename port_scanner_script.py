#!/usr/bin/python3

import sys
import socket
from datetime import datetime

# Function to print a banner
def print_banner(target):
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)

# Function to scan ports
def scan_ports(target):
    try:
        for port in range(50, 85):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target, port))
                if result == 0:
                    print(f"Port {port} is open")
    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to the server.")
        sys.exit()

# Main function
def main():
    if len(sys.argv) != 2:
        print("Invalid amount of arguments")
        print("Syntax: python3 scanner.py <ip>")
        sys.exit()

    target = socket.gethostbyname(sys.argv[1])
    print_banner(target)
    scan_ports(target)

if __name__ == "__main__":
    main()
