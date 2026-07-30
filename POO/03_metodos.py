 ## Metodos ##

class Celular():
  
   def __init__(self,marca,modelo,camara):  
      self.marca=marca
      self.modelo=modelo
      self.camara=camara
   #Las metodos (Acciones/funciones)
   def llamar(self):# El parametro SELF hace referencia al OBJETO
      print(f"Estas haciendo un llamado desde un: {self.modelo}") #siempre tiene q estar self 
   def cortar(self):
      print(f"Cortaste la llamada desde tu: {self.modelo}")      

#Objetos
celular1=Celular("Samsung","S23","49MP")
celular2=Celular("Apple","Iphone 15 Pro","96MP")

print(celular1.marca)

print(celular2.llamar())
celular1.llamar()
celular2.cortar()