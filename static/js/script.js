document.addEventListener("DOMContentLoaded", function() {
    console.log("Página cargada");
});

// Función para iniciar sesión
function login() {
    const usuario = document.getElementById('usuario').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:3000/usuario', { // Cambia al endpoint correcto
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ usuario, password }) // Envía usuario y contraseña
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la red');
        }
        return response.json();
    })
    .then(data => {
        console.log('Inicio de sesión exitoso:', data);
        // Redireccionar o manejar la respuesta aquí
        window.location.href = '/dashboard'; // Cambia a la ruta deseada
    })
    .catch(error => {
        console.error('Hubo un problema con la solicitud:', error);
    });
}

// Función para registrar un nuevo usuario
function register() {
    const usuario = document.getElementById('usuario').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:3000/usuario', { // Cambia al endpoint correcto
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ usuario, password }) // Envía usuario y contraseña
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la red');
        }
        return response.json();
    })
    .then(data => {
        console.log('Usuario creado:', data);
        // Redireccionar o manejar la respuesta aquí
        window.location.href = '/login'; // Cambia a la ruta deseada
    })
    .catch(error => {
        console.error('Hubo un problema con la solicitud:', error);
    });
}
