import unittest
from app import app
import json

class TestBilletera(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client

    # Prueba unitaria para 1 caso de éxito:
    ## Prueba 1: Se desea verificar los contactos de la cuenta 21345.
    def test_get_contactos_exito(self):
        response = self.client().get('/billetera/contactos?minumero=21345')
        data = json.loads(response.data)
        self.assertEqual(data['statusCode'], 200)
        self.assertEqual(data['contactos'], {'123': 'Luisa', '456': 'Andrea'})

    # Pruebas unitarias para 3 casos de error:
    ## Prueba 2: Se desea verificar que la cuenta '69' no existe al intentar acceder a sus contactos.
    def test_get_contactos_error(self):
        response = self.client().get('/billetera/contactos?minumero=69')
        data = json.loads(response.data)
        self.assertEqual(data['statusCode'], 404)
        self.assertEqual(data['response'], 'Cuenta 69 no encontrada.')

    ## Prueba 3: Se desea verificar que la cuenta '69' no existe al intentar realizar una operación a su nombre.
    def test_realizar_operacion_sin_remitente(self):
        response = self.client().get('/billetera/pagar?minumero=69&numerodestino=123&valor=100')
        data = json.loads(response.data)
        self.assertEqual(data['statusCode'], 404)
        self.assertEqual(data['response'], 'Cuenta remitente 69 no encontrada.')

    ## Prueba 4: Se desea verificar que la cuenta '456' no es contacto de la cuenta '123' al intentar realizar una
    ## operación al nombre de esta última.
    def test_realizar_operacion_no_contacto(self):
        response = self.client().get('/billetera/pagar?minumero=456&numerodestino=123&valor=100')
        data = json.loads(response.data)
        self.assertEqual(data['statusCode'], 400)
        self.assertEqual(data['response'], 'Cuenta destino 123 no es contacto de remitente 456.')