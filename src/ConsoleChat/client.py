import socket
import threading

SERVER_ADDRESS = ('localhost', 7759)

name = input('Введите свое имя: ')

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(('', 0))
socket.sendto(f'{name} connected to server'.encode('utf-8'), SERVER_ADDRESS)


def receive():
    while True:
        print(socket.recv(1024).decode('utf-8'))


def write():
    while True:
        try:
            message = input('')
            socket.sendto((name + ': ' + message).encode('utf-8'), SERVER_ADDRESS)
        except:
            print('Error!')


receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()