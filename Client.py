import socket

HEADER = 64
PORT = 5000
SERVER = "127.0.0.1"  # Or use the server IP address
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
        send_length = str(msg_length).ljust(HEADER)  # Use ljust to ensure the length is correct
        client.send(send_length.encode())
        client.send(message.encode())  # Send the message

        # Receive a motivational quote from the server
        quote = client.recv(1024).decode()  # Change the buffer size if needed
        print(f"Server: {quote}")

        if message == "ITBIN-2211-xxxx":  # Check if the client sends the close command
            print("Disconnecting from server...")
            break

send_request()
