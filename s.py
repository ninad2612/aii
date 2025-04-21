import socket

server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)
print("Server is listening...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

data = conn.recv(1024).decode()
num1, num2 = map(int, data.split())

result = num1 + num2
conn.send(str(result).encode())

conn.close()
server_socket.close()
