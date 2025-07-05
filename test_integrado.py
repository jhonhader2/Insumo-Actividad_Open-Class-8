import unittest
import os
from datetime import datetime
from app import app, personas, guardar_registros_en_json
import HtmlTestRunner
from glob import glob
import webbrowser


# Rutas
LOG_TXT = 'registro_pruebas.txt'
HTML_REPORT_DIR = 'reporte'

# Función para registrar en .txt
def registrar_en_txt(nombre_prueba, resultado):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entrada = (
        f"\n===============================\n"
        f"🧪 PRUEBA: {nombre_prueba}\n"
        f"🕒 FECHA Y HORA: {timestamp}\n"
        f"📄 RESULTADO: {resultado}\n"
        f"===============================\n"
    )
    with open(LOG_TXT, 'a', encoding='utf-8') as f:
        f.write(entrada)

# Clase de pruebas
class RegistroPersonasTestCase(unittest.TestCase):

    def setUp(self): # Configuración antes de cada prueba, self es una referencia a la instancia de la clase (convención de Python que hace referencia al propio objeto de prueba (es decir, a la instancia de la clase)
        self.client = app.test_client()
        self.client.testing = True
        personas.clear()
        guardar_registros_en_json(personas)

    def test_index(self):
        try:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            registrar_en_txt("Cargar Página Principal", "✅ Éxito")
        except AssertionError:
            registrar_en_txt("Cargar Página Principal", "❌ Fallo")
            raise

    def test_registro(self):
        try:
            response = self.client.post('/registrar', data={'nombre': 'Carlos', 'pais': 'Colombia'}, follow_redirects=True)
            self.assertIn(b'CARLOS', response.data)
            registrar_en_txt("Registrar Persona", "✅ Éxito")
        except AssertionError:
            registrar_en_txt("Registrar Persona", "❌ Fallo")
            raise

    def test_modificar(self):
        self.client.post('/registrar', data={'nombre': 'Laura', 'pais': 'Chile'})
        try:
            response = self.client.post('/modificar/0', data={'nombre': 'Luisa', 'pais': 'Argentina'}, follow_redirects=True)
            self.assertIn(b'LUISA', response.data)
            registrar_en_txt("Modificar Persona", "✅ Éxito")
        except AssertionError:
            registrar_en_txt("Modificar Persona", "❌ Fallo")
            raise

    def test_eliminar(self):
        self.client.post('/registrar', data={'nombre': 'Pedro', 'pais': 'Peru'})
        try:
            response = self.client.get('/eliminar/0', follow_redirects=True)
            self.assertNotIn(b'PEDRO', response.data)
            registrar_en_txt("Eliminar Persona", "✅ Éxito")
        except AssertionError:
            registrar_en_txt("Eliminar Persona", "❌ Fallo")
            raise

    def test_descargar_csv(self):
        self.client.post('/registrar', data={'nombre': 'Ana', 'pais': 'México'})
        try:
            response = self.client.get('/descargar_csv')
            self.assertEqual(response.status_code, 200)
            self.assertIn('text/csv', response.content_type)
            registrar_en_txt("Descargar CSV", "✅ Éxito")
        except AssertionError:
            registrar_en_txt("Descargar CSV", "❌ Fallo")
            raise

    def tearDown(self):
        personas.clear()
        guardar_registros_en_json(personas)

# Mostrar ruta HTML generada
def mostrar_ultima_ruta_html():
    archivos = sorted(glob(f'{HTML_REPORT_DIR}/TestResults__*.html'), reverse=True)
    if archivos:
        ruta_absoluta = os.path.abspath(archivos[0])
        enlace = f"file:///{ruta_absoluta.replace(os.sep, '/')}"
        print(f"\n✅ Reporte HTML generado: {ruta_absoluta}")
        print(f"🌐 Puedes abrirlo directamente en tu navegador:\n{enlace}")
        # Opcional: abre automáticamente el navegador predeterminado
        webbrowser.open(enlace)
    else:
        print("⚠️ No se encontró ningún reporte HTML.")

# Ejecutar pruebas
if __name__ == '__main__':
    os.makedirs(HTML_REPORT_DIR, exist_ok=True) # Asegurarse de que el directorio existe
    print("\n🧪 Ejecutando pruebas funcionales...") 

    unittest.main( # Ejecutar las pruebas de manera que se genere un reporte HTML
        testRunner=HtmlTestRunner.HTMLTestRunner(output=HTML_REPORT_DIR),
        verbosity=2
    )

    mostrar_ultima_ruta_html()
