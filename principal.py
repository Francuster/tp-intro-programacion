#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *
from menu import *
from highscore import *


#Funcion principal
def main():


        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()


        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Cancionero...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        #Menu
        menuScreen = True

        #loop principal, siempre vuelve al menu
        while (menuScreen):
            buttonClicked = dibujarMenu(screen)
            if(buttonClicked == 'Jugar'):
                buttonClicked = mainGameRender(screen)



def mainGameRender(screen):
    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial
    artistaYcancion = []
    puntos = 0
    palabraUsuario = ""
    letra = []
    correctas = 0
    elegidos = []
    masDeUnaVuelta = False

    # elige una cancion de todas las disponibles
    azar = random.randrange(1, N + 1)
    elegidos.append(azar)  # la agrega a la lista de los ya elegidos
    archivo = open(".\\letras\\" + str(azar) + ".txt", "r", encoding='utf-8')  # abre el archivo elegido con unicode.

    # lectura del archivo y filtrado de caracteres especiales, la primer linea es el artista y cancion
    # artistaYcancion, letra = lectura(archivo, letra, artistaYcancion)
    lectura(archivo, letra, artistaYcancion)

    # elige una linea al azar y su siguiente
    lista = seleccion(letra)


    ayuda = ""
    dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)

    while segundos > fps / 1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                letraApretada = dameLetraApretada(e.key)
                palabraUsuario += letraApretada
                if e.key == K_BACKSPACE:
                    palabraUsuario = palabraUsuario[0:len(palabraUsuario) - 1]
                if e.key == K_RETURN:
                    # chequea si es correcta y suma o resta puntos
                    sumar = esCorrecta(palabraUsuario, artistaYcancion, correctas)
                    puntos += sumar

                    if sumar > 0:
                        correctas = correctas + 1
                        if (correctas > 3):
                            multipleCorrectSound()
                        else:
                            correctAnswerSound()

                    else:
                        if (correctas == 0):
                            deadSound()
                        else:
                            wrongAnswerSound()
                        correctas = 0

                    if len(elegidos) == N:
                        elegidos = []
                        masDeUnaVuelta = True

                    azar = random.randrange(1, N + 1)
                    while (azar in elegidos):
                        azar = random.randrange(1, N + 1)

                    elegidos.append(azar)

                    if masDeUnaVuelta == True:
                        ayuda = artistaYcancion[0]

                    archivo = open(".\\letras\\" + str(azar) + ".txt", "r", encoding='utf-8')
                    palabraUsuario = ""
                    # lectura del archivo y filtrado de caracteres especiales
                    artistaYcancion = []
                    letra = []
                    # artistaYcancion, letra = lectura(archivo, letra, artistaYcancion)
                    lectura(archivo, letra, artistaYcancion)

                    # elige una linea al azar y su siguiente
                    lista = seleccion(letra)

        # segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000
        segundos = TIEMPO_MAX - totaltime / 1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # Dibujar de nuevo todo
        dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda)
        pygame.display.flip()

    archivo.close()

    if isPuntajeAlto(puntos):
        print("puntaje alto")
        insertarNombreUsuario(screen, puntos)

    return waitForUserAction(screen)

    #while 1:
        # Esperar el QUIT del usuario
     #   break
      #  for e in pygame.event.get():
       #     if e.type == QUIT:
        #        pygame.quit()
         #       return



#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

