// scripts.js
function showLogin() {
    document.getElementById('login-container').style.display = 'block';
    document.getElementById('register-container').style.display = 'none';
    document.getElementById('overlay').style.display = 'flex';
}

function showRegister() {
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('register-container').style.display = 'block';
    document.getElementById('overlay').style.display = 'flex';
}

function hideOverlay() {
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('register-container').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

function checkPasswordStrength() {
    const password = document.getElementById('reg-password').value;
    const strengthElement = document.getElementById('password-strength');
    let strength = 'Débil';
    let width = '0';
    let color = '#ffcc00'; // Amarillo por defecto

    if (password.length > 8 && /[^a-zA-Z0-9]/.test(password)) {
        strength = 'Fuerte';
        width = '100%';
        color = '#ff0000'; // Rojo para fuerte
    } else if (password.length > 5) {
        strength = 'Normal';
        width = '66%';
        color = '#00cc00'; // Verde para normal
    } else if (password.length > 0) {
        strength = 'Débil';
        width = '33%';
    }

    strengthElement.style.width = width;
    strengthElement.style.backgroundColor = color;
    strengthElement.textContent = strength; // Actualiza el texto en la barra
}

function checkPasswordsMatch() {
    const password = document.getElementById('reg-password').value;
    const passwordConfirm = document.getElementById('reg-password-confirm').value;
    const errorElement = document.getElementById('password-error');

    errorElement.textContent = password !== passwordConfirm ? 'Las contraseñas no coinciden.' : '';
}

let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', function() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
        navbar.style.top = '-60px';
    } else {
        navbar.style.top = '0';
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});
