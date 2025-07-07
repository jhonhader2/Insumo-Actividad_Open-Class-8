# 🎯 Configuración de SonarQube para Proyecto Python Flask

## 📋 Resumen
Este documento explica cómo configurar y usar SonarQube para analizar la calidad del código del proyecto **Insumo Actividad Open Class 8**.

## 🚀 Pasos de Configuración

### 1. Obtener Token de SonarQube

1. **Acceder a SonarQube**: Ve a `http://localhost:9000`
2. **Iniciar sesión**: Usa las credenciales de administrador
3. **Generar token**:
   - Ve a **My Account** → **Security**
   - En **Generate Tokens**, crea un nuevo token
   - Copia el token generado

### 2. Configurar el Archivo sonar-project.properties

1. **Editar el archivo**: Abre `sonar-project.properties`
2. **Reemplazar el token**: Cambia `TU_TOKEN_DE_SONAR_AQUI` por tu token real
3. **Verificar configuración**: Asegúrate de que `sonar.host.url` apunte a tu servidor

### 3. Instalar SonarScanner

```bash
# Opción 1: Descargar desde SonarQube
# Ve a http://localhost:9000/documentation/analysis/scan/sonarscanner/

# Opción 2: Usar Docker
docker run --rm \
  -e SONAR_HOST_URL="http://localhost:9000" \
  -e SONAR_LOGIN="TU_TOKEN" \
  -v "${PWD}:/usr/src" \
  sonarsource/sonar-scanner-cli

# Opción 3: Usar npm (si tienes Node.js)
npm install -g sonarqube-scanner
```

## 🔧 Ejecutar Análisis

### Método 1: SonarScanner CLI
```bash
# Desde la raíz del proyecto
sonar-scanner

# Con parámetros específicos
sonar-scanner \
  -Dsonar.projectKey=insumo_actividad_open_class_8 \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.token=TU_TOKEN
```

### Método 2: Script de Automatización
```bash
# Crear script run-sonar.bat (Windows)
@echo off
echo Iniciando análisis de SonarQube...
sonar-scanner
echo Análisis completado.
pause
```

### Método 3: Integración con Python
```python
# Crear script run_sonar_analysis.py
import subprocess
import os

def ejecutar_analisis_sonar():
    """Ejecutar análisis de SonarQube"""
    try:
        resultado = subprocess.run(
            ['sonar-scanner'],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        
        if resultado.returncode == 0:
            print("✅ Análisis de SonarQube completado exitosamente")
            print(resultado.stdout)
        else:
            print("❌ Error en el análisis de SonarQube")
            print(resultado.stderr)
            
    except FileNotFoundError:
        print("❌ SonarScanner no encontrado. Instálalo primero.")

if __name__ == "__main__":
    ejecutar_analisis_sonar()
```

## 📊 Configuración de Cobertura de Código

### 1. Instalar Dependencias
```bash
pip install pytest-cov
```

### 2. Ejecutar Tests con Cobertura
```bash
# Generar reporte de cobertura
pytest --cov=. --cov-report=xml --cov-report=html

# O usar el script existente
python ejecutar_pruebas.py
```

### 3. Configurar SonarQube para Cobertura
El archivo `sonar-project.properties` ya está configurado para:
- `sonar.python.coverage.reportPaths=coverage.xml`
- `sonar.python.xunit.reportPath=test-results.xml`

## 🎯 Métricas de Calidad Configuradas

### Complejidad Ciclomática
- **Función**: Máximo 10
- **Clase**: Máximo 20

### Duplicación de Código
- **Líneas mínimas**: 5
- **Tokens mínimos**: 70

### Líneas de Código
- **Umbral**: 1000 líneas por archivo

## 🔍 Exclusiones Configuradas

### Archivos Excluidos del Análisis Principal
- `__pycache__/` - Archivos compilados de Python
- `*.pyc`, `*.pyo`, `*.pyd` - Bytecode de Python
- `.git/` - Control de versiones
- `venv/`, `env/` - Entornos virtuales
- `static/js/*.map`, `static/css/*.map` - Source maps
- `reporte/` - Directorio de reportes
- `registro_pruebas.txt` - Archivo de logs
- `ejecutar_pruebas.py` - Script de ejecución

### Archivos de Test Excluidos
- `tests/` - Directorio completo de tests
- `test_*.py` - Archivos de test
- `conftest.py` - Configuración de pytest

## 🛠️ Solución de Problemas

### Error: "SonarScanner no encontrado"
```bash
# Verificar instalación
sonar-scanner --version

# Si no está instalado, descargar desde:
# https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
```

### Error: "Token inválido"
1. Verificar que el token esté correctamente copiado
2. Asegurarse de que no haya espacios extra
3. Regenerar el token si es necesario

### Error: "No se puede conectar al servidor"
1. Verificar que SonarQube esté ejecutándose
2. Comprobar la URL en `sonar.host.url`
3. Verificar firewall y puertos

### Error: "Archivo no encontrado"
1. Verificar que estés en el directorio correcto
2. Comprobar que `sonar-project.properties` existe
3. Verificar permisos de archivos

## 📈 Interpretación de Resultados

### Calidad del Código
- **A**: Excelente (0-5% de deuda técnica)
- **B**: Buena (6-10% de deuda técnica)
- **C**: Regular (11-20% de deuda técnica)
- **D**: Mala (21-50% de deuda técnica)
- **E**: Muy mala (>50% de deuda técnica)

### Cobertura de Código
- **80%+**: Excelente
- **60-79%**: Buena
- **40-59%**: Regular
- **<40%**: Necesita mejora

### Duplicación
- **<3%**: Excelente
- **3-5%**: Buena
- **5-10%**: Regular
- **>10%**: Necesita refactorización

## 🔄 Integración Continua

### GitHub Actions
```yaml
# .github/workflows/sonar.yml
name: SonarQube Analysis

on: [push, pull_request]

jobs:
  sonar:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: SonarQube Scan
      uses: sonarqube-quality-gate-action@master
      env:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
```

### GitLab CI
```yaml
# .gitlab-ci.yml
sonar:
  stage: test
  image: sonarqube-scanner
  script:
    - sonar-scanner
  only:
    - merge_requests
    - main
```

## 📚 Recursos Adicionales

- [Documentación oficial de SonarQube](https://docs.sonarqube.org/)
- [Reglas de Python en SonarQube](https://rules.sonarsource.com/python)
- [Mejores prácticas para Python](https://docs.sonarqube.org/latest/analysis/languages/python/)

## 🎉 ¡Listo!

Con esta configuración, tu proyecto Python Flask estará completamente integrado con SonarQube para análisis continuo de calidad de código, siguiendo los principios de **POO**, **DRY**, **KISS** y **Single Responsibility**. 