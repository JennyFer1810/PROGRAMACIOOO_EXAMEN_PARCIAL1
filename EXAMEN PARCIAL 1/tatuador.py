class Tatuador:
    nombre    = str
    edad      = int
    telefono  = str
    trabajo   = str 
    
    def __init__ (self, nombre, edad, telefono, trabajo):
        self.nombre   = nombre
        self.edad     = edad
        self.telefono = telefono
        self.trabajo  = trabajo
        
    def tatuar(self):
        return f"Hola {self.nombre}, tienes {self.edad} años, tu telefono es {self.telefono} y trabajas en {self.trabajo}"
    
jefe = Tatuador("Jonathan Acosta", 20, "0987456321", "Presicion tatto")
print(vars(jefe))      
jefe.tatuar()    
        
        
class Jefe(Tatuador):
    
    direccion = str
    
    def __init__(self, nombre, edad, telefono, trabajo, direccion):
        Jefe.__init__(self, nombre, edad, telefono, trabajo)
        
        self.direccion = direccion    
         

 
 
