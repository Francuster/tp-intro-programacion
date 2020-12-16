from configuracion import *
import random
import math
import unicodedata


def lectura(archivo, letra, artistaYcancion): #se queda solo con los oraciones de cierta longitud y filtra tildes por ej

    #leer archivo y convertir en array
    for line in archivo.readlines():
        letra.append(line.rstrip('\n'))

    #saco la primera linea del array que representa al artistaYCancion
    firstLine = letra.pop(0)

    # nombre artista, variantes y cancion dividido por ";"
    arrayArtistaCancion = firstLine.split(';')
    for artistaCan in arrayArtistaCancion:
        artistaYcancion.append(artistaCan)

    #segunda linea en adelante son lineas de la cancion. variable letra

    print(artistaYcancion)
    print(letra)
    archivo.close()

    #return (artistaYcancion, letra)

def seleccion(letra):#elige uno al azar, devuelve ese y el siguiente
    lineas = []

    # index random teniendo en cuenta que tengo que seleccionar 2 seguidos
    intRandom = random.randint(0, len(letra) - 2)
    print(intRandom)

    lineas.append(letra[intRandom])
    lineas.append(letra[intRandom + 1])

    return (lineas)

def puntos(n):
    #devuelve el puntaje, segun seguidilla
    puntosTotal = 0

    if(n > 0):
        puntosTotal = math.pow(2, n)

    else:
        puntosTotal = 0

    return puntosTotal



def esCorrecta(palabraUsuario, artistaYCancion, correctas):
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    puntosTotal = 0

    if palabraUsuario in artistaYCancion:
        correctas= correctas + 1
        puntosTotal = puntos(correctas)


    return puntosTotal


