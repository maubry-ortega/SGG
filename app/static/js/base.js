// base.js: utilidades JS para responsividad y componentes
// Aquí puedes agregar scripts para animaciones, validaciones globales, etc.
// Por ahora, solo un ejemplo de animación de fadeIn para el container

document.addEventListener("DOMContentLoaded", function() {
    var container = document.querySelector('.container');
    if (container) {
        container.style.opacity = 0;
        setTimeout(function() {
            container.style.transition = "opacity 0.7s";
            container.style.opacity = 1;
        }, 100);
    }
});
