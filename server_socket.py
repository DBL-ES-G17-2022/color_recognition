import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '192.168.47.1'#'192.168.47.1'
port = 11334

s.bind((ip, port))
s.listen()
connection, client_address = s.accept()

while True:
    data = connection.recv(5)
    if data != b'':
        print(data)