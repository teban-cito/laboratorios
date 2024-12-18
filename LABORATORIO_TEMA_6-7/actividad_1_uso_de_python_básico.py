# -*- coding: utf-8 -*-
"""Actividad 1. Uso de Python básico.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1khRYD5-UUY8gdqGxD1hb9Nm-XHVYHxsE
"""

#Paso 1 - Escribir un programa que imprima un mensaje en la consola.

print('Buen dia! para no decir hola mundo')

#Paso 1 - Declarar variables de diferentes tipos (int, float, str) y realizar operaciones matemáticas simples.

entero = 15
decimal = 2.1
texto = "Hola a todos"

suma = entero + decimal
resta = entero - decimal
multiplicacion = entero + decimal
division = entero / decimal

print(f"\nSuma : {suma} , \nResta : {resta} , \nMultiplicacion : {multiplicacion} , \nDivision : {division}")

#Paso 1 - Concatenar cadenas de texto y utilizar funciones básicas como print() y input().

nombre = input("\nCual es su nombre? :")
mensaje = "Hola " + nombre + " Bienvenido al BootCamp de programacion!"
print(mensaje)

#Paso 2 -Crear un script que pida al usuario un número y determine si es par o impar utilizando condicionales (if, else).

numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

#Paso 2 - Implementar un bucle for para iterar sobre una lista de números e imprimir sus cuadrados

numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1):
    cuadrado = i ** 2
    print(f"El cuadrado de {i} es {cuadrado}")

#Paso 2 - Usar un bucle while para solicitar repetidamente la entrada del usuario hasta que se cumpla una condición específica.

while True:
    entrada = input("Ingrese la palabra *salir* para salir: ")
    if entrada.lower() == "salir":
        break
print(f"Has ingresado: {entrada}")

#Paso 3 - Crear una lista de elementos, como nombres de estudiantes, y mostrar cada uno utilizando un bucle.

estudiantes = ["Juan" , "Sebastian" , "Andrea" , "Harold" , "Esteban"]

for estudiante in estudiantes:
    print(estudiante)

#Paso 3 -Crear un diccionario simple que almacene información de contacto (nombre, correo) y mostrar sus claves y valores.

contactos = {
    "nombre":"Andrea" ,
    "correo":"andreapareja@abc.com"
    }
for clave, valor in contactos.items():
    print(f"{clave}: {valor}")

#Paso 3 - Implementar un script que permita al usuario agregar elementos a una lista o actualizar valores en un diccionario.
estudiantes = []
while True:

  nombre = input("Ingrese el nombre del estudiante: ")
  if nombre.lower() == "salir":
       break
  estudiantes.append(nombre)

print(estudiantes)
print(f"Has ingresado: {nombre}")

#Paso 4 - Desarrollar un programa que simule una calculadora básica, permitiendo al usuario realizar sumas, restas, multiplicaciones y divisiones.

def calculadora_basica(predefined_inputs=None):
    print("\nCalculadora Básica")
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    input_sequence = iter(predefined_inputs or [])

    def custom_input(prompt):
        if predefined_inputs is not None:
            return next(input_sequence)
        return input(prompt)

    while True:
        try:
            opcion = int(custom_input("Ingrese el número de la operación deseada (1-4): "))
            if opcion not in [1, 2, 3, 4]:
                print("Opción no válida. Intente de nuevo.")
                continue

            num1 = float(custom_input("Ingrese el primer número: "))
            num2 = float(custom_input("Ingrese el segundo número: "))

            if opcion == 4 and (num1 == 0 or num2 == 0):
                print("Error: División por cero no permitida.")
            elif opcion == 1:
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == 2:
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == 3:
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif opcion == 4:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números y opciones válidas.")

if __name__ == "__main__":
    calculadora_basica(predefined_inputs=None)

#Paso 4 -  Crear un juego de adivinanza donde el programa genere un número aleatorio y el usuario deba adivinarlo, recibiendo pistas de "mayor" o "menor" en cada intento.

import random

def juego_adivinanza(predefined_inputs=None):
    print("\nJuego de Adivinanza")
    print("El programa generará un número aleatorio entre 1 y 100.")
    print("Intenta adivinarlo!")

    numero_secreto = random.randint(1, 100)
    intentos = 0
    input_sequence = iter(predefined_inputs or [])

    def custom_input(prompt):
        if predefined_inputs is not None:
            return next(input_sequence)
        return input(prompt)

    while True:
        try:
            intento = int(custom_input("Ingresa tu número: "))
            intentos += 1

            if intento < numero_secreto:
                print("Más alto!")
            elif intento > numero_secreto:
                print("Más bajo!")
            else:
                print(f"¡Felicitaciones! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    juego_adivinanza(predefined_inputs=None)


