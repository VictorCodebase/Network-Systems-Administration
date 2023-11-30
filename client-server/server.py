import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#create socket, family ipv4, type stream
ip = socket.gethostbyname(socket.gethostname())
allowedIP = ip
port = 3000


s.bind(('', port)) 
s.listen(2) 
print('Server is listening')

while True:
    # Accept incoming connections
    conn, addr = s.accept() 

    print('Got connection from', addr)

    if addr[0] == allowedIP:
        print("address:", addr[0])

        #receiving and decoding data
        data = conn.recv(1024) 
        data  = data.decode()


        print('Received data from client: ', data)
        conn.send(b'Thank you for connecting')
        conn.close()
        if(data == "close"):
            print("closing server...")
            break
    else:
        print('Connection from', addr, 'refused')
        conn.close()





