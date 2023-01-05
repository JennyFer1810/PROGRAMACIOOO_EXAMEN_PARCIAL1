from tatuador import Tatuador
from ayudante import Ayudante
from cliente import Cliente
from tatuadorNuevo import TatuadorNuevo

if __name__ == "__main__":

  print("TATUADOR:")
  tatuador1 = Tatuador("Jennyfer Chalacan", 20, "098974536", "Presicion tatto")
  print(vars(tatuador1))
    
  tatuador2 = Tatuador("Kerlly Aconda", 22, "098546923", "Las casas")
  print(vars(tatuador2))
    
  print("AYUDANTE:")
  ayudante1 = Ayudante("Jonathan Diaz", 25, "09965874", "La comuna alta", 18, "3 años")
  print(vars(ayudante1))
    
  ayudante2 = Ayudante("Jefferson Chimborazo", 21, "09965874", "el reten", 22, "5 años")
  print(vars(ayudante2))

  print("CLIENTE:")
  cliente1 = Cliente("Dilan Bonilla", 25, "09965874")
  print(vars(cliente1))
    
  cliente2 = Cliente("Maria Hilasaca", 21, "09965874")
  print(vars(cliente2))
  
  print("TATUADOR_NUEVO:")
  tatuadorNuevo1 = TatuadorNuevo("Mauricio Ontaneda", 25, "09965874", "La comuna alta", "2 años")
  print(vars(tatuadorNuevo1))
    
  tatuadorNuevo2 = TatuadorNuevo("Diego Pinsag", 21, "09965874", "el reten", "1 año")
  print(vars(tatuadorNuevo2))
  
