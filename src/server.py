import socket
import client

def main():
    host = 'localhost'
    port = 8080

    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind((host, port)
    serv_sock.listen(4)
    while True:
        client.run()
        (clientsocket, address) = serv_sock.accept()
