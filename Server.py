import random
import socket
import threading

HEADER = 64
PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT !!"

# Your index number (e.g., ITBIN-2211-xxxx)
CLOSE_COMMAND = "ITBIN-2211-xxxx"

# List of motivational quotes
quotes = [
    "Believe in yourself!",
    "You are stronger than you think.",
    "Dream big and dare to fail.",
    "Success is not final, failure is not fatal.",
    "The only way to do great work is to love what you do.",
    "Don’t watch the clock; do what it does. Keep going.",
    "You are capable of amazing things!"
]

ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected!")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER)
        if msg_length:
            msg_length = int(msg_length)

            # Decode the received message
            msg = conn.recv(msg_length).decode()  
            
            print(f"[{addr}] {msg}")

            # Check if the received message matches the command to close
            if msg == CLOSE_COMMAND:  
                print(f"[{addr}] Closing connection...")
                connected = False

            # Choose a random quote from the list and send it to the client
            random_quote = random.choice(quotes)
            conn.send(random_quote.encode())

    conn.close()

# Applying multiple threading
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count() - 1}")


print("[STARTING] Server is starting...")

start()
