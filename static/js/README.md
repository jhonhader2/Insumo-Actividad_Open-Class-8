# Documentación JavaScript - App Registro de Personas

## 📁 Estructura de Archivos JavaScript

```
static/js/
├── app.js                 # Archivo principal de la aplicación
├── sweetalert-config.js   # Configuración de SweetAlert2
├── form-validations.js    # Validaciones de formularios
├── crud-operations.js     # Operaciones CRUD
├── select2-config.js      # Configuración de Select2
└── README.md             # Esta documentación
```

## 🎯 Principios de Diseño Aplicados

### **POO (Programación Orientada a Objetos)**
- **Clases bien definidas**: `App`, `FormValidator`, `CrudOperations`, `Select2Manager`
- **Encapsulación**: Métodos y propiedades organizados en clases
- **Herencia y polimorfismo**: Configuraciones extensibles

### **DRY (Don't Repeat Yourself)**
- **Funciones reutilizables**: Configuraciones centralizadas
- **Componentes modulares**: Cada archivo tiene una responsabilidad específica
- **Código compartido**: Funciones utilitarias globales

### **KISS (Keep It Simple, Stupid)**
- **Interfaz simple**: Funciones con nombres descriptivos
- **Lógica clara**: Código fácil de entender y mantener
- **Configuración intuitiva**: Parámetros con valores por defecto

### **Single Responsibility Principle**
- **Un archivo, una responsabilidad**: Cada archivo maneja un aspecto específico
- **Funciones específicas**: Cada función tiene un propósito claro
- **Separación de concerns**: Lógica de negocio separada de la presentación

## 📋 Descripción de Archivos

### 1. **app.js** - Archivo Principal
**Responsabilidad**: Inicialización y configuración principal de la aplicación

**Características**:
- Clase `App` para gestión centralizada
- Inicialización automática de componentes
- Manejo de eventos globales
- Configuración de debug
- Gestión del ciclo de vida de la aplicación

**Funciones principales**:
```javascript
// Inicializar aplicación
initApp()

// Habilitar/deshabilitar debug
enableDebugMode()
disableDebugMode()

// Refrescar datos
refreshAppData()

// Limpiar formularios
clearAppForms()
```

### 2. **sweetalert-config.js** - Configuración SweetAlert2
**Responsabilidad**: Configuración y funciones para alertas y modales

**Características**:
- Configuraciones predefinidas por tipo de alerta
- Funciones helper para crear alertas
- Estilos personalizados
- Configuración global centralizada

**Funciones principales**:
```javascript
// Alertas por tipo
showConfirm(title, text, options)
showWarning(title, text, options)
showError(title, text, options)
showSuccess(title, text, options)
showInfo(title, text, options)

// Loading
showLoading(title, text)
```

### 3. **form-validations.js** - Validaciones de Formularios
**Responsabilidad**: Validación de datos y manejo de formularios

**Características**:
- Clase `FormValidator` para validaciones
- Validaciones específicas por tipo de campo
- Manejo de errores de validación
- Funciones utilitarias para formularios

**Funciones principales**:
```javascript
// Validaciones
validateRegistrationForm()
validateModificationForm()

// Utilidades
clearForm(formId)
toggleSubmitButton(formId, disabled)
formatToUpperCase(input)
showValidationErrors(errors)
```

### 4. **crud-operations.js** - Operaciones CRUD
**Responsabilidad**: Operaciones de base de datos (Crear, Leer, Actualizar, Eliminar)

**Características**:
- Clase `CrudOperations` para manejo de datos
- Operaciones asíncronas con fetch API
- Manejo de errores robusto
- Funciones específicas por operación

**Funciones principales**:
```javascript
// Operaciones CRUD
registrarPersona(event)
modificarPersona(event)
confirmarEliminacion(index, nombre)
confirmarDescarga(event)

// Utilidades
refreshData()
```

### 5. **select2-config.js** - Configuración Select2
**Responsabilidad**: Configuración y personalización de selectores avanzados

**Características**:
- Clase `Select2Manager` para gestión de Select2
- Configuraciones predefinidas
- Templates personalizados
- Manejo de eventos específicos

**Funciones principales**:
```javascript
// Inicialización
initSelect2Paises()
initSelect2(selector, config)

// Utilidades
clearSelect2(selector)
disableSelect2(selector)
enableSelect2(selector)
getSelect2Value(selector)
setSelect2Value(selector, value)
```

## 🔧 Configuración y Uso

### **Orden de Carga**
Los archivos deben cargarse en el siguiente orden:

1. **Librerías externas** (jQuery, Select2, SweetAlert2)
2. **sweetalert-config.js** - Configuración base
3. **form-validations.js** - Validaciones
4. **select2-config.js** - Configuración Select2
5. **crud-operations.js** - Operaciones CRUD
6. **app.js** - Aplicación principal

### **Ejemplo de Implementación**
```html
<!-- Librerías externas -->
<script src="jquery.min.js"></script>
<script src="select2.min.js"></script>
<script src="sweetalert2.min.js"></script>

<!-- JavaScript personalizado -->
<script src="js/sweetalert-config.js"></script>
<script src="js/form-validations.js"></script>
<script src="js/select2-config.js"></script>
<script src="js/crud-operations.js"></script>
<script src="js/app.js"></script>
```

## 🎨 Personalización

### **Configuración de SweetAlert2**
```javascript
// Personalizar colores
SweetAlertConfig.confirm.confirmButtonColor = '#custom-color';

// Agregar nueva configuración
SweetAlertConfig.custom = {
    icon: 'custom',
    confirmButtonColor: '#custom-color'
};
```

### **Configuración de Select2**
```javascript
// Personalizar configuración
const customConfig = {
    placeholder: 'Selecciona...',
    minimumInputLength: 2
};

initSelect2('.custom-select', customConfig);
```

### **Configuración de Validaciones**
```javascript
// Agregar nueva validación
FormValidator.prototype.validateCustom = function(value, fieldName) {
    // Lógica de validación personalizada
};
```

## 🐛 Debug y Mantenimiento

### **Habilitar Modo Debug**
```javascript
// En consola del navegador
enableDebugMode();

// Ver logs detallados
app.log('Mensaje de debug');
```

### **Funciones de Utilidad**
```javascript
// Refrescar datos
refreshAppData();

// Limpiar formularios
clearAppForms();

// Verificar estado de la aplicación
console.log(app.isInitialized);
```

## 📈 Ventajas de la Separación

### **Mantenibilidad**
- Código organizado y fácil de mantener
- Cambios localizados en archivos específicos
- Debugging más eficiente

### **Reutilización**
- Componentes modulares reutilizables
- Configuraciones centralizadas
- Funciones utilitarias compartidas

### **Escalabilidad**
- Fácil agregar nuevas funcionalidades
- Estructura preparada para crecimiento
- Separación clara de responsabilidades

### **Colaboración**
- Múltiples desarrolladores pueden trabajar en paralelo
- Conflictos de merge reducidos
- Código más legible y documentado

---

**Desarrollado siguiendo principios de POO, DRY, KISS y Single Responsibility**

# Configuración de Select2

## Descripción
Este archivo contiene la configuración y personalización de Select2 para selectores avanzados en la aplicación de registro de personas.

## Características
- **Búsqueda en tiempo real**: Los usuarios pueden buscar países escribiendo en el campo
- **Interfaz en español**: Mensajes y placeholders en español
- **Tema Bootstrap 5**: Diseño moderno y responsive
- **Limpieza de selección**: Botón para limpiar la selección actual
- **Validación**: Integración con validaciones de formularios

## Archivos principales

### select2-config.js
Contiene la clase `Select2Manager` que maneja toda la configuración de Select2:

```javascript
// Inicializar Select2 en países
initSelect2Paises();

// Inicializar Select2 personalizado
initSelect2('#mi-selector', {
    placeholder: 'Selecciona una opción',
    allowClear: true
});
```

## Configuración

### Configuración por defecto
```javascript
{
    theme: 'bootstrap-5',
    placeholder: 'Selecciona una opción',
    allowClear: true,
    width: '100%',
    language: 'es',
    minimumInputLength: 0,
    minimumResultsForSearch: 0
}
```

### Configuración específica para países
```javascript
{
    placeholder: 'Selecciona un país',
    minimumInputLength: 0,
    language: 'es',
    allowClear: true,
    minimumResultsForSearch: 0
}
```

## Uso en HTML

### Selector básico
```html
<select id="pais" name="pais" class="select2-paises" required>
    <option value="">Selecciona un país</option>
    <option value="Colombia">Colombia</option>
    <option value="México">México</option>
    <!-- más opciones... -->
</select>
```

### Librerías requeridas
```html
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />
<link href="https://cdn.jsdelivr.net/npm/select2-bootstrap-5-theme@1.3.0/dist/select2-bootstrap-5-theme.min.css" rel="stylesheet" />

<!-- JavaScript -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/i18n/es.js"></script>
```

## Funciones disponibles

### Inicialización
- `initSelect2Paises()`: Inicializa Select2 en elementos con clase `select2-paises`
- `initSelect2(selector, config)`: Inicializa Select2 en cualquier selector

### Manipulación
- `clearSelect2(selector)`: Limpia la selección
- `disableSelect2(selector)`: Deshabilita el selector
- `enableSelect2(selector)`: Habilita el selector
- `getSelect2Value(selector)`: Obtiene el valor seleccionado
- `setSelect2Value(selector, value)`: Establece un valor
- `hasSelect2Value(selector)`: Verifica si tiene valor

## Solución de problemas

### La búsqueda no funciona
1. Verificar que `minimumResultsForSearch: 0` esté configurado
2. Asegurar que jQuery esté cargado antes que Select2
3. Verificar que la clase `select2-paises` esté aplicada al select

### Select2 no se inicializa
1. Verificar que todas las librerías estén cargadas
2. Revisar la consola del navegador para errores
3. Asegurar que el DOM esté listo antes de inicializar

### Estilos no se aplican
1. Verificar que los archivos CSS de Select2 estén cargados
2. Asegurar que el tema Bootstrap 5 esté incluido
3. Verificar que no haya conflictos con otros estilos

## Ejemplo de uso completo

```html
<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />
    <link href="https://cdn.jsdelivr.net/npm/select2-bootstrap-5-theme@1.3.0/dist/select2-bootstrap-5-theme.min.css" rel="stylesheet" />
</head>
<body>
    <select id="pais" class="select2-paises">
        <option value="">Selecciona un país</option>
        <option value="Colombia">Colombia</option>
        <option value="México">México</option>
    </select>

    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/i18n/es.js"></script>
    <script src="static/js/select2-config.js"></script>
    
    <script>
        $(document).ready(function() {
            initSelect2Paises();
        });
    </script>
</body>
</html>
```

## Notas importantes
- Select2 requiere jQuery para funcionar
- La búsqueda funciona con la lista de opciones que ya están en el HTML
- Los países se cargan desde el backend (Flask) y se renderizan en el template
- La configuración está optimizada para listas pequeñas y medianas 