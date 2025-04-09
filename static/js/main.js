document.addEventListener('DOMContentLoaded', function() {
    // Dropdown: activación por hover en escritorio (ancho > 991px)
    const dropdowns = document.querySelectorAll('.nav-item.dropdown');
    if (window.innerWidth > 991) {
        dropdowns.forEach(dropdown => {
            dropdown.addEventListener('mouseenter', function() {
                this.classList.add('show');
                const toggle = this.querySelector('.dropdown-toggle');
                const menu = this.querySelector('.dropdown-menu');
                toggle.setAttribute('aria-expanded', 'true');
                menu.classList.add('show');
            });
            dropdown.addEventListener('mouseleave', function() {
                this.classList.remove('show');
                const toggle = this.querySelector('.dropdown-toggle');
                const menu = this.querySelector('.dropdown-menu');
                toggle.setAttribute('aria-expanded', 'false');
                menu.classList.remove('show');
            });
        });
    }

    // Manejar el click en el menú principal
    const navLinks = document.querySelectorAll('.nav-link[data-section]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            // Actualizar enlace activo
            document.querySelectorAll('.nav-link').forEach(item => item.classList.remove('active'));
            this.classList.add('active');
            // Mostrar la sección correspondiente
            const sectionId = this.getAttribute('data-section');
            document.querySelectorAll('.section-container').forEach(section => section.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');
        });
    });

// Manejar el clic en el enlace principal de la categoría (dropdown-toggle)
const dropdownToggles = document.querySelectorAll('.nav-item.dropdown .dropdown-toggle');
dropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', function(e) {
        // Evitamos el comportamiento por defecto (abrir el menú)
        e.preventDefault();
        // Obtenemos el valor de data-section del enlace (que ya agregamos en el HTML)
        const sectionId = this.getAttribute('data-section');
        if (sectionId) {
            // Actualizamos los enlaces activos
            document.querySelectorAll('.nav-link').forEach(item => item.classList.remove('active'));
            this.classList.add('active');
            // Mostramos la sección correspondiente (la categoría completa)
            document.querySelectorAll('.section-container').forEach(section => section.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');
        }
    });
});


    // Manejo para los ítems del dropdown (con data-sub cuando corresponde)
    const dropdownItems = document.querySelectorAll('.dropdown-item');
    dropdownItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            // Actualizamos el enlace activo en el dropdown principal
            const parentDropdown = this.closest('.dropdown');
            parentDropdown.querySelector('.dropdown-toggle').classList.add('active');
            // Mostrar la sección principal
            const sectionId = this.getAttribute('data-section');
            document.querySelectorAll('.section-container').forEach(section => section.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');
            // Si hay un data-sub, podemos intentar hacer scroll hasta esa subsección
            const subSection = this.getAttribute('data-sub');
            if (subSection) {
                setTimeout(() => {
                    const subElement = document.getElementById(subSection);
                    if (subElement) {
                        subElement.scrollIntoView({ behavior: 'smooth' });
                    }
                }, 100);
            }
        });
    });
});
