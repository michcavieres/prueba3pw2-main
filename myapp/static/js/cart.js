// scripts.js
document.addEventListener('DOMContentLoaded', (event) => {
    const cartBox = document.getElementById('cart-box');
    const addToCartButton = document.getElementById('add-to-cart');
    const buyMembershipButton = document.getElementById('buy-membership');
    const registrationForm = document.getElementById('registration-form');

    addToCartButton.addEventListener('click', () => {
        cartBox.classList.add('show'); // Mostrar el carrito
    });

    buyMembershipButton.addEventListener('click', () => {
        alert('¡Obtuviste tu membresía!');
        cartBox.classList.remove('show'); // Ocultar el carrito después de la compra
    });

    registrationForm.addEventListener('submit', (event) => {
        event.preventDefault();
        alert('Formulario de registro enviado');
    });
});
