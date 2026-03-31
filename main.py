import hashlib; from cryptography.fernet import Fernet; import base64; import socket; import random

List = ['santi , andrew, Edwardo']
r_w = random.choice(List)

#Server Creation
def Create_S():
    socket.sethostname(r_w)


#Connect With Device

def connection():
    Host = input(float("What Host Do You Wanna Connect :"))
    Port = input(float("What Port Do You Wanna Connect :"))
    

#List open Devices

def OpenDevices():
    Server = socket.getaddrinfo()
    in Server in