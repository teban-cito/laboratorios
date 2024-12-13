document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const name = document.getElementById("name").value.trim();
    const reason = document.getElementById("reason").value.trim();
    const email = document.getElementById("email").value.trim();
    if (!name || !reason || !email) {
        alert("Por favor, completa todos los campos antes de enviar.");
        return;
    }
    if (!validateEmail(email)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return;
    }
    alert("Formulario enviado correctamente. ¡Gracias por tu mensaje!");
    this.reset();
});
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}