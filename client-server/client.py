'''
client server project
NSA

Members
Daniel Wekesa - SCT212-0183/2022
Josiah Ndirangu - SCT212-0111/2022
Samuel Gicheha - SCT212-0118/2022
Ttsumah Derick Richard - SCT212-0192/2022
Mark Victor Kithinji - SCT212-0105/2022

'''
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


port = 3000
ip = socket.gethostbyname(socket.gethostname())

connectionString =(ip, port)
s.connect(connectionString)




message = input("Enter sample message to send to server: ")
s.send(message.encode()) 


print(s.recv(1024))

s.close()

