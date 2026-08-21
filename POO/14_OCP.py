#----------------PRINCIPIO DE ABIERTO/CERRADO------------
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por SMS a {self.usuario.sms}")

class NotificadorTwitter(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por twit a {self.usuario.twit}")

class Usuario:
    def __init__(self, email, sms, twit):
        self.email = email
        self.sms = sms
        self.twit = twit


usuario1 = Usuario(email="juan@correo.com", sms="+51999999999", twit="@juan123")

notificador_email = NotificadorEmail(usuario1, "Tu pedido fue enviado")
notificador_sms = NotificadorSMS(usuario1, "Tu pedido fue enviado")
notificador_twitter = NotificadorTwitter(usuario1, "Tu pedido fue enviado")

notificador_email.notificar()
notificador_sms.notificar()
notificador_twitter.notificar()

"""
Este código sigue el Principio de Abierto/Cerrado, que dice que una clase 
debe estar abierta para agregar cosas nuevas, pero cerrada para que no 
tengamos que modificar lo que ya existe. Aquí tenemos una clase base 
llamada Notificador, que solo dice que todo notificador debe tener un 
método notificar, pero no dice cómo debe hacerlo. Luego creamos clases 
hijas como NotificadorEmail, NotificadorSMS y NotificadorTwitter, y cada 
una decide a su manera cómo enviar el mensaje. Si en el futuro queremos 
agregar un nuevo tipo de notificación, por ejemplo por WhatsApp, no 
necesitamos tocar ni cambiar el código que ya funciona, solo creamos una 
clase nueva que también use el método notificar. Esto evita que rompamos 
algo que ya estaba funcionando y hace que el código sea más fácil de 
hacer crecer sin miedo a dañar lo anterior.
"""