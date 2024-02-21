import socket
import Convert
import pyautogui as pg

class Server():
    def __init__(self):
        size = pg.size()
        self.regeon = self.regeon = (0,0, size[0], size[1])

        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # get local machine name
        self.host = socket.gethostname()                           

        self.port = 4444

        self.convert = Convert.Convert()

    def stop(self):
        self.serversocket.shutdown(socket.SHUT_RDWR)
        self.serversocket.close()
        print ("closed")

    def send(self):
        print(self.clientsocket.sendall(self.convert.read(self.received_message,self.regeon)))

    def update_regeon(self, new_regeon):
        self.regeon = new_regeon
    
    def startServer(self, port):

        self.port = port

        

        # create a socket object


        try:

            # bind to the port
            self.serversocket.bind((self.host, self.port))                                  

            # queue up to 5 requests
            self.serversocket.listen(1)                                           
            print(f" Host: {self.host} | Server Ip: {socket.gethostbyname(self.host)} | Server Port: {self.port}")
            while True:
                print("waiting for connection")
                self.clientsocket, self.addr = self.serversocket.accept()  
                self.received_message = self.clientsocket.recv(1024).decode()
                
                print("connection received")
                print("Got a connection from %s" % str(self.addr))
                print(self.received_message)
                self.send()

                while True:
                    self.clientsocket, self.addr = self.serversocket.accept()

                    self.received_message = self.clientsocket.recv(1024).decode()
                    print(self.received_message)

                    
                    self.send()
        except Exception as E:
            print(E)
            self.clientsocket.close()
            
