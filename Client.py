import socket

HEADER = 64
PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_request():
    while True:
        message = input("Send a message: ")
        if message == DISCONNECT_MESSAGE:
            break

        msg_length = len(message)
        send_length = str(msg_length).ljust(HEADER) 
        client.send(send_length.encode())

        # Send the message
        client.send(message.encode())  

        # Receive a motivational quote from the server
        quote = client.recv(1024).decode()
        print(f"Server: {quote}")

        # Check if the client sends the close command
        if message == "ITBIN-2211-xxxx":  
            print("Disconnecting from server...")
            break

send_request()
