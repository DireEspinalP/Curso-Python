## MRO (METODO DE RESOLUCION DE ORDEN) ##
"""
Esto pasa cuando queremos hacer el llamado de un mismo metodo
de dos clases distintas y el super() busca a la clase "padre"...
D>B>C>A son como ramas desde D(B,C)-> B(A) ->A() or C(A) ->A()
"""
#Ejemplo1
class A:
    def hablar(self):
        print("A")
class B(A):
    def hablar(self):
        print("B")
class C(A):
    def hablar(self):
        print("C")
class D(B,C):
    def hablar(self):
        print("D")

d=D()
d.hablar()
print(f"{D.mro()}\n")
#Recomendacion es probar combinacion y llamadas de nuevas clases y hacer pass
#Ejemplo1
class A:
    def hablar(self):
        print("A")
class F(A):
    def hablar(self):
        print("F")
class B(A):
    def hablar(self):
        print("B")
class C(F):
    def hablar(self):
        print("C")
class D(B,C):
    def hablar(self):
        print("D")
d=D()
d.hablar()
"clase.objeto(objeto ya creado)"
F.hablar(d)
print(f"{D.mro()}\n")