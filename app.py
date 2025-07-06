from flask import Flask, request, render_template, redirect, jsonify  # Importar las clases necesarias de Flask para la aplicación web
import json # Importar el módulo json para trabajar con archivos JSON
import requests # Importar el módulo requests para realizar solicitudes HTTP
import csv # Importar el módulo csv para trabajar con archivos CSV
from io import StringIO # Importar StringIO para manejar cadenas como archivos
from flask import Response # Importar Response para enviar respuestas personalizadas

app = Flask(__name__)  # Crear una instancia de la clase Flask

# Lista para almacenar las personas y sus países
personas = []

# Función para cargar registros desde el archivo JSON al inicio
def cargar_registros_desde_json():
    try:
        with open('registros.json', 'r') as json_file:
            registros = json.load(json_file)
            return registros
    except FileNotFoundError:
        return []

# Función para obtener la lista de países desde la API
def obtener_paises_desde_api():
    try:
        response = requests.get('https://restcountries.com/v2/all?fields=name')
        if response.status_code == 200:
            data = response.json()
            countries = [country['name'] for country in data]
            return sorted(countries)  # para ordenar alfabéticamente
        else:
            return []
    except Exception as e:
        print("Error al obtener países:", e)
        return []

# Función para verificar si existe una persona con el mismo nombre
def verificar_duplicado(nombre, exclude_index=None):
    """
    Verifica si ya existe una persona con el mismo nombre.
    
    Args:
        nombre (str): Nombre a verificar (en mayúsculas)
        exclude_index (int, optional): Índice a excluir de la verificación (para modificaciones)
    
    Returns:
        bool: True si existe duplicado, False en caso contrario
    """
    for i, persona in enumerate(personas):
        if exclude_index is not None and i == exclude_index:
            continue  # Saltar el índice actual en caso de modificación
        if persona['nombre'] == nombre:
            return True
    return False


# Cargar registros al iniciar la aplicación
personas = cargar_registros_desde_json()

@app.route('/')
def index():
    countries = obtener_paises_desde_api()
    return render_template('index.html', personas=personas, countries=countries)


@app.route('/registrar', methods=['POST']) # Decorador para la ruta de registro
def registrar():
    nombre = request.form.get('nombre').upper()  # Convertir el nombre a mayúsculas
    pais = request.form.get('pais')
    
    # Verificar si ya existe una persona con el mismo nombre
    if verificar_duplicado(nombre):
        return redirect('/?error=duplicado&nombre=' + nombre)
    
    personas.append({'nombre': nombre, 'pais': pais})
    guardar_registros_en_json(personas)
    return redirect('/?success=true')

@app.route('/eliminar/<int:index>', methods=['GET']) # Decorador para la ruta de eliminación
def eliminar(index):
    if 0 <= index < len(personas):
        nombre = personas[index]['nombre']
        pais = personas[index]['pais']
        del personas[index]
        guardar_registros_en_json(personas)
    return redirect('/?success=true')

@app.route('/modificar/<int:index>', methods=['GET', 'POST']) # Decorador para la ruta de modificación
def modificar(index):
    if request.method == 'GET':
        if 0 <= index < len(personas):
            persona = personas[index]
            countries = obtener_paises_desde_api()
            return render_template('modificar.html', index=index, persona=persona, countries=countries)
        return redirect('/')
    elif request.method == 'POST':
        if 0 <= index < len(personas):
            nombre = request.form.get('nombre').upper()
            pais = request.form.get('pais')
            
            # Verificar si ya existe otra persona con el mismo nombre (excluyendo el actual)
            if verificar_duplicado(nombre, exclude_index=index):
                return redirect('/?error=duplicado&nombre=' + nombre)
            
            personas[index] = {'nombre': nombre, 'pais': pais}
            guardar_registros_en_json(personas)
        return redirect('/?success=true')

# Ruta para cargar los registros en formato JSON
@app.route('/personas_json')
def cargar_personas_json():
    return jsonify(personas)

# Ruta para verificar duplicados
@app.route('/verificar_duplicado/<nombre>')
def verificar_duplicado_api(nombre):
    nombre_upper = nombre.upper()
    es_duplicado = verificar_duplicado(nombre_upper)
    return jsonify({
        'duplicado': es_duplicado,
        'nombre': nombre_upper
    })

# Función para guardar los registros en un archivo JSON
def guardar_registros_en_json(registros):
    with open('registros.json', 'w') as json_file:
        json.dump(registros, json_file)


@app.route('/descargar_csv')
def descargar_csv():
    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['Nombre', 'País'])  # Encabezados con tilde

    for persona in personas:
        writer.writerow([persona['nombre'], persona['pais']])

    output = '\ufeff' + si.getvalue()  # Agregar BOM UTF-8 al inicio
    si.close()

    return Response(
        output,
        mimetype='text/csv; charset=utf-8',
        headers={"Content-Disposition": "attachment;filename=personas.csv"}
    )

# Nueva ruta para descarga CSV con respuesta JSON
@app.route('/descargar_csv_json')
def descargar_csv_json():
    try:
        si = StringIO()
        writer = csv.writer(si)
        writer.writerow(['Nombre', 'País'])

        for persona in personas:
            writer.writerow([persona['nombre'], persona['pais']])

        output = '\ufeff' + si.getvalue()
        si.close()

        return jsonify({
            'success': True,
            'message': 'Archivo CSV generado correctamente',
            'data': output,
            'filename': 'personas.csv'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error al generar CSV: {str(e)}'
        }), 500


if __name__ == '__main__':  # Comprobar si el script se ejecuta directamente
    app.run(debug=True)   # Ejecutar la aplicación en modo de depuración
