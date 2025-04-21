import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 12345))

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

client_socket.send(f"{num1} {num2}".encode())

result = client_socket.recv(1024).decode()
print(f"Sum from Server: {result}")

client_socket.close()
