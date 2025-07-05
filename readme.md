# App Registro de Personas API JSON

## Descripción
Aplicación web desarrollada en Flask para el registro de personas con integración de API de países y funcionalidades CRUD completas.

## Características Implementadas

### 🎨 **SweetAlert2 Integration**
- **Alertas Modernas**: Implementación completa de SweetAlert2 para una experiencia de usuario superior
- **Confirmaciones Interactivas**: Diálogos de confirmación antes de realizar operaciones críticas
- **Indicadores de Carga**: Animaciones de loading durante operaciones asíncronas
- **Mensajes de Éxito**: Notificaciones automáticas tras operaciones exitosas
- **Validación Visual**: Alertas de advertencia para campos requeridos

### 🔧 **Funcionalidades Principales**
- **Registro de Personas**: Formulario con validación y confirmación
- **Listado Dinámico**: Tabla con datos de personas registradas
- **Modificación**: Edición de registros existentes con confirmación
- **Eliminación**: Borrado seguro con confirmación previa
- **Descarga CSV**: Exportación de datos en formato CSV
- **API de Países**: Integración con REST Countries API

### 🎯 **Mejoras de UX/UI**
- **Select2 Integration**: Búsqueda avanzada en selector de países
- **Responsive Design**: Interfaz adaptable a diferentes dispositivos
- **Animaciones Suaves**: Transiciones y efectos visuales
- **Colores Semánticos**: Botones con colores diferenciados por acción
- **Feedback Visual**: Confirmaciones y mensajes de estado
- **JavaScript Modular**: Código organizado y mantenible

## Tecnologías Utilizadas

### Backend
- **Flask**: Framework web de Python
- **JSON**: Almacenamiento de datos
- **CSV**: Exportación de datos
- **Requests**: Cliente HTTP para APIs

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Estilos modernos y responsivos
- **JavaScript Modular**: Arquitectura separada por responsabilidades
  - `app.js`: Aplicación principal
  - `sweetalert-config.js`: Configuración de alertas
  - `form-validations.js`: Validaciones de formularios
  - `crud-operations.js`: Operaciones de base de datos
  - `select2-config.js`: Configuración de selectores
- **jQuery**: Manipulación del DOM
- **SweetAlert2**: Alertas y modales modernos
- **Select2**: Selector avanzado con búsqueda

## Estructura del Proyecto

```
Insumo Actividad_Open Class 8/
├── app.py                 # Aplicación principal Flask
├── templates/
│   ├── index.html        # Página principal con SweetAlert2
│   └── modificar.html    # Formulario de modificación
├── static/
│   ├── style.css         # Estilos CSS personalizados
│   └── js/               # Archivos JavaScript modulares
│       ├── app.js                 # Archivo principal de la aplicación
│       ├── sweetalert-config.js   # Configuración de SweetAlert2
│       ├── form-validations.js    # Validaciones de formularios
│       ├── crud-operations.js     # Operaciones CRUD
│       ├── select2-config.js      # Configuración de Select2
│       └── README.md             # Documentación JavaScript
├── registros.json        # Base de datos JSON
├── test_app.py           # Pruebas unitarias
├── test_integrado.py     # Pruebas de integración
└── readme.md             # Documentación
```

## Funcionalidades SweetAlert2 Implementadas

### 1. **Registro de Personas**
- Validación de campos requeridos
- Confirmación antes del registro
- Indicador de carga durante el proceso
- Mensaje de éxito tras completar

### 2. **Modificación de Registros**
- Mensaje de bienvenida al cargar
- Validación de formulario
- Confirmación antes de guardar
- Indicador de progreso

### 3. **Eliminación de Registros**
- Confirmación con nombre de la persona
- Advertencia visual clara
- Indicador de eliminación
- Feedback de éxito

### 4. **Descarga de CSV**
- Indicador de preparación
- Mensaje de descarga iniciada

## Principios de Diseño Aplicados

### 🎯 **POO (Programación Orientada a Objetos)**
- Clases bien definidas en Flask
- Encapsulación de funcionalidades
- Herencia y polimorfismo en componentes

### 🔄 **DRY (Don't Repeat Yourself)**
- Funciones reutilizables para operaciones CRUD
- Componentes JavaScript modulares y separados por responsabilidad
- Estilos CSS centralizados
- Configuraciones compartidas entre componentes

### 💡 **KISS (Keep It Simple, Stupid)**
- Interfaz intuitiva y clara
- Flujos de usuario simplificados
- Código legible y mantenible

### 🎯 **Single Responsibility Principle**
- Cada función tiene una responsabilidad específica
- Separación clara entre lógica de negocio y presentación
- Componentes modulares y reutilizables
- Archivos JavaScript separados por funcionalidad específica

## Instalación y Uso

### Requisitos
```bash
pip install flask requests
```

### Ejecución
```bash
python app.py
```

### Acceso
Abrir navegador en: `http://localhost:5000`

## Características Técnicas

### API Integration
- **REST Countries API**: Obtención de lista de países
- **Manejo de Errores**: Gestión robusta de fallos de red
- **Caché Local**: Almacenamiento temporal de datos

### Persistencia de Datos
- **JSON File**: Almacenamiento local de registros
- **Backup Automático**: Guardado automático tras cada operación
- **Integridad de Datos**: Validación antes de guardar

### Seguridad
- **Validación de Entrada**: Sanitización de datos
- **Confirmaciones**: Prevención de operaciones accidentales
- **Manejo de Errores**: Respuestas seguras ante fallos

## Pruebas

### Pruebas Unitarias
```bash
python test_app.py
```

### Pruebas de Integración
```bash
python test_integrado.py
```

## Contribución

1. Fork del proyecto
2. Crear rama de características
3. Commit de cambios
4. Push a la rama
5. Crear Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT.

---

**Desarrollado con ❤️ siguiendo principios de POO, DRY, KISS y Single Responsibility**


