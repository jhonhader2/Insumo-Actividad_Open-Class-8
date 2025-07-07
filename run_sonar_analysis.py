#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Automatización para Análisis de SonarQube
===================================================

Este script automatiza la ejecución del análisis de SonarQube para el proyecto
Python Flask, siguiendo los principios de POO, DRY, KISS y Single Responsibility.

Autor: Sistema de Análisis de Calidad
Versión: 1.0.0
"""

import subprocess
import os
import sys
import json
import time
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ConfiguracionSonar:
    """Clase para manejar la configuración de SonarQube (Single Responsibility)"""
    
    archivo_config: str = 'sonar-project.properties'
    url_sonar: str = 'http://localhost:9000'
    timeout: int = 300  # 5 minutos
    
    def verificar_archivo_config(self) -> bool:
        """Verificar que existe el archivo de configuración"""
        return Path(self.archivo_config).exists()
    
    def leer_configuracion(self) -> Dict[str, str]:
        """Leer configuración del archivo sonar-project.properties"""
        config = {}
        try:
            with open(self.archivo_config, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea and not linea.startswith('#') and '=' in linea:
                        clave, valor = linea.split('=', 1)
                        config[clave.strip()] = valor.strip()
            return config
        except Exception as e:
            print(f"❌ Error al leer configuración: {e}")
            return {}


class GestorEjecucion:
    """Clase para gestionar la ejecución de comandos (Single Responsibility)"""
    
    def __init__(self, timeout: int = 300):
        self.timeout = timeout
    
    def ejecutar_comando(self, comando: List[str], directorio: str = None) -> Tuple[int, str, str]:
        """Ejecutar comando y retornar código, stdout y stderr"""
        try:
            resultado = subprocess.run(
                comando,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=directorio
            )
            return resultado.returncode, resultado.stdout, resultado.stderr
        except subprocess.TimeoutExpired:
            return -1, "", f"Comando excedió el timeout de {self.timeout} segundos"
        except FileNotFoundError:
            return -1, "", "Comando no encontrado"
        except Exception as e:
            return -1, "", f"Error inesperado: {e}"
    
    def verificar_sonar_scanner(self) -> bool:
        """Verificar si SonarScanner está instalado"""
        codigo, _, stderr = self.ejecutar_comando(['sonar-scanner', '--version'])
        return codigo == 0


class GestorReportes:
    """Clase para gestionar reportes y logs (Single Responsibility)"""
    
    def __init__(self, directorio_logs: str = 'logs'):
        self.directorio_logs = directorio_logs
        self._crear_directorio_logs()
    
    def _crear_directorio_logs(self) -> None:
        """Crear directorio de logs si no existe"""
        Path(self.directorio_logs).mkdir(exist_ok=True)
    
    def guardar_log(self, contenido: str, nombre_archivo: str) -> None:
        """Guardar log en archivo"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        nombre_completo = f"{self.directorio_logs}/{timestamp}_{nombre_archivo}"
        
        try:
            with open(nombre_completo, 'w', encoding='utf-8') as f:
                f.write(contenido)
            print(f"📄 Log guardado: {nombre_completo}")
        except Exception as e:
            print(f"❌ Error al guardar log: {e}")
    
    def generar_reporte_resumen(self, resultado: Dict) -> str:
        """Generar reporte resumen del análisis"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        reporte = f"""
=== REPORTE DE ANÁLISIS SONARQUBE ===
Fecha y Hora: {timestamp}
Estado: {'✅ EXITOSO' if resultado['exitoso'] else '❌ FALLIDO'}
Duración: {resultado['duracion']:.2f} segundos

Detalles:
- Código de salida: {resultado['codigo_salida']}
- Configuración válida: {'✅' if resultado['config_valida'] else '❌'}
- SonarScanner disponible: {'✅' if resultado['scanner_disponible'] else '❌'}

Salida del comando:
{resultado['salida']}

Errores (si los hay):
{resultado['errores']}
"""
        return reporte


class AnalizadorSonarQube:
    """Clase principal para el análisis de SonarQube (Single Responsibility)"""
    
    def __init__(self):
        self.config = ConfiguracionSonar()
        self.ejecutor = GestorEjecucion()
        self.reportes = GestorReportes()
    
    def verificar_prerequisitos(self) -> Dict[str, bool]:
        """Verificar todos los prerequisitos para el análisis"""
        return {
            'config_valida': self.config.verificar_archivo_config(),
            'scanner_disponible': self.ejecutor.verificar_sonar_scanner(),
            'directorio_valido': self._verificar_directorio_actual()
        }
    
    def _verificar_directorio_actual(self) -> bool:
        """Verificar que estamos en el directorio correcto del proyecto"""
        archivos_esperados = ['app.py', 'requirements.txt', 'sonar-project.properties']
        return all(Path(archivo).exists() for archivo in archivos_esperados)
    
    def ejecutar_analisis(self) -> Dict:
        """Ejecutar análisis completo de SonarQube"""
        tiempo_inicio = time.time()
        
        # Verificar prerequisitos
        prerequisitos = self.verificar_prerequisitos()
        
        if not all(prerequisitos.values()):
            return self._generar_resultado_fallido(prerequisitos, tiempo_inicio)
        
        # Ejecutar SonarScanner
        codigo, stdout, stderr = self.ejecutor.ejecutar_comando(['sonar-scanner'])
        
        tiempo_fin = time.time()
        duracion = tiempo_fin - tiempo_inicio
        
        # Generar resultado
        resultado = {
            'exitoso': codigo == 0,
            'codigo_salida': codigo,
            'salida': stdout,
            'errores': stderr,
            'duracion': duracion,
            'prerequisitos': prerequisitos,
            'config_valida': prerequisitos['config_valida'],
            'scanner_disponible': prerequisitos['scanner_disponible']
        }
        
        # Guardar logs
        self._guardar_logs_analisis(resultado)
        
        return resultado
    
    def _generar_resultado_fallido(self, prerequisitos: Dict[str, bool], tiempo_inicio: float) -> Dict:
        """Generar resultado cuando fallan los prerequisitos"""
        tiempo_fin = time.time()
        duracion = tiempo_fin - tiempo_inicio
        
        return {
            'exitoso': False,
            'codigo_salida': -1,
            'salida': '',
            'errores': self._generar_mensaje_errores_prerequisitos(prerequisitos),
            'duracion': duracion,
            'prerequisitos': prerequisitos,
            'config_valida': prerequisitos['config_valida'],
            'scanner_disponible': prerequisitos['scanner_disponible']
        }
    
    def _generar_mensaje_errores_prerequisitos(self, prerequisitos: Dict[str, bool]) -> str:
        """Generar mensaje de errores de prerequisitos"""
        errores = []
        
        if not prerequisitos['config_valida']:
            errores.append("- Archivo sonar-project.properties no encontrado")
        
        if not prerequisitos['scanner_disponible']:
            errores.append("- SonarScanner no está instalado o no está en el PATH")
        
        if not prerequisitos['directorio_valido']:
            errores.append("- No estás en el directorio correcto del proyecto")
        
        return "\n".join(errores) if errores else "Error desconocido"
    
    def _guardar_logs_analisis(self, resultado: Dict) -> None:
        """Guardar logs del análisis"""
        # Guardar salida completa
        contenido_completo = f"Salida:\n{resultado['salida']}\n\nErrores:\n{resultado['errores']}"
        self.reportes.guardar_log(contenido_completo, 'sonar_analisis_completo.log')
        
        # Guardar reporte resumen
        reporte_resumen = self.reportes.generar_reporte_resumen(resultado)
        self.reportes.guardar_log(reporte_resumen, 'sonar_reporte_resumen.log')


def mostrar_ayuda() -> None:
    """Mostrar ayuda del script"""
    ayuda = """
🎯 Script de Análisis de SonarQube para Proyecto Python Flask

Uso:
    python run_sonar_analysis.py [opciones]

Opciones:
    --help, -h          Mostrar esta ayuda
    --verbose, -v       Modo verboso
    --check-only        Solo verificar prerequisitos
    --no-logs           No guardar logs

Ejemplos:
    python run_sonar_analysis.py
    python run_sonar_analysis.py --verbose
    python run_sonar_analysis.py --check-only

Requisitos:
    1. Archivo sonar-project.properties configurado
    2. SonarScanner instalado y en el PATH
    3. SonarQube ejecutándose en http://localhost:9000
    4. Token válido configurado en sonar-project.properties
"""
    print(ayuda)


def main():
    """Función principal del script"""
    # Procesar argumentos de línea de comandos
    argumentos = sys.argv[1:]
    
    if '--help' in argumentos or '-h' in argumentos:
        mostrar_ayuda()
        return
    
    modo_verboso = '--verbose' in argumentos or '-v' in argumentos
    solo_verificar = '--check-only' in argumentos
    no_logs = '--no-logs' in argumentos
    
    print("🚀 Iniciando Análisis de SonarQube...")
    print("=" * 50)
    
    # Crear analizador
    analizador = AnalizadorSonarQube()
    
    if solo_verificar:
        # Solo verificar prerequisitos
        prerequisitos = analizador.verificar_prerequisitos()
        print("\n📋 Verificación de Prerequisitos:")
        print("-" * 30)
        
        for prerequisito, estado in prerequisitos.items():
            icono = "✅" if estado else "❌"
            print(f"{icono} {prerequisito}: {'Válido' if estado else 'Inválido'}")
        
        if all(prerequisitos.values()):
            print("\n🎉 Todos los prerequisitos están cumplidos. Puedes ejecutar el análisis.")
        else:
            print("\n⚠️  Algunos prerequisitos no están cumplidos. Revisa la configuración.")
        
        return
    
    # Ejecutar análisis completo
    resultado = analizador.ejecutar_analisis()
    
    # Mostrar resultados
    print(f"\n📊 Resultados del Análisis:")
    print("-" * 30)
    
    if resultado['exitoso']:
        print("✅ Análisis completado exitosamente")
        print(f"⏱️  Duración: {resultado['duracion']:.2f} segundos")
        
        if modo_verboso:
            print(f"\n📄 Salida del comando:")
            print(resultado['salida'])
    else:
        print("❌ Análisis falló")
        print(f"⏱️  Duración: {resultado['duracion']:.2f} segundos")
        print(f"🔍 Código de salida: {resultado['codigo_salida']}")
        
        if resultado['errores']:
            print(f"\n❌ Errores:")
            print(resultado['errores'])
    
    # Mostrar información adicional
    if modo_verboso:
        print(f"\n🔧 Información de Configuración:")
        print("-" * 30)
        for prerequisito, estado in resultado['prerequisitos'].items():
            icono = "✅" if estado else "❌"
            print(f"{icono} {prerequisito}: {'Válido' if estado else 'Inválido'}")
    
    print("\n" + "=" * 50)
    
    if resultado['exitoso']:
        print("🎉 ¡Análisis de SonarQube completado!")
        print("📈 Revisa los resultados en: http://localhost:9000")
    else:
        print("⚠️  Revisa los errores y vuelve a intentar")
        print("📚 Consulta SONARQUBE_SETUP.md para más información")


if __name__ == "__main__":
    main() 