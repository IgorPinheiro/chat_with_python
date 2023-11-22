import socket
import threading
import tkinter
from tkinter import *
from tkinter import simpledialog


class Chat:

    def __init__(self):

        HOST = '127.0.0.1'
        PORT = 8004
        # self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.connect((HOST, PORT))
        
        login = Tk()
        login.withdraw()

        self.loaded_window = False
        self.active = True

        self.name = simpledialog.askstring('name', 'Type your name! ', parent=login)
        self.room = simpledialog.askstring('room', 'Type the name of room that you wish entry! ', parent=login)
        self.main_window()


    def main_window(self):
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title('Enjoi Chat')

        self.text_box = Text(self.root)
        self.text_box.place(relx=0.05, rely=0.05, width=700, height=600)

        self.send_menssage = Entry(self.root,)
        self.send_menssage.place(relx=0.05, rely=0.9, width=500, height=30)

        self.btn_send = Button(self.root, text='Send', command=sendMessage)
        self.btn_send.place(relx=0.7, rely=0.9, width=100, height=30)



        self.root.mainloop()

    def sendMessage(self):
        ...

chat = Chat()



