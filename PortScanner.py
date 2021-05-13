#!/bin/usr/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("ip: ")
port = int(input("port: "))

def portscanner(port):
    if s.connect_ex((host, port)):
        print(f"{port} is closed.")
    else:
        print(f"{port} is open.")
portscanner(port)