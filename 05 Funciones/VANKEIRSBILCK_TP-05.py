# EJercicio 1: Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
# range.

numeros = list(range(1, 101))
multiplos_de_4 = []
for numero in numeros:
    if numero % 4 == 0:
        multiplos_de_4.append(numero)
print("Los números del 1 al 100 que son múltiplos de 4 son:", multiplos_de_4)

# Ejercicio 2:  Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
# indexing con números negativos!

numeros = [1, 2, "a", 4, "UTN"]
print("El penúltimo elemento de la lista es:", numeros[-2])

# Ejercicio 3: Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
# ejemplo:

palabras = []
palabras.append("Hola")
palabras.append("Mundo")
palabras.append("Python")
print("La lista de palabras es:", palabras)

# Ejercicio 4: Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
# respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
# en los videos o bien investigar cómo funciona el indexing con números negativos!
# animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("La lista de animales es:", animales)

# Ejercicio 5: Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8,15,3,22,7]
# numeros.remove(max(numeros))
# print(numeros)

print(f"""
Hola mi nombre es Joaquin. Este programa toma la lista: numeros = [8,15,3,22,7].
Luego, identifica el número más grande, para ello se utiliza "max(numeros)" y elimina este número mayor de la lista
( en este ejemplo es el numero 22).
El resultado final que se muestra es la lista sin su elemento más grande: numeros = [8,15,3,7].
""")

# Ejercicio 6: Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
# pantalla los dos primeros.


numeros = list(range(10,31,5))
print("La lista de números es:", numeros)
print(f"Los primeros dos numero de la lista son: {numeros[0]} y {numeros[1]}")

# Ejercicio 7: Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.
# autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "fiesta"
autos[2] = "focus"

# Ejercicio 8: Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
# directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("La lista de dobles es:", dobles)

# Ejercicio 9: Dada la lista “compras”, cuyos elementos representan los productos comprados por
# diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
