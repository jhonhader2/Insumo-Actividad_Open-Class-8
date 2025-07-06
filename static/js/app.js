/**
 * Archivo principal de la aplicación
 * Archivo: static/js/app.js
 * Descripción: Inicialización y configuración principal de la aplicación
 */

// Clase principal de la aplicación
class App {
    constructor() {
        this.isInitialized = false;
        this.config = {
            debug: true,
            autoRefresh: false,
            refreshInterval: 30000 // 30 segundos
        };
    }

    // Inicializar la aplicación
    init() {
        if (this.isInitialized) {
            console.warn('La aplicación ya está inicializada');
            return;
        }

        try {
            this.log('Inicializando aplicación...');

            // Inicializar componentes
            this.initComponents();

            // Configurar eventos
            this.setupEvents();

            // Configurar mensajes de éxito
            this.setupSuccessMessages();

            // Marcar como inicializada
            this.isInitialized = true;

            this.log('Aplicación inicializada correctamente');

        } catch (error) {
            console.error('Error al inicializar la aplicación:', error);
            this.showError('Error de inicialización', 'No se pudo inicializar la aplicación correctamente');
        }
    }

    // Inicializar componentes
    initComponents() {
        // Inicializar Select2
        this.initSelect2();

        // Inicializar formularios
        this.initForms();

        // Inicializar validaciones
        this.initValidations();
    }

    // Inicializar Select2
    initSelect2() {
        if (typeof initSelect2Paises === 'function') {
            initSelect2Paises();
            this.log('Select2 inicializado');
        }
    }

    // Inicializar formularios
    initForms() {
        // Formulario de registro
        const registroForm = document.getElementById('registroForm');
        if (registroForm) {
            registroForm.addEventListener('submit', this.handleRegistroSubmit.bind(this));
            this.log('Formulario de registro configurado');
        }

        // Formulario de modificación
        const modificarForm = document.getElementById('modificarForm');
        if (modificarForm) {
            modificarForm.addEventListener('submit', this.handleModificarSubmit.bind(this));
            this.log('Formulario de modificación configurado');
        }
    }

    // Inicializar validaciones
    initValidations() {
        // Configurar validación en tiempo real para campos de texto
        const textInputs = document.querySelectorAll('input[type="text"]');
        textInputs.forEach(input => {
            // Formatear a mayúsculas
            input.addEventListener('input', (e) => {
                if (typeof formatToUpperCase === 'function') {
                    formatToUpperCase(e.target);
                }

                // Validar duplicados en tiempo real para el campo nombre
                if (input.id === 'nombre' && typeof validarNombreEnTiempoReal === 'function') {
                    validarNombreEnTiempoReal(e.target);
                }
            });

            // Prevenir envío con Enter
            input.addEventListener('keypress', (e) => {
                if (typeof preventEnterSubmit === 'function') {
                    preventEnterSubmit(e);
                }
            });
        });

        // Configurar botones de eliminación
        const deleteButtons = document.querySelectorAll('.delete-btn');
        deleteButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                const index = e.target.dataset.index;
                const nombre = e.target.dataset.nombre;
                if (typeof confirmarEliminacion === 'function') {
                    confirmarEliminacion(index, nombre);
                }
            });
        });
    }

    // Configurar eventos
    setupEvents() {
        // Evento de carga completa de la página
        document.addEventListener('DOMContentLoaded', () => {
            this.log('DOM cargado completamente');
        });

        // Evento de visibilidad de la página
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.log('Página oculta');
            } else {
                this.log('Página visible');
            }
        });

        // Evento de error global
        window.addEventListener('error', (e) => {
            this.log('Error global detectado:', e.error);
        });
    }

    // Configurar mensajes de éxito y error
    setupSuccessMessages() {
        // Mostrar mensaje de éxito si hay parámetro en la URL
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.get('success') === 'true') {
            if (typeof showSuccess === 'function') {
                showSuccess('¡Operación exitosa!', 'La operación se completó correctamente');
            }
        }

        // Mostrar mensaje de error si hay parámetro de error en la URL
        if (urlParams.get('error') === 'duplicado') {
            const nombre = urlParams.get('nombre');
            if (typeof showError === 'function') {
                showError('Error de duplicado', `Ya existe una persona registrada con el nombre "${nombre}"`);
            }
        }
    }

    // Manejar envío del formulario de registro
    async handleRegistroSubmit(event) {
        if (typeof registrarPersona === 'function') {
            await registrarPersona(event);
        }
    }

    // Manejar envío del formulario de modificación
    async handleModificarSubmit(event) {
        if (typeof modificarPersona === 'function') {
            await modificarPersona(event);
        }
    }

    // Mostrar error
    showError(title, message) {
        if (typeof showError === 'function') {
            showError(title, message);
        } else {
            console.error(title, message);
        }
    }

    // Función de logging
    log(message, data = null) {
        if (this.config.debug) {
            if (data) {
                console.log(`[App] ${message}`, data);
            } else {
                console.log(`[App] ${message}`);
            }
        }
    }

    // Habilitar modo debug
    enableDebug() {
        this.config.debug = true;
        this.log('Modo debug habilitado');
    }

    // Deshabilitar modo debug
    disableDebug() {
        this.config.debug = false;
        this.log('Modo debug deshabilitado');
    }

    // Refrescar datos
    async refreshData() {
        if (typeof refreshData === 'function') {
            return await refreshData();
        }
        return null;
    }

    // Limpiar formularios
    clearForms() {
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            if (typeof clearForm === 'function') {
                clearForm(form.id);
            }
        });
    }
}

// Instancia global de la aplicación
const app = new App();

// Función para inicializar la aplicación cuando el DOM esté listo
function initApp() {
    app.init();
}

// Función para habilitar modo debug
function enableDebugMode() {
    app.enableDebug();
}

// Función para deshabilitar modo debug
function disableDebugMode() {
    app.disableDebug();
}

// Función para refrescar datos
async function refreshAppData() {
    return await app.refreshData();
}

// Función para limpiar formularios
function clearAppForms() {
    app.clearForms();
}

// Inicializar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}

// Exportar para uso global
window.App = App;
window.app = app;
window.initApp = initApp;
window.enableDebugMode = enableDebugMode;
window.disableDebugMode = disableDebugMode;
window.refreshAppData = refreshAppData;
window.clearAppForms = clearAppForms;

// ========================================
// FUNCIONES DE ANIMACIÓN Y EFECTOS
// ========================================

// Clase para manejar animaciones
class AnimationManager {
    constructor() {
        this.observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        this.observer = null;
    }

    // Inicializar animaciones
    init() {
        this.setupIntersectionObserver();
        this.setupHoverEffects();
        this.setupFormEffects();
    }

    // Configurar observador de intersección para animaciones
    setupIntersectionObserver() {
        this.observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, this.observerOptions);

        // Observar elementos para animación
        const elementsToAnimate = document.querySelectorAll('.form-card, .table-container, .stats, .person-info');
        elementsToAnimate.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            this.observer.observe(el);
        });
    }

    // Configurar efectos hover
    setupHoverEffects() {
        // Efecto hover en las filas de la tabla
        document.querySelectorAll('tbody tr').forEach(row => {
            row.addEventListener('mouseenter', function () {
                this.style.transform = 'scale(1.01)';
                this.style.boxShadow = '0 4px 8px rgba(0,0,0,0.1)';
            });

            row.addEventListener('mouseleave', function () {
                this.style.transform = 'scale(1)';
                this.style.boxShadow = 'none';
            });
        });

        // Efecto hover en botones
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('mouseenter', function () {
                this.style.transform = 'translateY(-2px)';
            });

            btn.addEventListener('mouseleave', function () {
                this.style.transform = 'translateY(0)';
            });
        });
    }

    // Configurar efectos de formulario
    setupFormEffects() {
        // Mostrar loading al enviar formulario de modificación
        const modificarForm = document.getElementById('modificarForm');
        if (modificarForm) {
            modificarForm.addEventListener('submit', function () {
                const loadingOverlay = document.getElementById('loadingOverlay');
                if (loadingOverlay) {
                    loadingOverlay.classList.add('show');
                }
            });
        }
    }
}

// Clase para manejar loading
class LoadingManager {
    constructor() {
        this.overlay = document.getElementById('loadingOverlay');
    }

    // Mostrar loading
    show() {
        if (this.overlay) {
            this.overlay.classList.add('show');
        }
    }

    // Ocultar loading
    hide() {
        if (this.overlay) {
            this.overlay.classList.remove('show');
        }
    }
}

// Clase para manejar mensajes específicos de página
class PageMessageManager {
    constructor() {
        this.currentPage = this.detectCurrentPage();
    }

    // Detectar página actual
    detectCurrentPage() {
        const path = window.location.pathname;
        if (path.includes('/modificar/')) {
            return 'modificar';
        }
        return 'index';
    }

    // Mostrar mensajes específicos de página
    showPageMessages() {
        if (this.currentPage === 'modificar') {
            this.showModificarWelcome();
        }
    }

    // Mostrar mensaje de bienvenida en página de modificación
    showModificarWelcome() {
        // Obtener el nombre de la persona desde el DOM
        const personInfo = document.querySelector('.person-info p');
        if (personInfo) {
            const nombreMatch = personInfo.textContent.match(/Nombre:\s*([^|]+)/);
            if (nombreMatch && typeof showInfo === 'function') {
                const nombre = nombreMatch[1].trim();
                showInfo('Modificando registro', `Estás modificando el registro de ${nombre}`);
            }
        }
    }
}

// Instancias globales
const animationManager = new AnimationManager();
const loadingManager = new LoadingManager();
const pageMessageManager = new PageMessageManager();

// Función para inicializar animaciones
function initAnimations() {
    animationManager.init();
}

// Función para mostrar loading
function showLoading() {
    loadingManager.show();
}

// Función para ocultar loading
function hideLoading() {
    loadingManager.hide();
}

// Función para mostrar mensajes de página
function showPageMessages() {
    pageMessageManager.showPageMessages();
}

// Inicializar animaciones cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function () {
    initAnimations();
    showPageMessages();
});

// Mostrar mensaje de bienvenida al cargar la página (para modificar.html)
window.addEventListener('load', function () {
    showPageMessages();
});

// Exportar funciones adicionales
window.AnimationManager = AnimationManager;
window.LoadingManager = LoadingManager;
window.PageMessageManager = PageMessageManager;
window.initAnimations = initAnimations;
window.showLoading = showLoading;
window.hideLoading = hideLoading;
window.showPageMessages = showPageMessages; 