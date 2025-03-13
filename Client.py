import socket
import threading

PORT= 5000

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)

ADDR = (SERVER , PORT)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR )

def handle_client(con , addr):
    pass

def start():
    server.listen()
    while True:
        conn , addr = server.accept()


print("[STARTING] Server is startting...")  

start()