import socket; import os

def client():
    Host = "127.0.0.1"
    Port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((Host, Port))
        print("Connected")
        while True:
            reply = input("You: ")
            s.sendall(reply.encode())
            data = s.recv(1024)
            message = data.decode()
            if reply == "quit" or message == "quit":
                s.close()
                break
            print(f"Server: {message}")

client()