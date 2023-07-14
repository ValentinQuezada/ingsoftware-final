from datetime import datetime

class Operacion:
    def __init__(self, numero_remitente, numero_destino, valor):
        self.numero_remitente = numero_remitente
        self.numero_destino = numero_destino
        self.fecha = datetime.now().strftime('%d/%m/%Y')
        self.valor = valor

class Cuenta:
    def __init__(self, numero, nombre, saldo, contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = float(saldo)
        self.contactos = contactos
        self.operaciones = []

    def nueva_operacion_realizada(self, operacion: Operacion):
        nueva_operacion = f"Pago realizado de {operacion.valor} a {get_cuenta(operacion.numero_destino).nombre} el {operacion.fecha}"
        self.operaciones.append(nueva_operacion)
        self.saldo -= operacion.valor
        

    def nueva_operacion_recibida(self, operacion: Operacion):
        nueva_operacion = f"Pago recibido de {operacion.valor} de {get_cuenta(operacion.numero_remitente).nombre} el {operacion.fecha}"
        self.operaciones.append(nueva_operacion)
        self.saldo += operacion.valor

BD = []
BD.append(Cuenta("21345", "Arnaldo", 200, ["123", "456"]))
BD.append(Cuenta("123", "Luisa", 400, ["456"]))
BD.append(Cuenta("456", "Andrea", 300, ["21345"]))

def get_cuenta(numero):
    for cuenta in BD:
        if cuenta.numero == numero:
            return cuenta
    return None