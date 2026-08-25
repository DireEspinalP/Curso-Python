#----------------PRINCIPIO DE SUSTITUCION DE LISKOV----------------
"""
class Ave:
    def volar(self):
        return "Estoy volando"

class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"


def hacer_volar(ave=Ave):
    return ave.volar()

print(hacer_volar(Pinguino()))
"""
class Ave:
    pass
class AveVoladora(Ave):
    def volar(delf):
        return "ESTOY VOLANDO"

class AveNoVoladora(Ave):
    pass

"""
Este código muestra el Principio de Sustitución de Liskov con este ejemplo
donde no todas las aves vuelan, así que no todas deberían prometer que 
pueden hacerlo. Arriba, en la parte comentada, Pinguino hereda de Ave 
pero no puede cumplir con volar(), lo cual está mal diseñado. Abajo, se 
soluciona separando las aves en dos grupos: las que vuelan (AveVoladora) 
y las que no (AveNoVoladora). Así, cada ave hereda del grupo correcto 
y el código se comporta como se espera, sin sorpresas ni errores.
"""