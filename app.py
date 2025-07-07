from flask import Flask, request, render_template, redirect, jsonify, Response
import json # Importar el módulo json para trabajar con archivos JSON
import requests # Importar el módulo requests para realizar solicitudes HTTP
import csv # Importar el módulo csv para trabajar con archivos CSV
from io import StringIO # Importar StringIO para manejar cadenas como archivos
from typing import List, Dict, Optional, Union
from dataclasses import dataclass


@dataclass
class Persona:
    """Clase para representar una persona con nombre y país"""
    nombre: str
    pais: str
    
    def __post_init__(self):
        """Convertir el nombre a mayúsculas después de la inicialización"""
        self.nombre = self.nombre.upper()


class GestorPersonas:
    """Clase responsable de gestionar las personas (Single Responsibility)"""
    
    def __init__(self, archivo_registros: str = 'registros.json'):
        self.archivo_registros = archivo_registros
        self.personas: List[Persona] = self._cargar_registros()
    
    def _cargar_registros(self) -> List[Persona]:
        """Cargar registros desde el archivo JSON"""
        try:
            with open(self.archivo_registros, 'r', encoding='utf-8') as json_file:
                datos = json.load(json_file)
                return [Persona(persona['nombre'], persona['pais']) for persona in datos]
        except FileNotFoundError:
            return []
    
    def guardar_registros(self) -> None:
        """Guardar registros en archivo JSON"""
        datos = [{'nombre': persona.nombre, 'pais': persona.pais} for persona in self.personas]
        with open(self.archivo_registros, 'w', encoding='utf-8') as json_file:
            json.dump(datos, json_file, ensure_ascii=False, indent=2)
    
    def agregar_persona(self, nombre: str, pais: str) -> bool:
        """Agregar una nueva persona si no existe duplicado"""
        if not nombre or not pais:
            return False
        
        nueva_persona = Persona(nombre, pais)
        
        # Verificar duplicado
        if self._existe_duplicado(nueva_persona.nombre):
            return False
        
        self.personas.append(nueva_persona)
        self.guardar_registros()
        return True
    
    def eliminar_persona(self, index: int) -> bool:
        """Eliminar persona por índice"""
        if 0 <= index < len(self.personas):
            del self.personas[index]
            self.guardar_registros()
            return True
        return False
    
    def modificar_persona(self, index: int, nombre: str, pais: str) -> bool:
        """Modificar persona existente"""
        if not nombre or not pais or not (0 <= index < len(self.personas)):
            return False
        
        nueva_persona = Persona(nombre, pais)
        
        # Verificar duplicado excluyendo el índice actual
        if self._existe_duplicado(nueva_persona.nombre, exclude_index=index):
            return False
        
        self.personas[index] = nueva_persona
        self.guardar_registros()
        return True
    
    def obtener_persona(self, index: int) -> Optional[Persona]:
        """Obtener persona por índice"""
        if 0 <= index < len(self.personas):
            return self.personas[index]
        return None
    
    def obtener_todas(self) -> List[Persona]:
        """Obtener todas las personas"""
        return self.personas
    
    def _existe_duplicado(self, nombre: str, exclude_index: Optional[int] = None) -> bool:
        """Verificar si existe duplicado por nombre"""
        for i, persona in enumerate(self.personas):
            if exclude_index is not None and i == exclude_index:
                continue
            if persona.nombre == nombre:
                return True
        return False
    
    def verificar_duplicado(self, nombre: str) -> bool:
        """Verificar duplicado para API"""
        return self._existe_duplicado(nombre.upper())
    
    def generar_csv(self) -> str:
        """Generar contenido CSV de las personas"""
        si = StringIO()
        writer = csv.writer(si)
        writer.writerow(['Nombre', 'País'])
        
        for persona in self.personas:
            writer.writerow([persona.nombre, persona.pais])
        
        output = '\ufeff' + si.getvalue()
        si.close()
        return output


class GestorPaises:
    """Clase responsable de gestionar los países (Single Responsibility)"""
    
    def __init__(self, url_api: str = 'https://restcountries.com/v2/all?fields=name'):
        self.url_api = url_api
    
    def obtener_paises(self) -> List[str]:
        """Obtener lista de países desde API"""
        try:
            response = requests.get(self.url_api, timeout=10)
            if response.status_code == 200:
                data = response.json()
                countries = [country['name'] for country in data]
                return sorted(countries)
            return []
        except Exception as e:
            print(f"Error al obtener países: {e}")
            return []


class AplicacionFlask:
    """Clase principal de la aplicación Flask (Single Responsibility)"""
    
    def __init__(self):
        self.app = Flask(__name__)
        self.gestor_personas = GestorPersonas()
        self.gestor_paises = GestorPaises()
        self._configurar_rutas()
    
    def _configurar_rutas(self) -> None:
        """Configurar todas las rutas de la aplicación"""
        
        @self.app.route('/')
        def index():
            countries = self.gestor_paises.obtener_paises()
            personas = self.gestor_personas.obtener_todas()
            return render_template('index.html', personas=personas, countries=countries)
        
        @self.app.route('/registrar', methods=['POST'])
        def registrar():
            nombre = request.form.get('nombre', '').strip()
            pais = request.form.get('pais', '').strip()
            
            if not nombre or not pais:
                return redirect('/?error=campos_vacios')
            
            if self.gestor_personas.agregar_persona(nombre, pais):
                return redirect('/?success=true')
            else:
                return redirect(f'/?error=duplicado&nombre={nombre}')
        
        @self.app.route('/eliminar/<int:index>', methods=['GET'])
        def eliminar(index):
            self.gestor_personas.eliminar_persona(index)
            return redirect('/?success=true')
        
        @self.app.route('/modificar/<int:index>', methods=['GET', 'POST'])
        def modificar(index):
            if request.method == 'GET':
                persona = self.gestor_personas.obtener_persona(index)
                if persona:
                    countries = self.gestor_paises.obtener_paises()
                    return render_template('modificar.html', index=index, persona=persona, countries=countries)
                return redirect('/')
            
            elif request.method == 'POST':
                nombre = request.form.get('nombre', '').strip()
                pais = request.form.get('pais', '').strip()
                
                if not nombre or not pais:
                    return redirect('/?error=campos_vacios')
                
                if self.gestor_personas.modificar_persona(index, nombre, pais):
                    return redirect('/?success=true')
                else:
                    return redirect(f'/?error=duplicado&nombre={nombre}')
            
            return redirect('/')
        
        @self.app.route('/personas_json')
        def cargar_personas_json():
            personas = self.gestor_personas.obtener_todas()
            return jsonify([{'nombre': p.nombre, 'pais': p.pais} for p in personas])
        
        @self.app.route('/verificar_duplicado/<nombre>')
        def verificar_duplicado_api(nombre):
            es_duplicado = self.gestor_personas.verificar_duplicado(nombre)
            return jsonify({
                'duplicado': es_duplicado,
                'nombre': nombre.upper()
            })
        
        @self.app.route('/descargar_csv')
        def descargar_csv():
            contenido_csv = self.gestor_personas.generar_csv()
            return Response(
                contenido_csv,
                mimetype='text/csv; charset=utf-8',
                headers={"Content-Disposition": "attachment;filename=personas.csv"}
            )
        
        @self.app.route('/descargar_csv_json')
        def descargar_csv_json():
            try:
                contenido_csv = self.gestor_personas.generar_csv()
                return jsonify({
                    'success': True,
                    'message': 'Archivo CSV generado correctamente',
                    'data': contenido_csv,
                    'filename': 'personas.csv'
                })
            except Exception as e:
                return jsonify({
                    'success': False,
                    'message': f'Error al generar CSV: {str(e)}'
                }), 500
    
    def ejecutar(self, debug: bool = True) -> None:
        """Ejecutar la aplicación Flask"""
        self.app.run(debug=debug)


# Crear instancia de la aplicación
aplicacion = AplicacionFlask()

if __name__ == '__main__':
    aplicacion.ejecutar()
