from tatuador import Tatuador

class Ayudante(Tatuador):
    idAyudante = int
    practicas  = str
    
    def __init__(self, nombre, edad, telefono, trabajo, idAyudante, practicas):
        super().__init__(nombre, edad, telefono, trabajo)
        
        self.idAyudante  = idAyudante
        self.practicas   = practicas
    
    