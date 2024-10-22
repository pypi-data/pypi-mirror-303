class Exception401(Exception):
    def __init__(self):
        self.message = "Usuário não autorizado ou token inválido."
        
    def __str__(self):
        return self.message
    

class Exception403(Exception):
    def __init__(self,message):
        self.message = message if message  else "Usuário não autorizado para utilizar este recurso."
        
    def __str__(self):
        return self.message
    
class Exception409(Exception):
    def __init__(self):
        self.message = "Token expirado."
        
    def __str__(self):
        return self.message