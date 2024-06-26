#tarea 1 
cadena = "Hola mundo, Hola universo"
cadena_modificada = cadena.replace("hola", "Hola")
print(cadena_modificada)

#tarea 2
cadena = "manzana,pera,plátano,uva"
lista_de_frutas = cadena.split(",")
print(lista_de_frutas)

#tarea 3
cadena = " Hola mundo "
cadena_sin_espacios = cadena.strip()
print(cadena_sin_espacios)

#tarea 4

def procesar_texto(texto):  
    texto = texto.strip() #eliminar espacio en blanco al inicio/final
    texto = texto.lower() #convierte la cadena en minusculas
    texto = texto.replace("mundo", "universo") #reemplaza las ocurrencias
    palabras = texto.split() #dividir la cadena en palabras
    conteo_universo = palabras.count("universo")
    return palabras, conteo_universo

cadena = "En un mundo donde la tecnología domina cada aspecto de nuestra vida, es importante recordar que la verdadera esencia de la humanidad radica en la conexión con el mundo natural que nos rodea. Explorar el mundo a través de los ojos de un niño nos permite redescubrir la magia y la maravilla que a menudo pasamos por alto en nuestro día a día. Juntos, podemos crear un mundo mejor para las generaciones futuras, donde la igualdad, la compasión y el respeto por el mundo sean los pilares de nuestra sociedad."
palabras_proceadas, conteo_universo = procesar_texto(cadena)
print("palabras procesadas:", palabras_proceadas)
print("numero de veces que aparece 'universo'", conteo_universo)

#tarea 5

import re 
from collections import Counter

def normalizar_texto(parrafo):
    parrafo = parrafo.strip() #eliminar cualquier espacio en blanco adicial al inicio y al final
    parrafo = parrafo.lower() #convertir todo el texto en minusculas 
    parrafo = re.sub(r'[^\w\s]', ' ', parrafo) #reemplazar todos los signos de puntuacion por espacion 
    palabras = parrafo.split() #dividir el texto en palabras 
    frecuencia_palabras = Counter(palabras) #contar la frecuencia de cada palabra y volver un diccionario
    return frecuencia_palabras
texto = "La vida es un viaje lleno de sorpresas, desafíos y momentos inolvidables? Cada día nos ofrece la oportunidad de crecer... aprender y descubrir nuevas experiencias! A veces, el camino puede ser difícil... y lleno de obstáculos!!! Pero es importante recordar que cada desafío nos ayuda a fortalecernos??? y a alcanzar nuestras metas! No importa cuán difícil parezca el camino... Siempre hay una luz al final del túnel??? Aprovechemos cada momento. Vivamos con pasión y enfrentemos cada desafío con valentía y determinación! Así es como creamos recuerdos que perdurarán para siempre en nuestro corazón..."
frecuencia_palabras = normalizar_texto(texto)
print("Frecuencia de palabras:")
print(frecuencia_palabras)

#tarea 6

def validar_correos(lista_correos):
    correos_validos = []
    
    for correo in lista_correos:
        correo = correo.strip() #eliminar cualquier espacio en blanco al inicio y al final de cada correo
        correo = correo.lower() #convertir tododos los correos en minusculas
        if '@' in correo and '.' in correo: #verificar si cada correo tiene un formato valido
            correos_validos.append(correo)
    return correos_validos
lista_correos = ["ejemplo@dominio.com", "correo_invalido", "CORREO_Con_Espacios@gmail.com ", "otrocorreo@hotmail.com"]             
correos_validos = validar_correos(lista_correos)
print("CORREOS VALIDOS:")
print(correos_validos)