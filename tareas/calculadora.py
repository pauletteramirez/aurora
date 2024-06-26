# creamos la suma
def suma(a, b):
    return a + b 
#creamos la resta
def resta(a, b):
    return a - b 
#creamos la multiplicacion
def multiplicacion(a, b):
    return a * b
#creamos la division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"
#pidamos una operacion 
print("operaciones disponibles:")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
opcion = input("seleccione una operacion (1/2/3/4): ")
#Numeros solicitados
numero1 = float(input("ingrese numero uno: "))
numero2 = float(input("ingrese numero dos: "))
#operacion seleccionada
if opcion == '1':
    print("la suma es: ", suma(numero1, numero2))
elif opcion == '2':
    print("la resta es: ", resta(numero1, numero2))
elif opcion == '3':
    print("la multiplicacion es:", multiplicacion(numero1, numero2))
elif opcion == '4':
    print("la division es:", division(numero1, numero2))
else:
    print("opcion no valida XC")
    
    
#intento dos calculadora
operaciones = {
    '1': lambda a, b: a + b,
    '2': lambda a, b: a - b,
    '3': lambda a, b: a * b,
    '4': lambda a, b: a / b if b != 0 else "No se puede dividir por cero"
}
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = input("Seleccione una operación (1/2/3/4): ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if opcion in operaciones:
    print("El resultado es:", operaciones[opcion](num1, num2))
else:
    print("Opción no válida")