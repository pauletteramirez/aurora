#tarea 1
def es_par(numero): 
    return numero % 2 == 0

for numero in range(1, 11):
    if es_par(numero):
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")
        
#tarea2
suma = 0 

for numero in range(1, 11):
    suma += numero

print("La suma de los primeros 10 números naturales es:", suma)

#tarea3

numero = 5 

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#tarea4

def contar_letras_a(palabra):
    contador = 0
    for letra in palabra:
        if letra == 'a':
            contador += 1
    return contador

palabra = input("Ingresa una palabra: ")
resultado = contar_letras_a(palabra)
print("El número de letras 'a' en la palabra es:", resultado)

#tarea5

mayor= 9
arr=[5,1,6,4,2,8,3,9]
for num in arr:
    if num >mayor:
        print(mayor)
print("el numero mayor es:", mayor)
print("============================")

#tarea6

for numero in range(1, 31): 
    if numero % 3 == 0:
        print(numero)

#tarea7


