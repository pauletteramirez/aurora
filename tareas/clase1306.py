"""#ejercicio 1
def suma_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0: #verifica si el numero es un par
            suma += numero #suma el numero a la suma total
    return suma
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = suma_pares(numeros)
print("la suma de los numeros pares en la lista es:", resultado)

#ejercicio 2 y 3
def son_anagramas (cadena1, cadena2):
    cadena1 = cadena1.replace("", "").lower() #eliminar espacion y convertir a minusculas para hacer comparacion
    cadena2 = cadena2.replace("", "").lower()
    if len(cadena1) != len(cadena2): #verificar si las cadenas tienen la misma cantidad de caracteres
        return False 
    return sorted(cadena1) == sorted(cadena2) #ordenar los caracter de ambas cadenas y verificar si son iguales
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower() #eliminar espacios y convertir a minusculas para la comparacion
    return cadena == cadena[::-1] #verificar si la cadena es igual a su inversa
def anagrama_y_palindromo(cadena1, cadena2):
    if son_anagramas(cadena1, cadena2):
        print("Las cadenas son anagramas.")
    else:
        print("Las cadenas no son anagramas.")
    
    if es_palindromo(cadena1):
        print("La primera cadena es un palíndromo.")
    else:
        print("La primera cadena no es un palíndromo.")
    
    if es_palindromo(cadena2):
        print("La segunda cadena es un palíndromo.")
    else:
        print("La segunda cadena no es un palíndromo.")
        
cadena1 = "anagrama"
cadena2 = "marganaa"
anagrama_y_palindromo(cadena1, cadena2)"""

#ejercicio 4

def reemplazar_mayusculas_con_dolar(cadena):
    resultado = ""
    for caracter in cadena:
        if caracter.isupper():  # Verifica si el caracter es una letra mayúscula
            resultado += "$"
        else:
            resultado += caracter
    return resultado

cadena = "Jujutsu Kaisen"
resultado = reemplazar_mayusculas_con_dolar(cadena)
print(resultado)

"""#ejercicio 5 

def fibonacci_recursion(n):
    if n <= 0:
        return "Error: n debe ser un entero positivo mayor que 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
    
n = 10
print(f"El {n}-ésimo número de Fibonacci es: {fibonacci_recursion(n)}")"""