# 📋 Sistema de Registro de Personas

Una aplicación web moderna para gestionar registros de personas con API JSON, construida con Flask y JavaScript.

## 🚀 Características

- **Registro de Personas**: Agregar nuevas personas con nombre y país
- **Gestión CRUD**: Crear, Leer, Actualizar y Eliminar registros
- **Validación en Tiempo Real**: Verificación de duplicados y validaciones
- **Interfaz Moderna**: Diseño responsive con animaciones suaves
- **Descarga de Datos**: Exportar registros en formato CSV
- **API REST**: Endpoints JSON para integración con otros sistemas
- **Responsive Design**: Optimizado para móviles y tablets

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.8+**
- **Flask**: Framework web
- **Requests**: Cliente HTTP para APIs externas
- **CSV**: Manejo de archivos CSV

### Frontend
- **HTML5 & CSS3**: Estructura y estilos
- **JavaScript (ES6+)**: Lógica del cliente
- **SweetAlert2**: Alertas y confirmaciones
- **Select2**: Selectores avanzados
- **Font Awesome**: Iconografía
- **Google Fonts**: Tipografías

### APIs Externas
- **REST Countries API**: Lista de países del mundo

## 📦 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd Insumo-Actividad_Open-Class-8
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

4. **Abrir en el navegador**
   ```
   http://localhost:5000
   ```

## 🏗️ Estructura del Proyecto

```
Insumo-Actividad_Open-Class-8/
├── app.py                          # Aplicación principal Flask
├── requirements.txt                 # Dependencias de Python
├── registros.json                  # Base de datos JSON
├── templates/
│   ├── index.html                  # Página principal
│   └── modificar.html             # Página de modificación
├── static/
│   ├── style.css                   # Estilos CSS
│   └── js/
│       ├── app.js                  # Lógica principal
│       ├── crud-operations.js      # Operaciones CRUD
│       ├── form-validations.js     # Validaciones
│       ├── select2-config.js       # Configuración Select2
│       └── sweetalert-config.js    # Configuración SweetAlert2
├── tests/                          # Pruebas unitarias
├── reporte/                        # Reportes generados
└── README.md                       # Este archivo
```

## 🎯 Funcionalidades Principales

### 1. Registro de Personas
- Formulario con validación en tiempo real
- Verificación automática de duplicados
- Selección de países desde API externa
- Formato automático de nombres (mayúsculas)

### 2. Gestión de Registros
- **Ver**: Lista todas las personas registradas
- **Editar**: Modificar información existente
- **Eliminar**: Borrar registros con confirmación
- **Buscar**: Filtrado por nombre y país

### 3. Exportación de Datos
- Descarga en formato CSV
- Compatible con Excel y Google Sheets
- Codificación UTF-8 para caracteres especiales

### 4. API REST
- `GET /personas_json`: Obtener todos los registros
- `POST /registrar`: Crear nuevo registro
- `POST /modificar/<index>`: Actualizar registro
- `GET /eliminar/<index>`: Eliminar registro
- `GET /verificar_duplicado/<nombre>`: Verificar duplicados

## 🎨 Diseño y UX

### Características de Diseño
- **Responsive Design**: Adaptable a todos los dispositivos
- **Animaciones Suaves**: Transiciones y efectos visuales
- **Paleta de Colores**: Azul profesional con acentos verdes
- **Tipografía**: Inter de Google Fonts
- **Iconografía**: Font Awesome para mejor UX

### Experiencia de Usuario
- **Feedback Visual**: Confirmaciones y mensajes claros
- **Validación en Tiempo Real**: Errores inmediatos
- **Loading States**: Indicadores de carga
- **Accesibilidad**: Tooltips y navegación por teclado

## 🔧 Configuración

### Variables de Entorno
```bash
# Configuración del servidor
FLASK_ENV=development
FLASK_DEBUG=True
```

### Personalización
- **Colores**: Modificar variables CSS en `static/style.css`
- **Animaciones**: Ajustar timing en archivos CSS
- **Validaciones**: Editar reglas en `static/js/form-validations.js`

## 🧪 Pruebas

### Ejecutar Pruebas
```bash
python ejecutar_pruebas.py
```

### Tipos de Pruebas
- **Pruebas Unitarias**: Funciones individuales
- **Pruebas de Integración**: Flujos completos
- **Pruebas de UI**: Interfaz de usuario

## 📊 API Endpoints

### Obtener Datos
```http
GET /personas_json
Content-Type: application/json
```

### Crear Registro
```http
POST /registrar
Content-Type: application/x-www-form-urlencoded

nombre=Juan Pérez&pais=México
```

### Verificar Duplicado
```http
GET /verificar_duplicado/JUAN PÉREZ
Content-Type: application/json
```

### Descargar CSV
```http
GET /descargar_csv
Content-Type: text/csv
```

## 🚀 Despliegue

### Desarrollo Local
```bash
python app.py
```

### Producción (Recomendado)
```bash
# Usar Gunicorn para producción
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Opcional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contribución

### Guías de Contribución
1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

### Estándares de Código
- **Python**: PEP 8
- **JavaScript**: ESLint configurado
- **CSS**: BEM methodology
- **HTML**: Semantic markup

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Desarrollador**: [Tu Nombre]
- **Proyecto**: Sistema de Registro de Personas
- **Versión**: 1.0.0

## 🙏 Agradecimientos

- **REST Countries API**: Para la lista de países
- **SweetAlert2**: Para las alertas modernas
- **Select2**: Para los selectores avanzados
- **Font Awesome**: Para los iconos
- **Google Fonts**: Para las tipografías

## 📞 Soporte

Si tienes preguntas o problemas:

1. **Issues**: Crear un issue en GitHub
2. **Documentación**: Revisar este README
3. **Código**: Comentar en el código fuente

---

**¡Gracias por usar nuestro Sistema de Registro de Personas!** 🎉 