"use strict";
document.addEventListener("DOMContentLoaded", function() {
    const regionSelect = document.getElementById("region");
    const form = document.getElementById("registroForm");
    const formMsg = document.getElementById("formMsg");
    const btnText = document.getElementById("btnText");
    const spinner = document.getElementById("spinner");

    // Animación de carga sutil
    form.classList.add("animate__animated", "animate__fadeIn");

    // Cargar regiones
    fetch("/api/regiones/")
        .then(res => res.json())
        .then(data => {
            regionSelect.innerHTML = '<option value="">Seleccione una región...</option>';
            data.forEach(region => {
                regionSelect.innerHTML += `<option value="${region.id}">${region.name}</option>`;
            });
        })
        .catch(() => {
            regionSelect.innerHTML = '<option value="">No se pudieron cargar las regiones</option>';
        });

    // Validación visual en tiempo real
    ["full_name", "email", "username", "region"].forEach(id => {
        const input = document.getElementById(id);
        input.addEventListener("input", () => {
            if (input.checkValidity()) {
                input.classList.remove("is-invalid");
                input.classList.add("is-valid");
            } else {
                input.classList.remove("is-valid");
                input.classList.add("is-invalid");
            }
        });
    });

    // Validar email
    function validarEmail(email) {
        return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email);
    }

    // Envío del formulario
    form.addEventListener("submit", function(e) {
        e.preventDefault();
        formMsg.textContent = "";
        let valido = true;
        ["full_name", "email", "username", "region"].forEach(id => {
            const input = document.getElementById(id);
            if (!input.value.trim() || (id === "email" && !validarEmail(input.value))) {
                input.classList.add("is-invalid");
                valido = false;
            } else {
                input.classList.remove("is-invalid");
            }
        });
        if (!valido) {
            formMsg.innerHTML = '<span class="text-danger"><i class="fa fa-times-circle"></i> Corrija los campos marcados.</span>';
            return;
        }
        btnText.textContent = "Enviando...";
        spinner.classList.remove("d-none");
        const datos = {
            full_name: form.full_name.value.trim(),
            email: form.email.value.trim(),
            username: form.username.value.trim(),
            region: form.region.value
        };
        fetch("/api/instructores/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datos)
        })
        .then(res => res.json().then(data => ({ status: res.status, data })))
        .then(({ status, data }) => {
            btnText.textContent = "Registrar";
            spinner.classList.add("d-none");
            if (status === 200 || status === 201) {
                formMsg.innerHTML = '<span class="text-success"><i class="fa fa-check-circle"></i> ¡Registro exitoso!</span>';
                setTimeout(() => { window.location.href = "/exito"; }, 1200);
            } else {
                formMsg.innerHTML = `<span class='text-danger'><i class='fa fa-times-circle'></i> ${data.mensaje || "Error al registrar."}</span>`;
                if (data.mensaje) setTimeout(() => { window.location.href = "/error?msg=" + encodeURIComponent(data.mensaje); }, 2000);
            }
        })
        .catch(() => {
            btnText.textContent = "Registrar";
            spinner.classList.add("d-none");
            formMsg.innerHTML = '<span class="text-danger"><i class="fa fa-times-circle"></i> Error de conexión.</span>';
        });
    });
});
