# socket-programming-project
This is a socket programming project done in my Computer Networks class. The goal of the project was to set up a client-server connection and have the client send commands to the server and have the server return the output of said commands.
 
server.py is ran with an unused port number on one VM.
> server.py [port number]
  
client.py is ran with the ip address of the server VM and given the same port number.
> client.py [ip address] [port]

After this you are able to enter linux commands like free, uptime, date, etc. to recieve said information from the server VM and exit when you are done.
