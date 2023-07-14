from flask import Flask, request, jsonify, abort
from models import *

app = Flask(__name__)

@app.route("/billetera/contactos", methods=["GET"])
def get_contactos():
    numero = request.args.get("minumero")
    cuenta = get_cuenta(numero)
    if cuenta is None:
        return jsonify({
            "statusCode": 404,
            "response": f"Cuenta {numero} no encontrada."
        })
    contactos = {}
    for contacto in cuenta.contactos:
        contactos[contacto] = get_cuenta(contacto).nombre

    return jsonify({
        "statusCode": 200,
        "contactos" : contactos
        }
    )

@app.route("/billetera/pagar", methods=["GET"])
def realizar_operacion():
    mi_numero = request.args.get("minumero")
    numero_destino = request.args.get("numerodestino")
    valor = float(request.args.get("valor"))
    
    cuenta_remitente = get_cuenta(mi_numero)
    cuenta_destino = get_cuenta(numero_destino)
    if cuenta_remitente is None:
        return jsonify({
            "statusCode": 404,
            "response": f"Cuenta remitente {mi_numero} no encontrada."
            }
        )
    if cuenta_destino is None:
        return jsonify({
            "statusCode": 404,
            "response": f"Cuenta destino {numero_destino} no encontrada."
            }
        )
    if numero_destino not in cuenta_remitente.contactos:
        return jsonify({
            "statusCode": 400,
            "response": f"Cuenta destino {numero_destino} no es contacto de remitente {mi_numero}."
            }
        )

    operacion = Operacion(mi_numero, numero_destino, valor)
    cuenta_remitente.nueva_operacion_realizada(operacion)
    cuenta_destino.nueva_operacion_recibida(operacion)
    
    return jsonify({
        "statusCode": 200,
        "response": f"Realizado en {operacion.fecha}"
    })

@app.route("/billetera/historial", methods=["GET"])
def get_historial():
    numero = request.args.get("minumero")
    cuenta = get_cuenta(numero)
    if cuenta is None:
        return jsonify({
            "statusCode": 404,
            "response": f"Cuenta {numero} no encontrada."
        })
    operaciones = cuenta.operaciones
    saldo = cuenta.saldo
    nombre = cuenta.nombre
    historial = f"Operaciones de {nombre}: "
    if len(operaciones) == 0:
        historial = f"{historial}Nignuna."
    else:
        for operacion in operaciones:
            historial = f"{historial}{operacion}, "
        historial = historial[:-2] + "."
    
    
    return jsonify({
        "statusCode": 200,
        "saldo": f"Saldo de {nombre}: {saldo}",
        "historial" : historial
        })

if __name__ == "__main__":
    app.run()

