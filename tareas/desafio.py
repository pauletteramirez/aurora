#desafio 1
contador = 1
suma = 0 

while contador <= 10:
        suma += contador 
        contador += 1

print("la suma de los numeros del 1 al 10 es :", suma)

#desafio 2
import random
numero_secreto = random.randint(1, 10)
adivinanza = None

print("adivina el numero entre 1 y 10")

while adivinanza != numero_secreto:
    adivinanza = int(input("introduce tu adivinanza: "))
    if adivinanza < numero_secreto:
        print("demasiado bajo. intentalo de nuevo")
    elif adivinanza > numero_secreto:
        print("demasiado alto. intentalo de nuevo.")
    else:
        print("felicidades adivinaste el numero correcto")
        
print("fin del juego")

#desafio 3

notas = []

print("introduce tus notas. escribe  'stop' para terminar y calcular el promedio")

while True:
    entrada = input("introduce una nota o  'stop' para terminar: ").strip()
    
    if entrada.lower() ==  'stop':
       break

    try:
        nota = float (entrada)
        notas.append(nota)
    except ValueError:
        print("entrada no valida. por favor, introduce un numro o un  'stop' para terminar")
        
if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print(f"el promedio de las notas es: {promedio:.2f}")
else:
    print("no s introdujeron notas.")
    
print("fin del programa.")

#ejercicio 4

opcion = ""

while opcion != "4":
    print("menu:")
    print("1. opcion 1")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4. salir")
    
    opcion = input("seleccione una opcion: ")
    
    if opcion == "1":
        print("ha seleccionado la opcion 1")
    elif opcion == "2":
        print("ha seleccionado la opcion 2")
    elif opcion == "3":
        print("ha seleccionado la opcion 3")
    elif opcion == "4":
        print("estas saliendo del menu")
    else:
        print("opcion no valida. seleccione una opcion correcta")
        
#ejercicio 5
    
nombre_completo = input("ingresa tu nombre: ")

nombre_sin_espacios = nombre_completo.replace(" ", "")
    
cantidad_letras = len(nombre_sin_espacios)
    
print("cantidad de letras de tu nombre es: ", cantidad_letras)
    