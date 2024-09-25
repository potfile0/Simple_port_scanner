#!/usr/bin/python3

import sys
import socket
from datetime import datetime

def print_banner():
    banner = r"""
    #####################################################
    #                                                   #
    #            Welcome to the Port Scanner            #
    #                Developed by Sanskar               #
    #                                                   #
    #####################################################
    """
    print(banner)

# Function to scan ports
def scan_ports(target, ports):
    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)

    try:
        for port in ports:
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
    print_banner()

    if len(sys.argv) != 2:
        print("Invalid amount of arguments")
        print("Syntax: python3 scanner.py <ip>")
        sys.exit()

    target = socket.gethostbyname(sys.argv[1])
    default_ports = range(1, 1001)

    print("Default scan will check ports 1-1000.")
    user_input = input("Would you like to scan specific ports instead? (y/n): ").strip().lower()

    if user_input == 'y':
        ports = input("Enter the ports to scan (comma-separated): ")
        ports = [int(port.strip()) for port in ports.split(',')]
    else:
        ports = default_ports

    scan_ports(target, ports)

if __name__ == "__main__":
    main()
