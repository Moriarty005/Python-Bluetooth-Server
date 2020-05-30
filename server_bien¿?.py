import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *
from bluetooth_server_thread import *
import threading


class BluetoothServer (threading.Thread):
    
    server_sock = None
    port = None
    server_thread_list = None
    excepcion = None
    
    def __init__(self):
        
        threading.Thread.__init__(self)
        self.server_thread_list = []
        self.excepcion = True
        
    def run(self):
        server_sock=BluetoothSocket( RFCOMM )
        server_sock.bind(("",PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]

        uuid = "9318353d-e586-42e3-8477-f8a1d84252b2"

        advertise_service( server_sock, "PruebaServerAlexinio",
                           service_id = uuid,
                           service_classes = [ uuid, SERIAL_PORT_CLASS ],
                           profiles = [ SERIAL_PORT_PROFILE ] )


        try:

            while self.excepcion:          
                print ("Waiting for connection on RFCOMM channel {}".format(port))
                
                client_sock, client_info = server_sock.accept()
                print ("Accepted connection from ", client_info)
                
                hebra = BluetoothThread(self, client_sock)
                print("Cosa1")
                self.server_thread_list.append(hebra)
                print("Cosa2")
                self.server_thread_list[-1].run()
                
                print("Cosa3")
                
        except NameError as e:
            print("Error: ", e)
            
        except:

            print ("disconnected")
            server_sock.close()
            
            excepcion = False
            print ("all done")
        
        finally:
            
            print ("disconnected")
            server_sock.close()
            
            excepcion = False
            print ("all done")
                

cosa2 = BluetoothServer()
cosa2.run()
