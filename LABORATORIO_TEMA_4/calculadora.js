// Paso 1. Declaración de Variables
let num1 = 10; // Valor numérico asignado
let num2 = 5;  // Valor numérico asignado
let operacion = "suma"; // Operación inicial

// Paso 2. Función para realizar operaciones
function realizarOperacion(num1, num2, operacion) {
    if (operacion === "suma") {
        return num1 + num2;
    } else if (operacion === "resta") {
        return num1 - num2;
    } else if (operacion === "multiplicacion") {
        return num1 * num2;
    } else if (operacion === "division") {
        if (num2 === 0) {
            return "Error: División por cero no es permitida.";
        }
        return num1 / num2;
    } else {
        return "Error: Operación no válida.";
    }
}

// Paso 3. Validación de datos y operaciones
function validarOperacion(operacion) {
    const operacionesValidas = ["suma", "resta", "multiplicacion", "division"];
    return operacionesValidas.includes(operacion);
}

// Paso 4. Bucle para realizar múltiples operaciones
while (true) {
    // Simular entrada del usuario 
    operacion = window.prompt("Ingrese la operación a realizar (suma, resta, multiplicacion, division) o 'salir' para terminar:");

    if (operacion === "salir") {
        alert("Gracias por usar la calculadora. ¡Adiós!");
        break;
    }

    if (!validarOperacion(operacion)) {
        alert("Error: Operación no válida. Intente de nuevo.");
        continue;
    }

    num1 = parseFloat(window.prompt("Ingrese el primer número:"));
    num2 = parseFloat(window.prompt("Ingrese el segundo número:"));

    const resultado = realizarOperacion(num1, num2, operacion);
    alert(`El resultado de la ${operacion} es: ${resultado}`);
}
