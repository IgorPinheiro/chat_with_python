import socket
import threading

# Create a socket server

HOST = '127.0.0.1'
PORT = 8004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

while True:
    client, addr = server.accept()
