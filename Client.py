import socket
import threading

HEADER = 64
PORT= 5000

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)

ADDR = (SERVER , PORT)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR )

def handle_client(conn , addr):
    print(f"[NEW CONNECTION] {addr} connected!")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER)


def start():
    server.listen()
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handle_client , argus=(conn , addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")


print("[STARTING] Server is startting...")  

start()