# Ejercicio 1
print("Hola Mundo")

# Ejercicio 2
nombre = input("Por favor, ingresa tu nombre:")
print(f"¡Hola {nombre}!")

# Ejercicio 3
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
radio = float(input("Ingresa el radio del círculo: "))
pi = 3.14159
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

# Ejercicio 5
segundos = int(input("Ingresa el tiempo en segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos son {horas} horas.")

# Ejercicio 6
numero = int(input("Ingresa un numero: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# Ejercicio 7
num1 = int(input("Ingresa el primer numero (Distinto de 0): "))
num2 = int(input("Ingresa el segundo numero (Distinto de 0): "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multiplicacion}")
print(f"La division es: {division}")

# Ejercicio 8
altura = float(input("Ingresa tu altura en metros: "))
peso = float(input("Ingresa tu peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc}")

# Ejercicio 9
celcius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"La temperatura en Fahrenheit es: {fahrenheit}")

# Ejercicio 10
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio}")
