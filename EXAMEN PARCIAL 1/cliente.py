class Cliente:
    nombre   = str
    edad     = int
    telefono = str
    
    def __init__(self, nombre, edad, telefono):
        self.nombre   = nombre
        self.edad     = edad 
        self.telefono = telefono
        
    def __str__(self):
        return f"El nombre de nuestra clienta es {self.nombre}, su edad es: {self.edad} años y su telefono es: {self.telefono}"
       
persona1 = Cliente ("Liliana Alulema", 21, "0987452136")

print(persona1)