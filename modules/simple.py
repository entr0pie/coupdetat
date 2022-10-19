import socket


class SimpleClient:
    def client_connect(self, server_ip):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, 2022))
        return client

        crypt_key = client.recv(2048).decode()
        return client


class Simpleserver:
    def server_bind(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", 2022))
        server.listen(5)
        mailman, adress = server.accept()
        
        
        mailman.send(f"{adress}".encode())
        mailman.close()