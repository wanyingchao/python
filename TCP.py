import socket

host = ''
port = ''

obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
obj.connect((host, port))
obj.send(''.encode())

