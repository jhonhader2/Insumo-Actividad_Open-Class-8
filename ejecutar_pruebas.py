#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para ejecutar pruebas integradas del sistema de registro de personas.
Este script implementa los principios SOLID y DRY para mantener el código limpio y mantenible.

Autor: Sistema de Pruebas Integradas
Fecha: 2025-07-06
"""

import os
import sys
import subprocess
from datetime import datetime


class EjecutorPruebas:
    """
    Clase responsable de ejecutar las pruebas del sistema.
    Implementa el principio de Responsabilidad Única (SRP).
    """
    
    def __init__(self):
        """Inicializa el ejecutor de pruebas."""
        self.archivo_pruebas = 'tests/test_integrado.py'
        self.archivo_requirements = 'requirements.txt'
        self.directorio_reporte = 'reporte'
        self.directorio_tests = 'tests'
    
    def verificar_dependencias(self):
        """
        Verifica que todas las dependencias estén instaladas.
        Retorna True si todo está correcto, False en caso contrario.
        """
        try:
            print("🔍 Verificando dependencias...")
            
            # Verificar que existe el archivo de pruebas
            if not os.path.exists(self.archivo_pruebas):
                print(f"❌ Error: No se encuentra el archivo {self.archivo_pruebas}")
                return False
            
            # Verificar que existe el archivo de requirements
            if not os.path.exists(self.archivo_requirements):
                print(f"❌ Error: No se encuentra el archivo {self.archivo_requirements}")
                return False
            
            # Verificar que existe la aplicación principal
            if not os.path.exists('app.py'):
                print("❌ Error: No se encuentra el archivo app.py")
                return False
            
            # Verificar que existe el directorio de tests
            if not os.path.exists(self.directorio_tests):
                print(f"❌ Error: No se encuentra el directorio {self.directorio_tests}")
                return False
            
            print("✅ Todas las dependencias están disponibles")
            return True
            
        except Exception as e:
            print(f"❌ Error al verificar dependencias: {e}")
            return False
    
    def instalar_dependencias(self):
        """
        Instala las dependencias necesarias para las pruebas.
        """
        try:
            print("📦 Instalando dependencias...")
            
            # Usar la versión específica de Python que tiene pip
            python_cmd = r'C:\Python311\python.exe'
            
            resultado = subprocess.run(
                [python_cmd, '-m', 'pip', 'install', '-r', self.archivo_requirements],
                capture_output=True,
                text=True,
                check=True
            )
            print("✅ Dependencias instaladas correctamente")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al instalar dependencias: {e}")
            print(f"Salida de error: {e.stderr}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False
    
    def ejecutar_pruebas(self):
        """
        Ejecuta las pruebas integradas del sistema.
        """
        try:
            print("🧪 Ejecutando pruebas integradas...")
            print("=" * 50)
            
            # Crear directorio de reportes si no existe
            os.makedirs(self.directorio_reporte, exist_ok=True)
            
            # Usar la versión específica de Python que tiene pip
            # python_cmd = r'C:\Python311\python.exe'
            python_cmd = r'C:\laragon\bin\python\python-3.13.5\python.exe'
            
            # Ejecutar las pruebas
            resultado = subprocess.run(
                [python_cmd, self.archivo_pruebas],
                capture_output=True,
                text=True,
                check=True
            )
            
            print("✅ Pruebas ejecutadas correctamente")
            print("📊 Resultados:")
            print(resultado.stdout)
            
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar pruebas: {e}")
            print(f"Salida de error: {e.stderr}")
            return False
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return False
    
    def mostrar_resumen(self):
        """
        Muestra un resumen de los archivos generados.
        """
        print("\n📋 RESUMEN DE EJECUCIÓN")
        print("=" * 50)
        
        # Verificar archivo de registro
        if os.path.exists('registro_pruebas.txt'):
            print("✅ Archivo de registro: registro_pruebas.txt")
        else:
            print("❌ No se generó el archivo de registro")
        
        # Verificar reportes HTML
        if os.path.exists(self.directorio_reporte):
            archivos_html = [f for f in os.listdir(self.directorio_reporte) if f.endswith('.html')]
            if archivos_html:
                print(f"✅ Reportes HTML generados: {len(archivos_html)} archivos")
                for archivo in sorted(archivos_html, reverse=True)[:3]:  # Mostrar los 3 más recientes
                    print(f"   📄 {archivo}")
            else:
                print("❌ No se generaron reportes HTML")
        
        # Verificar archivo JSON de registros
        if os.path.exists('registros.json'):
            print("✅ Archivo de datos: registros.json")
        else:
            print("❌ No se encuentra el archivo de datos")
        
        # Verificar estructura de tests
        print(f"✅ Directorio de tests: {self.directorio_tests}/")
        if os.path.exists(f"{self.directorio_tests}/__init__.py"):
            print("✅ Paquete de tests configurado correctamente")
        if os.path.exists(f"{self.directorio_tests}/conftest.py"):
            print("✅ Configuración de tests disponible")
    
    def ejecutar_todo(self):
        """
        Ejecuta todo el proceso de pruebas de manera ordenada.
        """
        print("🚀 INICIANDO SISTEMA DE PRUEBAS INTEGRADAS")
        print("=" * 50)
        print(f"⏰ Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Paso 1: Verificar dependencias
        if not self.verificar_dependencias():
            print("❌ Fallo en la verificación de dependencias")
            return False
        
        # Paso 2: Instalar dependencias
        if not self.instalar_dependencias():
            print("❌ Fallo en la instalación de dependencias")
            return False
        
        # Paso 3: Ejecutar pruebas
        if not self.ejecutar_pruebas():
            print("❌ Fallo en la ejecución de pruebas")
            return False
        
        # Paso 4: Mostrar resumen
        self.mostrar_resumen()
        
        print("\n🎉 ¡Proceso completado exitosamente!")
        return True


def main():
    """
    Función principal que ejecuta el sistema de pruebas.
    """
    ejecutor = EjecutorPruebas()
    return ejecutor.ejecutar_todo()


if __name__ == '__main__':
    """
    Punto de entrada principal del script.
    """
    try:
        exito = main()
        sys.exit(0 if exito else 1)
    except KeyboardInterrupt:
        print("\n⚠️ Proceso interrumpido por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1) 