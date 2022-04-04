import socket
import syslog


SERVER_ADDRESS = ('localhost', 7759)
clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)
print('Server is running...')

while True:
    data, address = server_socket.recvfrom(1024)
    print(address[0], address[1])
    if address not in clients:
        clients.append(address)
    for client in clients:
        if client == address:
            continue
        server_socket.sendto(data, client)
    server_socket.sendto('sent'.encode('utf-8'), address)
    syslog.syslog(data.decode('utf-8'))

