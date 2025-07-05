/**
 * Validaciones de formularios y manejo de eventos
 * Archivo: static/js/form-validations.js
 * Descripción: Funciones para validar formularios y manejar eventos de entrada
 */

// Clase para manejo de validaciones
class FormValidator {
    constructor() {
        this.errors = [];
    }

    // Validar campo requerido
    validateRequired(value, fieldName) {
        if (!value || value.trim() === '') {
            this.errors.push(`El campo ${fieldName} es requerido`);
            return false;
        }
        return true;
    }

    // Validar longitud mínima
    validateMinLength(value, minLength, fieldName) {
        if (value && value.length < minLength) {
            this.errors.push(`${fieldName} debe tener al menos ${minLength} caracteres`);
            return false;
        }
        return true;
    }

    // Validar longitud máxima
    validateMaxLength(value, maxLength, fieldName) {
        if (value && value.length > maxLength) {
            this.errors.push(`${fieldName} no puede exceder ${maxLength} caracteres`);
            return false;
        }
        return true;
    }

    // Validar formato de email
    validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email && !emailRegex.test(email)) {
            this.errors.push('El formato del email no es válido');
            return false;
        }
        return true;
    }

    // Obtener errores
    getErrors() {
        return this.errors;
    }

    // Limpiar errores
    clearErrors() {
        this.errors = [];
    }

    // Verificar si hay errores
    hasErrors() {
        return this.errors.length > 0;
    }
}

// Función para validar formulario de registro
function validateRegistrationForm() {
    const validator = new FormValidator();

    const nombre = document.getElementById('nombre').value;
    const pais = document.getElementById('pais').value;

    // Validar campos requeridos
    validator.validateRequired(nombre, 'Nombre');
    validator.validateRequired(pais, 'País');

    // Validar longitud del nombre
    validator.validateMinLength(nombre, 2, 'Nombre');
    validator.validateMaxLength(nombre, 50, 'Nombre');

    return validator;
}

// Función para validar formulario de modificación
function validateModificationForm() {
    const validator = new FormValidator();

    const nombre = document.getElementById('nombre').value;
    const pais = document.getElementById('pais').value;

    // Validar campos requeridos
    validator.validateRequired(nombre, 'Nombre');
    validator.validateRequired(pais, 'País');

    // Validar longitud del nombre
    validator.validateMinLength(nombre, 2, 'Nombre');
    validator.validateMaxLength(nombre, 50, 'Nombre');

    return validator;
}

// Función para mostrar errores de validación
function showValidationErrors(errors) {
    if (errors.length === 1) {
        showWarning('Error de validación', errors[0]);
    } else {
        const errorList = errors.map(error => `• ${error}`).join('\n');
        showWarning('Errores de validación', errorList);
    }
}

// Función para limpiar formulario
function clearForm(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.reset();

        // Limpiar Select2 si existe
        if ($.fn.select2) {
            $(form).find('.select2-paises').val('').trigger('change');
        }
    }
}

// Función para habilitar/deshabilitar botón de envío
function toggleSubmitButton(formId, disabled = false) {
    const submitButton = document.querySelector(`#${formId} input[type="submit"]`);
    if (submitButton) {
        submitButton.disabled = disabled;
        submitButton.style.opacity = disabled ? '0.6' : '1';
    }
}

// Función para formatear texto a mayúsculas
function formatToUpperCase(input) {
    input.value = input.value.toUpperCase();
}

// Función para prevenir envío de formulario con Enter en campos de texto
function preventEnterSubmit(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        return false;
    }
} 