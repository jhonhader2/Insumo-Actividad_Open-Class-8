@echo off
REM =============================================================================
REM Script de Análisis de SonarQube para Proyecto Python Flask
REM =============================================================================
REM Principios aplicados: POO, DRY, KISS, Single Responsibility
REM =============================================================================

setlocal enabledelayedexpansion

REM Configuración de colores
set "VERDE=[92m"
set "ROJO=[91m"
set "AMARILLO=[93m"
set "AZUL=[94m"
set "RESET=[0m"

echo %AZUL%🎯 Script de Análisis de SonarQube para Proyecto Python Flask%RESET%
echo %AZUL%==============================================================================%RESET%
echo.

REM Verificar si estamos en el directorio correcto
if not exist "app.py" (
    echo %ROJO%❌ Error: No se encontró app.py%RESET%
    echo %AMARILLO%💡 Asegúrate de estar en el directorio raíz del proyecto%RESET%
    pause
    exit /b 1
)

if not exist "sonar-project.properties" (
    echo %ROJO%❌ Error: No se encontró sonar-project.properties%RESET%
    echo %AMARILLO%💡 Verifica que el archivo de configuración existe%RESET%
    pause
    exit /b 1
)

REM Verificar si Python está disponible
python --version >nul 2>&1
if errorlevel 1 (
    echo %ROJO%❌ Error: Python no está instalado o no está en el PATH%RESET%
    echo %AMARILLO%💡 Instala Python y agrégalo al PATH del sistema%RESET%
    pause
    exit /b 1
)

echo %VERDE%✅ Verificaciones básicas completadas%RESET%
echo.

REM Mostrar menú de opciones
:menu
echo %AZUL%Selecciona una opción:%RESET%
echo.
echo %VERDE%1.%RESET% Ejecutar análisis completo de SonarQube
echo %VERDE%2.%RESET% Verificar prerequisitos únicamente
echo %VERDE%3.%RESET% Ejecutar análisis con modo verboso
echo %VERDE%4.%RESET% Mostrar ayuda
echo %VERDE%5.%RESET% Salir
echo.
set /p opcion="Ingresa tu opción (1-5): "

if "%opcion%"=="1" goto ejecutar_analisis
if "%opcion%"=="2" goto verificar_prerequisitos
if "%opcion%"=="3" goto ejecutar_verboso
if "%opcion%"=="4" goto mostrar_ayuda
if "%opcion%"=="5" goto salir
echo %ROJO%❌ Opción inválida. Intenta de nuevo.%RESET%
echo.
goto menu

:ejecutar_analisis
echo.
echo %AZUL%🚀 Ejecutando análisis completo de SonarQube...%RESET%
echo %AZUL%==============================================================================%RESET%
python run_sonar_analysis.py
echo.
echo %AZUL%==============================================================================%RESET%
echo %VERDE%✅ Análisis completado%RESET%
echo.
pause
goto menu

:verificar_prerequisitos
echo.
echo %AZUL%📋 Verificando prerequisitos...%RESET%
echo %AZUL%==============================================================================%RESET%
python run_sonar_analysis.py --check-only
echo.
echo %AZUL%==============================================================================%RESET%
echo %VERDE%✅ Verificación completada%RESET%
echo.
pause
goto menu

:ejecutar_verboso
echo.
echo %AZUL%🚀 Ejecutando análisis con modo verboso...%RESET%
echo %AZUL%==============================================================================%RESET%
python run_sonar_analysis.py --verbose
echo.
echo %AZUL%==============================================================================%RESET%
echo %VERDE%✅ Análisis completado%RESET%
echo.
pause
goto menu

:mostrar_ayuda
echo.
echo %AZUL%📚 AYUDA - Configuración de SonarQube%RESET%
echo %AZUL%==============================================================================%RESET%
echo.
echo %AMARILLO%📋 Requisitos Previos:%RESET%
echo   1. SonarQube ejecutándose en http://localhost:9000
echo   2. Token de acceso configurado en sonar-project.properties
echo   3. SonarScanner instalado y en el PATH
echo   4. Python y dependencias instaladas
echo.
echo %AMARILLO%🔧 Configuración:%RESET%
echo   1. Edita sonar-project.properties
echo   2. Reemplaza TU_TOKEN_DE_SONAR_AQUI con tu token real
echo   3. Verifica que sonar.host.url apunte a tu servidor
echo.
echo %AMARILLO%📊 Resultados:%RESET%
echo   - Los resultados se mostrarán en http://localhost:9000
echo   - Los logs se guardarán en el directorio logs/
echo   - Consulta SONARQUBE_SETUP.md para más detalles
echo.
echo %AMARILLO%🛠️ Solución de Problemas:%RESET%
echo   - Si SonarScanner no se encuentra, descárgalo desde:
echo     https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/
echo   - Si hay errores de conexión, verifica que SonarQube esté ejecutándose
echo   - Si el token es inválido, regenera uno en SonarQube
echo.
echo %AZUL%==============================================================================%RESET%
echo.
pause
goto menu

:salir
echo.
echo %VERDE%👋 ¡Hasta luego!%RESET%
echo %AZUL%Gracias por usar el script de análisis de SonarQube%RESET%
echo.
exit /b 0

REM =============================================================================
REM Funciones auxiliares
REM =============================================================================

:mostrar_error
echo %ROJO%❌ Error: %1%RESET%
echo %AMARILLO%💡 %2%RESET%
echo.
pause
goto menu

:mostrar_exito
echo %VERDE%✅ %1%RESET%
echo.
pause
goto menu

REM =============================================================================
REM Fin del script
REM ============================================================================= 