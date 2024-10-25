import socket
import time
import threading
import hashlib


class Main(object):
    host = '127.0.0.1'
    port = 1233
    ThreadCount = 0
    HashTable = {"40bd001563085fc35165329ea1ff5c5ecbdbbeef","345","123"}

    # Function : For each client
    @classmethod
    def threaded_client(cls, connection):
        #connection.send(str.encode('ENTER USERNAME : ')) # Request Username
        #name = connection.recv(2048)
        connection.send(str.encode('ENTER PASSWORD : ')) # Request Password
        password = connection.recv(2048)
        password = password.decode()
        #name = name.decode()
        #password=hashlib.sha1(str.encode(password)).hexdigest() # Password hash using SHA256
        # REGISTERATION PHASE
        # If new user,  regiter in Hashtable Dictionary
        #if name not in cls.HashTable:
        #    cls.HashTable[name]=password
        #    connection.send(str.encode('Registeration Successful'))
        #    print('Registered : ',name)
        #    print("{:<8} {:<20}".format('USER','PASSWORD'))
        #    for k, v in cls.HashTable.items():
        #        label, num = k,v
        #        print("{:<8} {:<20}".format(label, num))
        #    print("-------------------------------------------")

        #else:
        # If already existing user, check if the entered password is correct
        #if(cls.HashTable[name] == password):
        if password in cls.HashTable:
            connection.send(str.encode('Connection Successful')) # Response Code for Connected Client
            print('Connected : ',password)
        else:
            connection.send(str.encode('Login Failed')) # Response code for login failed
            print('Connection denied : ',password)
        while True:
            break
        connection.close()

    @classmethod
    def run(cls):
        ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
        try:
            ServerSocket.bind((cls.host, cls.port))
        except socket.error as e:
            print(str(e))
        print('Waitiing for a Connection..')
        ServerSocket.listen(5)

        while True:
            time.sleep(1)
            Client, address = ServerSocket.accept()
            client_handler = threading.Thread(
                target=cls.threaded_client,
                args=(Client,)
            )
            client_handler.start()
            cls.ThreadCount += 1
            print('Connection Request: ' + str(cls.ThreadCount))

        ServerSocket.close()

if __name__ == "__main__":
    Main.run()
