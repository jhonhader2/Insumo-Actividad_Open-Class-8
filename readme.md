# Instalar el Framework Flask:
pip install Flask

# Instalar para realizar las pruebas y generar el html de logs
pip install html-testRunner

# Ejecutar el programa:
python app.py

# ejecución de pruebas:
python test_integrado.py



# _______________Estructura del proyecto________________________________________________________________
02_DEBUGGING_TEST_INSUMO ACTIVIDAD_OPEN CLASS 8/
│
├── app.py                          # Aplicación principal Flask
├── test_app.py                    # Script de prueba básico con unittest
├── test_integrado.py              # Script de prueba con logs y HTML report
├── registro_pruebas.txt           # Registro acumulado de resultados de pruebas
├── registros.json                 # Almacén de datos de personas en formato JSON
├── readme.md                      # Documentación del proyecto
│
├── static/
│   └── style.css                  # Hoja de estilos para la interfaz
│
├── templates/
│   ├── index.html                 # Vista principal (formulario de registro)
│   └── modificar.html            # Vista para modificar una persona
│
└── reporte/
    └── TestResults_*.html        # Archivos HTML generados por HtmlTestRunner


# partes del proyecto y su relación:

+------------------+         +-------------------+         +--------------------+
|    app.py        +--------> templates/index.html        |    test_app.py      |
| (Backend Flask)  |         | templates/modificar.html    |    test_integrado.py|
+------------------+         +-------------------+         +--------------------+
       |                             |                              |
       v                             v                              v
registros.json              static/style.css               registro_pruebas.txt
       |                                                        reporte/
       |                                                         |
       +---------------------------------------------------------+


# Estructura general del proyecto y relaciones

1. app.py – Lógica principal de la aplicación Flask
# ¿Qué hace?
-Define las rutas del servidor (/, /registrar, /eliminar/<id>, etc.).
-Administra la lista de personas (personas), cargándola desde un archivo JSON.
-Usa la API pública restcountries.com para obtener la lista de países.
-Renderiza HTML desde la carpeta templates/.
Permite guardar los registros en registros.json.

# Relación con otras partes:
-Usa templates/index.html y templates/modificar.html para mostrar las vistas.
-Usa static/style.css para aplicar estilos.
-Lee y escribe en registros.json.
-Se prueba mediante test_app.py y test_integrado.py.

2. templates/ – Vistas HTML (Frontend)
# Archivos:
index.html: Página principal con formulario para registrar personas y tabla de registros.
modificar.html: Formulario para editar un registro existente.
# Relación con otras partes:
Flask (en app.py) usa render_template() para mostrar estas vistas.
Se conectan con las rutas /, /modificar/<index> y /registrar.
Son estilizadas con static/style.css.

3. static/style.css – Estilos visuales
Define cómo se ve la aplicación (colores, tablas, botones).
Se aplica automáticamente cuando los HTML se renderizan (vía url_for('static', filename='style.css')).

4. registros.json – Base de datos de respaldo
Archivo JSON donde se guarda la lista de personas.
Permite mantener persistencia entre reinicios de la app.
# Usado por:
app.py, mediante las funciones cargar_registros_desde_json() y guardar_registros_en_json().

5. registro_pruebas.txt – Bitácora acumulativa de pruebas
Cada vez que corres test_integrado.py, se añade un registro con el resultado de cada prueba y la hora.
Te permite auditar la calidad del sistema a lo largo del tiempo.

6. test_app.py – Script de pruebas básicas
Ejecuta pruebas automáticas sobre la app usando unittest.
Verifica funcionalidades como: registrar, editar, eliminar, cargar la página, descargar CSV.

7. test_integrado.py – Pruebas avanzadas con logs y HTML
Ejecuta las mismas pruebas funcionales que test_app.py, pero con mejoras:

📄 Guarda resultados acumulativos en registro_pruebas.txt.
🌐 Genera un reporte HTML interactivo en la carpeta reporte/.
🧭 Muestra enlaces directos para abrir el reporte.

8. reporte/ – Carpeta de reportes HTML
Al ejecutar test_integrado.py, se genera un archivo .html por cada sesión de pruebas.
Muestra qué pruebas pasaron o fallaron con detalle visual.

9. readme.md – Documentación del proyecto
# Documento Markdown donde puedes explicar:
Qué hace la app.
Cómo se instala y ejecuta.
Cómo correr las pruebas.


