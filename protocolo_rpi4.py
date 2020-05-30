#Esta clase va a ser la encargada de administrar los mensajes que le llegen a la Raspberry tanto desde Android como del Servidor en Python

class protocolo_rpi4:
    
    palabra_auxiliar = None
    
    def __init__(self):
        self.palabra_auxiliar = ""
        
    #Método que va a comprobar si el mensaje que se le pasa contiene la palabra clave del protocolo y si está en la posición en al que debería estar        
    def checkIfMessageIsFromProtocol(cadena):
       
        cosas = cadena.split("#")
        
        verdadero_o_false = False
        
        if cosas[0] == "ASSISTANCESUPPORT":
            verdadero_o_false = True
            
        return verdadero_o_false
    
    #Método que va a comprobar de dónde viene el mensaje para realizar unas acciones u otras
    def checkWhereTheMessageIsFrom(cadena):
        
        cosas = cadena.split("#")
        
        de_donde_viene_el_mensaje = "";
        
        if cosas[1] == "SERVER":
            de_donde_viene_el_mensaje = "SERVER"
            
        elif cosas[1] == "APP":    
            de_donde_viene_el_mensaje = "APP"
            
        else:
            de_donde_viene_el_mensaje = "ERROR"
            
            
        return de_donde_viene_el_mensaje
    
    
     
