import socket
import threading

HEADER = 64
PORT= 5000

SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)

FORMAT = 'utf- 8'
DISSCONNECT_MESSAGE = "!!DISSCONNECT"

ADDR = (SERVER , PORT)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR )

def handle_client(conn , addr):
    print(f"[NEW CONNECTION] {addr} connected!")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISSCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")

    conn.close()    

def start():
    server.listen()
    while True:
        conn , addr = server.accept()
        thread = threading.Thread(target=handle_client , argus=(conn , addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")


print("[STARTING] Server is startting...")  

start()