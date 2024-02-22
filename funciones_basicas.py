
# Ejercicios Funciones


# Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

# Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

# Ejercicio 03: Diseña una función que tome una lista de números y devuelva la suma de todos los elementos.

# Ejercicio 04: Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

# Ejercicio 05: Escribe una función que tome una cadena como entrada y devuelva la cadena invertida.

# Ejercicio 06: Crea una función que reciba una lista de palabras y devuelva una nueva lista con las palabras ordenadas alfabéticamente.

# Ejercicio 07: Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.

# Ejercicio 08: Define una función que reciba una lista de números y devuelva una nueva lista con solo los números pares.

# Ejercicio 09: Escribe una función que tome una lista de números y calcule el producto de todos los elementos.

# Ejercicio 10: Crea una función que determine si una cadena dada es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

# Nota: Todas las funciones deben estar probadas y se podrá acceder a cada una de ellas mediante un menú de opciones.

import math

# Ejercicio 01
def area_circulo(radio):
    return math.pi * radio ** 2

# Ejercicio 02
def es_par(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

# Ejercicio 03
def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

# Ejercicio 04
def maximo_tres(a, b, c):
    maximo = a
    if b > maximo:
        maximo = b
    if c > maximo:
        maximo = c
    return maximo

# Ejercicio 05
def invertir_cadena(cadena):
    invertida = ''
    for caracter in cadena:
        invertida = caracter + invertida
    return invertida

# Ejercicio 06
def ordenar_palabras(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

# Ejercicio 07
def potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

# Ejercicio 08
def solo_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

# Ejercicio 09
def producto_lista(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

# Ejercicio 10
def es_palindromo(cadena):
    return cadena == invertir_cadena(cadena)


# Función para mostrar el menú
def mostrar_menu():
    print("Menú de Opciones:")
    print("1. Calcular el área de un círculo")
    print("2. Comprobar si un número es par o impar")
    print("3. Calcular la suma de una lista de números")
    print("4. Encontrar el máximo entre tres números")
    print("5. Invertir una cadena")
    print("6. Ordenar palabras en una lista")
    print("7. Calcular la potencia de un número")
    print("8. Filtrar números pares en una lista")
    print("9. Calcular el producto de una lista de números")
    print("10. Comprobar si una cadena es un palíndromo")
    print("0. Salir")

# Función principal del programa

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1 al 10, o ingrese 0 para salir): ")
    
    if opcion == '0':
        print("¡Hasta luego!")
        break
    elif opcion == '1':
        radio = float(input("Ingresa el radio del círculo: "))
        print(f"El área del círculo es: {area_circulo(radio)}")
    elif opcion == '2':
        numero = int(input("Ingresa un número: "))
        print(es_par(numero))
    elif opcion == '3':
        lista = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
        print(f"La suma de la lista es: {suma_lista(lista)}")
    elif opcion == '4':
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        c = float(input("Ingresa el tercer número: "))
        print(f"El máximo entre los tres números es: {maximo_tres(a, b, c)}")
    elif opcion == '5':
        cadena = input("Ingresa una cadena: ")
        print(f"Cadena invertida: {invertir_cadena(cadena)}")
    elif opcion == '6':
        palabras = input("Ingresa una lista de palabras separadas por espacios: ").split()
        print(f"Palabras ordenadas: {ordenar_palabras(palabras)}")
    elif opcion == '7':
        base = float(input("Ingresa la base: "))
        exponente = int(input("Ingresa el exponente: "))
        print(f"{base}^{exponente} = {potencia(base, exponente)}")
    elif opcion == '8':
        lista = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
        print(f"Números pares: {solo_pares(lista)}")
    elif opcion == '9':
        lista = [int(x) for x in input("Ingresa una lista de números separados por espacios: ").split()]
        print(f"El producto de la lista es: {producto_lista(lista)}")
    elif opcion == '10':
        cadena = input("Ingresa una cadena: ")
        if es_palindromo(cadena):
            print("La cadena es un palíndromo.")
        else:
            print("La cadena no es un palíndromo.")
    else:
        print("Opción no válida. Inténtalo de nuevo.")

