
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
allowedIP = '127.0.0.1'

port = 3000

s.bind(('', port))
s.listen(2)
print('Server is listening')


conn, addr = s.accept()
print('Got connection from', addr)
print("add", addr[0])

if addr[0] == allowedIP:
    data = conn.recv(1024)  # Receive data from the client
    print('Received data from client: ', data)
    conn.send(b'Thank you for connecting')
    conn.close()
else:
    print('Connection from', addr, 'refused')
    conn.close()






