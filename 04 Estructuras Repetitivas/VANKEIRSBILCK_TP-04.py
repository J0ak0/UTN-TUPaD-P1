# Ejercicio 1: Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# incluyendo ambos extremos), en orden creciente, mostrando un número por línea 

for i in range(101):
    print(i)

# Ejercicio 2: Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(numero))
print(f"La cantidad de dígitos en el número {numero} es: {cantidad_digitos}")

# Ejercicio 3: ) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = 0
for i in range(valor1 + 1, valor2):
    suma += i
print(f"La suma de los números enteros entre {valor1} y {valor2} es: {suma}")

# Ejercicio 4: Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

total = 0
numero = int(input("Ingrese un número entero (0 para salir): "))

while numero != 0:
    total = total + numero
    numero = int(input("Ingrese un número entero (0 para salir): "))

print(f"El total acumulado es: {total}")


# Ejercicio 5: Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
#Se generara un numero aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)
intentos = 0
numero_usuario = -1

print("Adivina el número entre 0 y 9")

while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("ingresa tu numero: "))
    intentos = intentos + 1 

print("Has adivinado, el número era", numero_aleatorio," y necesitaste", intentos, "intentos.")

# Ejercicio 6: Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)


# Ejercicio 7: Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(numero + 1):
    suma = suma + i
print(f"La suma de los números entre 0 y {numero} es: {suma}")

# Ejercio 8: ) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).


CANTIDAD = 10 # Definir la cantidad de números a ingresar 
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD):
    numero = int(input(f"Ingresá el número {i + 1}: "))

    # pares e impares
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    # positivos y negativos
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

print("\n")
print("Resultados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

# Ejercicio 9: Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

CANTIDAD = 10  # Definir la cantidad de números a ingresar 

suma = 0

for i in range(CANTIDAD):
    numero = int(input(f"Ingresá el número {i + 1}: "))
    suma = suma + numero

media = suma / CANTIDAD

print("\nLa media de los", CANTIDAD, "números ingresados es:", media)

