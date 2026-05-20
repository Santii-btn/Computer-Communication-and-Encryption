import os; import socket

messages = []
def add_message(msg):
    messages.append(msg)
def title():
    print(r" _       __________  ______   _____ ___________   _____    __ ")
    print(r"| |     / /  _/ __ \/ ____/  / ___//  _/ ____/ | / /   |  / / ")
    print(r"| | /| / // // /_/ / __/     \__ \ / // / __/  |/ / /| | / /  ")
    print(r"| |/ |/ // // _, _/ /___    ___/ // // /_/ / /|  / ___ |/ /___")
    print(r"|__/|__/___/_/ |_/_____/   /____/___/\____/_/ |_/_/  |_/_____/")
    print("")                                                        
def connection():
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
            message = data.decode()
            add_message(message)
            print(f"Client: {message}")
            reply = input("You: ")
            add_message(reply)
            conn.sendall(reply.encode())
            if reply == "quit" or message == "quit":
                conn.close()
                break
def show_history():
    print("\nMessage History:")
    if not messages:
        print("No messages yet.")
    else:
        for m in messages:
            print(m)
def inputsys():
    while True:
        title()
        print("1. Start Server Communication")
        print("2. View Message History")
        print("3. Exit")
        choice = input("Enter Your Choice: ").strip()
        if choice == "1":
            connection()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
inputsys()