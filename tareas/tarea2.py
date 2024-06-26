num = 1
fizzbuzz = num

def fizzbuzz(num):
    if num % 15 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)

for i in range(1, 101):
    if i == 24 or i == 55:
        print(i)
    else:
        print(fizzbuzz(i))
        
def verificar_edad(edad): 
    if edad >= 18:
        print("La persona es mayor de edad.")
    else: 22
print("La persona es menor de edad.")

