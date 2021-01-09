import socket

HOST = '127.0.0.1'
PORT = 7777
server = socket.socket()
server.bind((HOST, PORT))
print('[+] Server Started')
print('[+] Listening for Client Connection ...')
server.listen()
client, client_addr = server.accept()
print(f'[+]{client_addr}) Client connected to the server')

while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode()
    print(f"Output: {output}")