#----------------Principio de inversion de dependencias----------------
"""
class Diccionario:
    def verificar_palabra(self,palabra):
        pass
class CorredorOrtografico:
    def __init__(self):
        self.diccionario=Diccionario()

    def corregir_texto(self,texto):
        pass
        
"""
from abc import ABC, abstractcmethod
class VerificadorOrtografico(ABC):
    @abstractcmethod
    def verificar_palabara(self,palabra):
        pass
class Diccionario(VerificadorOrtografico):
    def verificar_palabara(self, palabra):
        pass
class ServicioOnline(VerificadorOrtografico):
    def verificar_palabara(self, palabra):
        pass
class CorrectorOrtografico:
    def __init__(self, verificador):
        self.verificador=verificador

    def corregir_texto(self,texto):
        pass

corrector=CorrectorOrtografico(Diccionario())

"""
Este código muestra el Principio de Inversión de Dependencias: las 
clases no deben depender de otras clases concretas, sino de algo más 
general como una interfaz. Arriba, en la parte comentada, 
CorredorOrtografico crea su propio Diccionario adentro, quedando 
atrapado con esa única opción. Abajo, se soluciona creando la interfaz 
VerificadorOrtografico, de la que heredan Diccionario y ServicioOnline, 
y haciendo que CorrectorOrtografico reciba el verificador desde afuera. 
Así, se puede cambiar el verificador sin modificar el corrector.
"""