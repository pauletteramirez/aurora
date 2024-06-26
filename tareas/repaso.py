#tarea 1
def saludar(x): 
    print(f"hola {x}, mucho gusto") 
    
saludar("pedro")
saludar("juan carlos")
saludar("mariana")

#tarea 2

def numero_primo(numero):
  if numero <= 1:
    return False
  elif numero <= 3:
    return True
  elif numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True

numero = int(input("Ingrese un número: "))

if numero_primo(numero):
  mensaje = str(numero) + " es un número primo"
  print(mensaje)
else:
  mensaje = str(numero) + " no es un número primo"
  print(mensaje)
  
#tarea 3 

