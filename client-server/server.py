
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#create socket, family ipv4, type stream
ip = socket.gethostbyname(socket.gethostname())
allowedIP = ip

port = 3000

s.bind(('', port)) 
s.listen(2) 
print('Server is listening')


conn, addr = s.accept() 

print('Got connection from', addr)
print("add", addr[0])

if addr[0] == allowedIP:
    print("address:", addr[0])

    data = conn.recv(1024)  
    print('Received data from client: ', data)
    conn.send(b'Thank you for connecting')
    conn.close()
else:
    print('Connection from', addr, 'refused')
    conn.close()






