import threading
from protocolo_rpi4 import *
from horarios import *
import socket

class BluetoothThread (threading.Thread):
    
    server_padre = None
    socket = None
    protocolo = None
    
    horarios = None
    
    
    def __init__(self, padre, skt):
        threading.Thread.__init__(self)
        
        print("Entramos en el contructor de la hebra server de rpi4")
        
        self.server_padre = padre
        self.socket = skt
        self.protocolo = protocolo_rpi4()
        self.horarios = Horarios()
        
        #Vamos a asignar valores de prueba para poder comenzar a probar y tal
        self.horarios.asignarAsignaturasDePrueba()
                                    
    def run(self):
        
        print("Comenzamos a leer del socket")
        
        try:
        
            while True:
                inputline = self.socket.recv(1024)
                inputline = str(inputline)
                
                print("Lo que recibimos en crudo {}".format(inputline))
                
                inputline = inputline[2:]
                inputline = inputline[:len(inputline) - 3]
                
                print("Lo que recibimos en la hebra server {}".format(inputline))
                
                if self.protocolo.checkIfMessageIsFromProtocol(inputline):
                    print("El comienzo de la cadena está correcto")
                    
                    if self.protocolo.checkWhereTheMessageIsFrom(inputline) == "APP":
                        print("El mensaje viene de la aplicación")
                        
                        if self.protocolo.manageMessageFromApp(inputline) == "ASSISTANCE":
                            print("Vamos a tranferir los datos del alumno a la base de datos")
                            
                            dni = self.protocolo.getUserDniFromAppMessage(inputline)
                            fecha = self.protocolo.getFechaFromAppMessage(inputline)
                            print("TODO GUAY")
                            asig = self.horarios.obtenerAsignaturaParaRegistrarAsistenciaEnBaseADiaYHora(fecha)
                            
                            HOST = '192.168.1.39'
                            PORT = 39999

                            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                                print('Entramos en la parte en la que conectamos con el server')
                                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                client.connect(('192.168.1.39', 39999))


                                client.send(bytes(str("ASSISTANCESUPPORT#RPI4#REGISTERASSISTANCE#{}#{}#{}".format(dni, fecha, asig)), "utf-8"))

                                client.close()
                                
                                                    
        except Exception as ex:
            print("Excepcion en la hebra:", ex)
        
            
        finally:
            self.socket.close
            
                                
                         
                    
                    
            
            
                