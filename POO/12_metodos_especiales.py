
# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                    MÉTODOS ESPECIALES (DUNDER METHODS)                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝

# ── Aritméticos ──────────────────────────────────────────────────────────────
# __add__(self, other)  →  Sobrecarga del operador de suma          (+)
# __sub__(self, other)  →  Sobrecarga del operador de resta         (-)
# __mul__(self, other)  →  Sobrecarga del operador de multiplicación (*)
# __div__(self, other)  →  Sobrecarga del operador de división      (/)
# __mod__(self, other)  →  Sobrecarga del operador de módulo        (%)
# __pow__(self, other)  →  Sobrecarga del operador de exponenciación (**)

# ── Comparación ───────────────────────────────────────────────────────────────
# __eq__(self, other)   →  Sobrecarga del operador de igualdad            (==)
# __ne__(self, other)   →  Sobrecarga del operador de desigualdad         (!=)
# __lt__(self, other)   →  Sobrecarga del operador "menor que"            (<)
# __gt__(self, other)   →  Sobrecarga del operador "mayor que"            (>)
# __le__(self, other)   →  Sobrecarga del operador "menor o igual que"    (<=)
# __ge__(self, other)   →  Sobrecarga del operador "mayor o igual que"    (>=)

# ── Asignación ────────────────────────────────────────────────────────────────
# __iadd__(self, other) →  Suma en asignación                (+=)
# __isub__(self, other) →  Resta en asignación                (-=)
# __imul__(self, other) →  Multiplicación en asignación       (*=)
# __idiv__(self, other) →  División en asignación             (/=)
# __imod__(self, other) →  Módulo en asignación               (%=)
# __ipow__(self, other) →  Exponenciación en asignación       (**=)

# ── Otros ─────────────────────────────────────────────────────────────────────
# __str__(self)              →  Representación legible del objeto como cadena
# __len__(self)              →  Devuelve la longitud del objeto
# __getitem__(self, index)   →  Permite acceder a elementos por índice ([])


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
     return f"Persona(nombre={self.nombre}, edad={self.edad})"
    def __repr__(self):
      return f"Persona('{self.nombre}', {self.edad})"

#Directo en python
dalto=Persona("Dire", 18)
print(dalto) # Esto llamará al metodo __str__ de la clase Persona
#Indirecto en python
lista=[1,2,3,4,5]
print(lista) # Esto llamará al metodo __str__ de la clase list

representacion=repr(dalto) # Esto llamará al metodo __repr__ de la clase Persona
resultado=eval(representacion) # Esto ejecutará el codigo que esta en la variable representacion
print(resultado) # Esto imprimirá el objeto creado a partir de la representacion


#-----------SOBRECARGA DE OPERADORES----------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
     return f"Persona(nombre={self.nombre}, edad={self.edad})"
    def __repr__(self):
      return f"Persona('{self.nombre}', {self.edad})"
    def __add__(self, otro):
        nuevo_valor=self.edad+otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)


dire=Persona(" Dire ",18)
pedro=Persona(" Pedro ",30)
maria=Persona(" Maria ",20)

nueva_persona=dire+pedro+maria
print(nueva_persona.nombre)
print(nueva_persona.edad)


