/**
 * Configuración global de SweetAlert2
 * Archivo: static/js/sweetalert-config.js
 * Descripción: Configuraciones y estilos personalizados para SweetAlert2
 */

// Configuración global de SweetAlert2
const SweetAlertConfig = {
    // Configuración por defecto
    default: {
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#6c757d',
        confirmButtonText: 'Aceptar',
        cancelButtonText: 'Cancelar',
        timer: 2000,
        timerProgressBar: true,
        showConfirmButton: false
    },

    // Configuración para confirmaciones
    confirm: {
        icon: 'question',
        showConfirmButton: true,
        showCancelButton: true,
        confirmButtonColor: '#28a745',
        cancelButtonColor: '#6c757d',
        confirmButtonText: 'Sí, continuar',
        cancelButtonText: 'Cancelar'
    },

    // Configuración para advertencias
    warning: {
        icon: 'warning',
        confirmButtonColor: '#ffc107',
        confirmButtonText: 'Entendido'
    },

    // Configuración para errores
    error: {
        icon: 'error',
        confirmButtonColor: '#dc3545',
        confirmButtonText: 'Entendido'
    },

    // Configuración para éxito
    success: {
        icon: 'success',
        confirmButtonColor: '#28a745',
        confirmButtonText: '¡Perfecto!'
    },

    // Configuración para información
    info: {
        icon: 'info',
        confirmButtonColor: '#17a2b8',
        confirmButtonText: 'Entendido'
    }
};

// Función para crear alertas con configuración predefinida
function createAlert(type, title, text, options = {}) {
    const config = { ...SweetAlertConfig.default, ...SweetAlertConfig[type], ...options };

    // Para confirmaciones, asegurar que se muestren los botones
    if (type === 'confirm') {
        config.showConfirmButton = true;
        config.showCancelButton = true;
    }

    return Swal.fire({
        title: title,
        text: text,
        ...config
    });
}

// Función para mostrar loading
function showLoading(title = 'Procesando...', text = 'Por favor espera') {
    return Swal.fire({
        title: title,
        text: text,
        allowOutsideClick: false,
        didOpen: () => {
            Swal.showLoading();
        }
    });
}

// Función para ocultar loading de SweetAlert2
function hideLoading() {
    Swal.close();
}

// Función para mostrar confirmación
function showConfirm(title, text, options = {}) {
    // Asegurar que las opciones de confirmación estén siempre presentes
    const confirmOptions = {
        showConfirmButton: true,
        showCancelButton: true,
        ...options
    };
    return createAlert('confirm', title, text, confirmOptions);
}

// Función para mostrar advertencia
function showWarning(title, text, options = {}) {
    return createAlert('warning', title, text, options);
}

// Función para mostrar error
function showError(title, text, options = {}) {
    return createAlert('error', title, text, options);
}

// Función para mostrar éxito
function showSuccess(title, text, options = {}) {
    return createAlert('success', title, text, options);
}

// Función para mostrar información
function showInfo(title, text, options = {}) {
    return createAlert('info', title, text, options);
}

// Exportar funciones para uso global
window.showLoading = showLoading;
window.hideLoading = hideLoading;
window.showConfirm = showConfirm;
window.showWarning = showWarning;
window.showError = showError;
window.showSuccess = showSuccess;
window.showInfo = showInfo; 