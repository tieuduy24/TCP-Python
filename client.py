import socket

#đây là của server
HOST = '127.0.0.1' 
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    i = input("Gửi lời chào tới server:")
    s.sendall(i.encode())
    data = s.recv(1024)

print('Received', repr(data))