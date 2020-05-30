import threading
from protocolo_rpi4 import *

class BluetoothThread (threading.Thread):
    
    server_padre = None
    socket = None
    protocolo = None
    
    
    def __init__(self, padre, skt):
        threading.Thread.__init__(self)
        
        print("Entramos en el contructor de la hebra server de rpi4")
        
        self.server_padre = padre
        self.socket = skt
        self.protocolo = protocolo_rpi4()
                                    
    def run(self):
        
        print("Comenzamos a leer del socket")
        
        while True:
            inputline = self.socket.recv(1024)
            inputline = str(inputline)
            inputline = inputline[2:]
            inputline = inputline[:len(inputline) - 1]
            
            print("Lo que recibimos {}".format(inputline))
            
            
            
            
            
            