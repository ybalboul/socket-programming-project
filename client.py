import sys
import socket
import signal

def signalHandler(sig, frame):
    print("\nDisconnecting")
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler) # catches Ctrl+C

if len(sys.argv) != 3:
    print("usage: client.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2]) # converts string to integer for connection

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sets up socket connection

try: #catches connection problems
    server.connect((host, port))
except socket.error:
    print("Could not connect")
    sys.exit(1)

key = True
while key != False:
    command = input("> ")
    if command == "":
        print("***Input can't be blank***")
    else:
        server.send(bytes(command, "utf-8")) # sends your command to the server as bytes
        response = server.recv(4096) # max size of 4096 bytes to be recieved from server
        response = response.decode() # decodes to be readable as a string

        if response == "Goodbye":
            key = False
            print(f"Server: {response}")
            break

        print(f"Server: {response}") # prints the server's response 

server.close()