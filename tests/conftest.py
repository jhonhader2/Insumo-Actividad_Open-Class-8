# -*- coding: utf-8 -*-
"""
Configuración común para todas las pruebas del proyecto.
Este archivo contiene configuraciones, fixtures y utilidades compartidas.

Autor: Sistema de Pruebas Integradas
Fecha: 2025-07-06
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Agregar el directorio raíz al path para importar la aplicación
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pytest
from app import app, personas, guardar_registros_en_json


class TestConfig:
    """Configuración para las pruebas."""
    
    # Rutas de archivos de prueba
    TEST_DATA_DIR = project_root / 'tests' / 'data'
    TEST_REPORTS_DIR = project_root / 'reporte'
    TEST_LOG_FILE = project_root / 'registro_pruebas.txt'
    
    # Configuración de la aplicación para pruebas
    TESTING = True
    DEBUG = False
    
    @classmethod
    def setup_test_environment(cls):
        """Configura el entorno de pruebas."""
        # Crear directorios necesarios
        cls.TEST_DATA_DIR.mkdir(exist_ok=True)
        cls.TEST_REPORTS_DIR.mkdir(exist_ok=True)
        
        # Limpiar datos de prueba anteriores
        cls.cleanup_test_data()
    
    @classmethod
    def cleanup_test_data(cls):
        """Limpia los datos de prueba."""
        # Limpiar registros
        if personas:
            personas.clear()
            guardar_registros_en_json(personas)
        
        # Limpiar archivo de registro de pruebas
        if cls.TEST_LOG_FILE.exists():
            cls.TEST_LOG_FILE.unlink()


@pytest.fixture(scope='session')
def test_config():
    """Fixture que proporciona la configuración de pruebas."""
    config = TestConfig()
    config.setup_test_environment()
    yield config
    config.cleanup_test_data()


@pytest.fixture(scope='function')
def client():
    """Fixture que proporciona un cliente de prueba de Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            # Limpiar datos antes de cada prueba
            personas.clear()
            guardar_registros_en_json(personas)
            yield client
            # Limpiar datos después de cada prueba
            personas.clear()
            guardar_registros_en_json(personas)


@pytest.fixture(scope='function')
def sample_person():
    """Fixture que proporciona datos de persona de ejemplo."""
    return {
        'nombre': 'Juan Pérez',
        'pais': 'México'
    }


@pytest.fixture(scope='function')
def sample_persons():
    """Fixture que proporciona una lista de personas de ejemplo."""
    return [
        {'nombre': 'Ana García', 'pais': 'España'},
        {'nombre': 'Carlos López', 'pais': 'Colombia'},
        {'nombre': 'María Rodríguez', 'pais': 'Argentina'}
    ]


def pytest_configure(config):
    """Configuración que se ejecuta al inicio de pytest."""
    print("\n" + "="*60)
    print("🧪 INICIANDO SISTEMA DE PRUEBAS")
    print("="*60)


def pytest_unconfigure(config):
    """Configuración que se ejecuta al final de pytest."""
    print("\n" + "="*60)
    print("✅ PRUEBAS COMPLETADAS")
    print("="*60) 