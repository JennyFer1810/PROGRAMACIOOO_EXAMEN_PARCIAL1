from tatuador import Tatuador

class TatuadorNuevo(Tatuador):
    
    tiempoExperiencia = int
    
    def __init__(self, nombre, edad, telefono, trabajo, tiempoExperiencia):
        super().__init__(nombre, edad, telefono, trabajo)
        
        self.tiempoExperiencia  = tiempoExperiencia
        
def __str__(self):
        return f"Hola! soy {self.nombre}, mi edad es: {self.edad} años, mi telefono es: {self.telefono}, mi telefono es {self.telefono} y mi tiempo de experiencia es {self.tiempoExperiencia}"
         
if __name__ == "__main__":
    
   persona3 = TatuadorNuevo ("Belen Rojas", 26, "0987452136", "tatoo quito", "6 años")
   print(persona3) 