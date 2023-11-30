import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3000
ip = socket.gethostbyname(socket.gethostname())

connectionString =(ip, port)
s.connect(connectionString)

message = input("Enter sample message to send to server: ")
s.send(message.encode()) 

print((s.recv(1024).decode()))

s.close()
