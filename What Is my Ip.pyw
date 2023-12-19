import time
from tkinter import *
from tkinter import ttk
import socket
import requests 

master = Tk()
master.geometry("300x1")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
master.title(requests.get('https://api.ipify.org/').text) 

mainloop()

