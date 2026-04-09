import os; import hashlib; import base64; import socket; import random

def connection():
    # Host = input("What Host Do You Wanna Create (IPv4) :")
    # Port = input("What Port Do You Wanna Create:")
    Host = "127.0.0.1"
    Port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Host, Port))
        s.listen()
        conn, addr = s.accept()


    with conn:
        print("Connected")
        while True:
            data = conn.recv(1024)
            if not data:
                break

connection()
# print("Wire signal")
# print("1. Enter Communication server's. ")
# print("2. Start a Communication server. ")
# input1 = input("")
# if input == "1":
#     connection()
# else:
#     print("none")

#Connect With Device


#List open Devices

def OpenDevices():
    Server = socket.getaddrinfo()   
