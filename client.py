import socket

# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
# client.connect((target, port))
client.connect(('127.0.0.1', 1233))
# Input UserName
#response = client.recv(2048)
#name = input(response.decode())
#client.send(str.encode(name))
# Input Password
response = client.recv(2048)
password = input(response.decode())
client.send(str.encode(password))
''' Response : Status of Connection :
	1 : Registeration successful
	2 : Connection Successful
	3 : Login Failed
'''
# Receive response
response = client.recv(2048)
response = response.decode()

print(response)
client.close()

