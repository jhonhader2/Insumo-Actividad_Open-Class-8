/**
 * Configuración de Select2
 * Archivo: static/js/select2-config.js
 * Descripción: Configuración y personalización de Select2 para selectores avanzados
 */

// Clase para manejo de Select2
class Select2Manager {
    constructor() {
        this.defaultConfig = {
            theme: 'bootstrap-5',
            placeholder: 'Selecciona una opción',
            allowClear: true,
            width: '100%',
            language: 'es',
            minimumInputLength: 0,
            minimumResultsForSearch: 0, // Habilitar búsqueda siempre
            templateResult: this.templateResult,
            templateSelection: this.templateSelection
        };
    }

    // Template para resultados de búsqueda
    templateResult(data) {
        if (data.loading) return data.text;
        if (!data.id) return data.text;
        return $('<span>').text(data.text);
    }

    // Template para selección
    templateSelection(data) {
        if (!data.id) return data.text;
        return $('<span>').text(data.text);
    }

    // Inicializar Select2 en un elemento
    init(element, customConfig = {}) {
        const config = { ...this.defaultConfig, ...customConfig };

        $(element).select2(config);

        // Agregar eventos personalizados
        this.addCustomEvents(element);

        return $(element);
    }

    // Inicializar Select2 para países (con lista estática del backend)
    initPaises(element) {
        return this.init(element, {
            placeholder: 'Selecciona un país',
            minimumInputLength: 0,
            language: 'es',
            allowClear: true,
            width: '100%',
            minimumResultsForSearch: 0 // Habilitar búsqueda siempre
        });
    }

    // Agregar eventos personalizados
    addCustomEvents(element) {
        const $element = $(element);

        // Evento al abrir
        $element.on('select2:open', function () {
            // Personalizar comportamiento al abrir
            console.log('Select2 abierto');
        });

        // Evento al seleccionar
        $element.on('select2:select', function (e) {
            // Personalizar comportamiento al seleccionar
            console.log('Opción seleccionada:', e.params.data);
        });

        // Evento al cambiar
        $element.on('select2:change', function (e) {
            // Personalizar comportamiento al cambiar
            console.log('Valor cambiado:', e.target.value);
        });
    }

    // Limpiar selección
    clear(element) {
        $(element).val('').trigger('change');
    }

    // Deshabilitar Select2
    disable(element) {
        $(element).prop('disabled', true).trigger('change');
    }

    // Habilitar Select2
    enable(element) {
        $(element).prop('disabled', false).trigger('change');
    }

    // Destruir Select2
    destroy(element) {
        $(element).select2('destroy');
    }

    // Obtener valor seleccionado
    getValue(element) {
        return $(element).val();
    }

    // Establecer valor
    setValue(element, value) {
        $(element).val(value).trigger('change');
    }

    // Verificar si tiene valor
    hasValue(element) {
        const value = $(element).val();
        return value && value !== '';
    }
}

// Instancia global del manager de Select2
const select2Manager = new Select2Manager();

// Función para inicializar Select2 en países
function initSelect2Paises() {
    if ($.fn.select2) {
        console.log('Inicializando Select2 para países...');
        select2Manager.initPaises('.select2-paises');
        console.log('Select2 para países inicializado correctamente');
    } else {
        console.error('Select2 no está disponible');
    }
}

// Función para inicializar Select2 en cualquier elemento
function initSelect2(selector, config = {}) {
    if ($.fn.select2) {
        select2Manager.init(selector, config);
    }
}

// Función para limpiar Select2
function clearSelect2(selector) {
    select2Manager.clear(selector);
}

// Función para deshabilitar Select2
function disableSelect2(selector) {
    select2Manager.disable(selector);
}

// Función para habilitar Select2
function enableSelect2(selector) {
    select2Manager.enable(selector);
}

// Función para obtener valor de Select2
function getSelect2Value(selector) {
    return select2Manager.getValue(selector);
}

// Función para establecer valor en Select2
function setSelect2Value(selector, value) {
    select2Manager.setValue(selector, value);
}

// Función para verificar si Select2 tiene valor
function hasSelect2Value(selector) {
    return select2Manager.hasValue(selector);
}

// Configuración personalizada para diferentes tipos de selectores
const Select2Configs = {
    // Configuración para países
    paises: {
        placeholder: 'Selecciona un país',
        minimumInputLength: 0,
        language: 'es',
        allowClear: true,
        minimumResultsForSearch: 0 // Habilitar búsqueda siempre
    },

    // Configuración para selección simple
    simple: {
        placeholder: 'Selecciona una opción',
        allowClear: true,
        minimumResultsForSearch: 10
    },

    // Configuración para búsqueda avanzada
    search: {
        placeholder: 'Buscar...',
        minimumInputLength: 1,
        language: 'es'
    }
};

// Inicializar Select2 cuando el DOM esté listo
$(document).ready(function () {
    console.log('DOM listo, inicializando Select2...');
    initSelect2Paises();
}); 