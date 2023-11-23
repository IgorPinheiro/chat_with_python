import socket
import threading

# Create a socket server

HOST = '127.0.0.1'
PORT = 8004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# Create a variable rooms for receive living_room
rooms = {}

# Creating a function broadcast.
def broadcast(living_room, menssage):
    for msg in rooms[living_room]:
        if isinstance(menssage, str):
            menssage = menssage.encode()

        msg.send(menssage)
    
def sendMenssage(name, living_room, client):
    while True:
        menssage = client.recv(1024)
        menssage = f'{name}: {menssage.decode()}\n'
        broadcast(living_room, menssage)


# Creating a while True for a infiniti connection, and send some words
while True:
    client, addr = server.accept()
    client.send(b'ROOM')
    name = client.recv(1024).decode()
    living_room = client.recv(1024).decode()
    
    if living_room not in rooms.keys():
        rooms[living_room] = []
    rooms[living_room].append(client)
    print(f"{name} is conected in the living room {living_room}! INFO: {addr}")
    broadcast(living_room, f'{name} is Online!\n')
    thread = threading.Thread(target=sendMenssage, args=(name, living_room, client))
    thread.start()
