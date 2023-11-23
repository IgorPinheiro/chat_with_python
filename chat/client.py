import socket
import threading
import tkinter
from tkinter import *
from tkinter import simpledialog


class Chat:

    def __init__(self):

        HOST = '127.0.0.1'
        PORT = 8004
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        
        login = Tk()
        login.withdraw()

        self.loaded_window = False
        self.active = True

        self.name = simpledialog.askstring('name', 'Type your name! ', parent=login)
        self.room = simpledialog.askstring('room', 'Type the name of room that you wish entry! ', parent=login)

        thread = threading.Thread(target=self.connect)
        thread.start()

        self.main_window()


    def main_window(self):
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title(f'{self.name} is in the chat {self.room}')

        self.text_box = Text(self.root)
        self.text_box.place(relx=0.05, rely=0.05, width=700, height=600)

        self.send_menssage = Entry(self.root)
        self.send_menssage.place(relx=0.05, rely=0.9, width=500, height=30)

        self.btn_send = Button(self.root, text='Send', command=self.sendMenssage)
        self.btn_send.place(relx=0.7, rely=0.9, width=100, height=30)
        self.root.protocol('WM_DELETE_WINDOW', self.close)


        self.root.mainloop()
    
    def close(self):
        self.root.destroy()
        self.client.close()
    
    def connect(self):
        while True:
            received = self.client.recv(1024)
            if received == b'ROOM':
                self.client.send(self.name.encode())
                self.client.send(self.room.encode())
            else:
                try:
                    self.text_box.insert('end', received.decode())
                except:
                    pass

    def sendMenssage(self):
        menssage = self.send_menssage.get()
        self.client.send(menssage.encode())


chat = Chat()