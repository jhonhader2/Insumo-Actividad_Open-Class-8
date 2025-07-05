import unittest
from app import app, personas, guardar_registros_en_json
import json

class RegistroPersonasTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        # Limpiar registros para pruebas
        personas.clear()
        guardar_registros_en_json(personas)

    def test_index_carga_correcta(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'App de pruebas para el Registro de Personas', response.data)

    def test_registro_persona(self):
        data = {'nombre': 'Carlos', 'pais': 'Colombia'}
        response = self.client.post('/registrar', data=data, follow_redirects=True)
        self.assertEqual(response.status_code, 200) # Verifica que la respuesta sea exitosa
        self.assertIn(b'CARLOS', response.data)  # Se guarda en mayúsculas
        self.assertIn(b'Colombia', response.data) # Verifica que el país se haya guardado correctamente

    def test_modificacion_persona(self):
        # Primero registramos
        self.client.post('/registrar', data={'nombre': 'Laura', 'pais': 'Chile'})
        # Modificamos
        response = self.client.post('/modificar/0', data={'nombre': 'Luisa', 'pais': 'Argentina'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'LUISA', response.data)
        self.assertIn(b'Argentina', response.data)

    def test_eliminacion_persona(self):
        # Primero registramos
        self.client.post('/registrar', data={'nombre': 'Pedro', 'pais': 'Peru'})
        # Eliminamos
        response = self.client.get('/eliminar/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'PEDRO', response.data)

    def test_descarga_csv(self):
        # Registrar un dato
        self.client.post('/registrar', data={'nombre': 'Ana', 'pais': 'México'})
        # Descargar CSV
        response = self.client.get('/descargar_csv')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/csv', response.content_type)
        self.assertIn('ANA', response.data.decode('utf-8'))

    def tearDown(self):
        personas.clear()
        guardar_registros_en_json(personas)

if __name__ == '__main__':
    unittest.main()
