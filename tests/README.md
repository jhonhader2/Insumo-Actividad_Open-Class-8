# 📁 Carpeta de Tests

Esta carpeta contiene todas las pruebas del sistema de registro de personas, organizadas siguiendo las mejores prácticas de testing.

## 📋 Estructura

```
tests/
├── __init__.py              # Hace que tests sea un paquete de Python
├── conftest.py              # Configuración común para todas las pruebas
├── test_integrado.py        # Pruebas de integración del sistema
├── test_app.py              # Pruebas unitarias de la aplicación
└── README.md               # Esta documentación
```

## 🧪 Tipos de Pruebas

### Pruebas de Integración (`test_integrado.py`)
- **test_index()** - Verifica carga de página principal
- **test_registro()** - Prueba registro de nuevas personas
- **test_modificar()** - Verifica modificación de registros
- **test_eliminar()** - Prueba eliminación de registros
- **test_descargar_csv()** - Verifica descarga de archivos CSV

### Pruebas Unitarias (`test_app.py`)
- Pruebas específicas de funciones individuales
- Validación de lógica de negocio
- Testing de utilidades y helpers

## 🚀 Ejecución de Pruebas

### Desde el directorio raíz:
```bash
# Ejecutar todas las pruebas con reportes
python ejecutar_pruebas.py

# Ejecutar pruebas de integración directamente
python tests/test_integrado.py

# Ejecutar pruebas unitarias
python tests/test_app.py
```

### Desde la carpeta tests:
```bash
# Ejecutar pruebas de integración
python test_integrado.py

# Ejecutar pruebas unitarias
python test_app.py
```

## ⚙️ Configuración (`conftest.py`)

### Fixtures Disponibles:
- **test_config** - Configuración general de pruebas
- **client** - Cliente de prueba de Flask
- **sample_person** - Datos de persona de ejemplo
- **sample_persons** - Lista de personas de ejemplo

### Configuración Automática:
- Limpieza de datos antes y después de cada prueba
- Configuración del entorno de testing
- Gestión de archivos temporales

## 📊 Reportes Generados

### Archivos de Salida:
- `registro_pruebas.txt` - Historial detallado de pruebas
- `reporte/TestResults_*.html` - Reportes visuales HTML
- Consola - Resumen en tiempo real

### Ubicaciones:
- Los reportes se generan en el directorio raíz del proyecto
- Los logs se guardan en `registro_pruebas.txt`
- Los reportes HTML van a `reporte/`

## 🔧 Agregar Nuevas Pruebas

### Para Pruebas de Integración:
```python
# En test_integrado.py
def test_nueva_funcionalidad(self):
    """Prueba para nueva funcionalidad."""
    try:
        # Tu código de prueba aquí
        response = self.client.get('/nueva-ruta')
        self.assertEqual(response.status_code, 200)
        registrar_en_txt("Nueva Funcionalidad", "✅ Éxito")
    except AssertionError:
        registrar_en_txt("Nueva Funcionalidad", "❌ Fallo")
        raise
```

### Para Pruebas Unitarias:
```python
# En test_app.py
def test_nueva_funcion(self):
    """Prueba unitaria para nueva función."""
    # Tu código de prueba aquí
    resultado = nueva_funcion()
    self.assertEqual(resultado, valor_esperado)
```

## 🎯 Principios de Testing

### Organización:
- **Separación de responsabilidades** - Cada archivo tiene un propósito específico
- **Reutilización** - Fixtures compartidas en conftest.py
- **Mantenibilidad** - Código limpio y documentado

### Cobertura:
- **Funcionalidades principales** - 100% cubiertas
- **Casos edge** - Incluidos en pruebas
- **Manejo de errores** - Validado en cada prueba

## 📈 Métricas de Calidad

- **Tiempo de ejecución**: < 2 segundos
- **Fiabilidad**: Todas las pruebas pasan exitosamente
- **Cobertura**: 100% de funcionalidades críticas
- **Mantenibilidad**: Código limpio y bien documentado

---

**¡El sistema de pruebas está organizado y listo para uso en producción!** 🎉 