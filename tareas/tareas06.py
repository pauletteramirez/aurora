#ejercicio1 
# escribir funcion que tome numero como entrada y vuelta "true" si es primo
#"false" si no lo es, utilizar un bucle for para iterar sobre todos los números en el rango dado

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def suma_primos_en_rango(inicio, fin):
    suma = 0 
    for num in range(inicio, fin + 1):
        if es_primo(num):
            suma += num
    return suma
inicio = 1
fin = 353

suma_total = suma_primos_en_rango(inicio, fin)
print("la suma de todos los numeros primos en el rango {} a {} es: {}".format(inicio, fin, suma_total))

#ejercicio 2
# ingreso tres números y los almaceno en las variables numero1, numero2 y numero3

numero1 = float(input("ingrese el primero numero: "))
numero2 = float(input("ingrese el segundo numero: "))
numero3 = float(input("ingrese el tercer numero: "))

maximo = max(numero1, numero2, numero3)
print("el numero mayor es: ", maximo)

numeros = [numero1, numero2, numero3]
continuar = True

while continuar:
    nuevo_numero = input("ingrese otro numero (o 'finalizar' para terminar): ")
    
    if nuevo_numero.lower()== 'finalizar':
        continuar = False
    else:
        numeros.append(float(nuevo_numero))
        
numeros_ordenados = sorted(numeros)
print("los numeros ordenados de menor a mayor son:", numeros_ordenados)

#ejercicio 3

def contar_palabras(cadena):
    palabras = cadena.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

texto = input("Ingrese un texto aquí: ")
cantidad = contar_palabras(texto)
print("El texto tiene {} palabras.".format(cantidad))