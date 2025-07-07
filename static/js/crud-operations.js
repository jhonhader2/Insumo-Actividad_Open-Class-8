/**
 * Operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
 * Archivo: static/js/crud-operations.js
 * Descripción: Funciones para manejar operaciones de base de datos
 */

// Clase para manejo de operaciones CRUD
class CrudOperations {
    constructor() {
        this.baseUrl = window.location.origin;
    }

    // Crear nuevo registro
    async create(data) {
        try {
            const response = await fetch('/registrar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams(data)
            });

            if (response.ok) {
                return { success: true, message: 'Registro creado exitosamente' };
            } else {
                throw new Error('Error al crear el registro');
            }
        } catch (error) {
            return { success: false, message: error.message };
        }
    }

    // Actualizar registro existente
    async update(index, data) {
        try {
            const response = await fetch(`/modificar/${index}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams(data)
            });

            if (response.ok) {
                return { success: true, message: 'Registro actualizado exitosamente' };
            } else {
                throw new Error('Error al actualizar el registro');
            }
        } catch (error) {
            return { success: false, message: error.message };
        }
    }

    // Eliminar registro
    async delete(index) {
        try {
            const response = await fetch(`/eliminar/${index}`, {
                method: 'GET'
            });

            if (response.ok) {
                return { success: true, message: 'Registro eliminado exitosamente' };
            } else {
                throw new Error('Error al eliminar el registro');
            }
        } catch (error) {
            return { success: false, message: error.message };
        }
    }

    // Obtener datos JSON
    async getJsonData() {
        try {
            const response = await fetch('/personas_json');
            if (response.ok) {
                return await response.json();
            } else {
                throw new Error('Error al obtener los datos');
            }
        } catch (error) {
            return { success: false, message: error.message };
        }
    }
}

// Instancia global de operaciones CRUD
const crudOps = new CrudOperations();

// Función helper para ocultar el loading de SweetAlert2
function hideAllLoading() {
    Swal.close();
}

// Función para registrar nueva persona
async function registrarPersona(event) {
    event.preventDefault();

    // Validar formulario (ahora es asíncrono)
    const validator = await validateRegistrationForm();
    if (validator.hasErrors()) {
        showValidationErrors(validator.getErrors());
        return false;
    }

    // Obtener datos del formulario
    const formData = new FormData(event.target);
    const data = {
        nombre: formData.get('nombre').toUpperCase(),
        pais: formData.get('pais')
    };

    // Mostrar confirmación
    const result = await showConfirm(
        '¿Registrar persona?',
        `¿Deseas registrar a ${data.nombre} de ${data.pais}?`
    );

    if (result.isConfirmed) {
        // Mostrar loading
        const loadingAlert = showLoading('Registrando...', 'Por favor espera');

        try {
            // Realizar operación
            const response = await crudOps.create(data);

            if (response.success) {
                showSuccess('¡Registro exitoso!', response.message);
                // Redirigir después de un breve delay
                setTimeout(() => {
                    window.location.href = '/?success=true';
                }, 1500);
            } else {
                showError('Error al registrar', response.message);
            }
        } catch (error) {
            showError('Error de conexión', 'No se pudo conectar con el servidor');
        } finally {
            // Ocultar todos los tipos de loading
            hideAllLoading();
        }
    }

    return false;
}

// Función para modificar persona
async function modificarPersona(event) {
    event.preventDefault();

    // Validar formulario
    const validator = validateModificationForm();
    if (validator.hasErrors()) {
        showValidationErrors(validator.getErrors());
        return false;
    }

    // Obtener datos del formulario
    const formData = new FormData(event.target);
    const data = {
        nombre: formData.get('nombre').toUpperCase(),
        pais: formData.get('pais')
    };

    // Obtener índice de la URL
    const urlParts = window.location.pathname.split('/');
    const index = urlParts[urlParts.length - 1];

    // Mostrar confirmación
    const result = await showConfirm(
        '¿Guardar cambios?',
        `¿Deseas guardar los cambios para ${data.nombre}?`
    );

    if (result.isConfirmed) {
        // Mostrar loading de SweetAlert2
        const loadingAlert = showLoading('Guardando...', 'Por favor espera');

        try {
            // Realizar operación
            const response = await crudOps.update(index, data);

            if (response.success) {
                showSuccess('¡Cambios guardados!', response.message);
                // Redirigir después de un breve delay
                setTimeout(() => {
                    window.location.href = '/?success=true';
                }, 1500);
            } else {
                showError('Error al guardar', response.message);
            }
        } catch (error) {
            showError('Error de conexión', 'No se pudo conectar con el servidor');
        } finally {
            // Ocultar todos los tipos de loading
            hideAllLoading();
        }
    }

    return false;
}

// Función para confirmar eliminación
async function confirmarEliminacion(index, nombre) {
    const result = await showConfirm(
        '¿Eliminar registro?',
        `¿Estás seguro de que deseas eliminar a ${nombre}?`,
        {
            confirmButtonText: 'Sí, eliminar',
            confirmButtonColor: '#dc3545'
        }
    );

    if (result.isConfirmed) {
        // Mostrar loading
        const loadingAlert = showLoading('Eliminando...', 'Por favor espera');

        try {
            // Realizar operación
            const response = await crudOps.delete(index);

            if (response.success) {
                showSuccess('¡Registro eliminado!', response.message);
                // Redirigir después de un breve delay
                setTimeout(() => {
                    window.location.href = '/?success=true';
                }, 1500);
            } else {
                showError('Error al eliminar', response.message);
            }
        } catch (error) {
            showError('Error de conexión', 'No se pudo conectar con el servidor');
        } finally {
            // Ocultar todos los tipos de loading
            hideAllLoading();
        }
    }
}

// Función para descargar CSV
function confirmarDescarga(event) {
    event.preventDefault();

    // Detectar si es móvil
    const isMobile = window.innerWidth <= 768;

    const confirmMessage = isMobile
        ? '¿Descargar CSV?\n\nEl archivo se descargará automáticamente.'
        : '¿Descargar CSV?\n\nSe descargará un archivo con todos los registros';

    showConfirm(
        '¿Descargar CSV?',
        confirmMessage,
        {
            confirmButtonText: 'Sí, descargar',
            confirmButtonColor: '#28a745',
            cancelButtonText: 'Cancelar'
        }
    ).then((result) => {
        if (result.isConfirmed) {
            // Mostrar loading específico para descarga
            const loadingAlert = showLoading(
                'Preparando descarga...',
                isMobile ? 'Generando archivo CSV...' : 'Preparando archivo para descarga...'
            );

            // Simular un pequeño delay para mejor UX
            setTimeout(() => {
                // Ocultar loading
                Swal.close();

                // Mostrar mensaje de éxito
                showSuccess(
                    '¡Descarga iniciada!',
                    isMobile ? 'El archivo CSV se está descargando' : 'El archivo CSV se está descargando',
                    {
                        timer: 2000,
                        showConfirmButton: false
                    }
                );

                // Iniciar descarga después de mostrar el mensaje
                setTimeout(() => {
                    window.location.href = '/descargar_csv';
                }, 500);
            }, 1000);
        }
    });

    return false;
}

// Función para refrescar datos
async function refreshData() {
    try {
        const data = await crudOps.getJsonData();
        if (data.success === false) {
            showError('Error al cargar datos', data.message);
        }
        return data;
    } catch (error) {
        showError('Error de conexión', 'No se pudieron cargar los datos');
        return null;
    }
} 