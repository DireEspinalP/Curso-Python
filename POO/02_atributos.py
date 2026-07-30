 ## Clases ##
#Recomendacion PascalCase

# Un objeto es una instancia de clase
class Celular():
   #Atributos (Caracteristicas)
   def __init__(self,marca,modelo,camara): #Accedemos a sus atributos
      self.marca=marca
      self.modelo=modelo
      self.camara=camara
 #self es como "celular pero para todos"
celular1=Celular("Samsung","S23","49MP")
celular2=Celular("Apple","Iphone 15 Pro","96MP")

print(celular1.marca)