import pygame
from pygame.locals import *
from configuracion import *
from helpers import *
from extras import *


def insertarNombreUsuario(screen, puntos):

    # reset pantalla
    setFondoJuego(screen)


    mensaje= "Puntaje alto! Ingrese su nombre y presione ENTER"


    while True:


        palabraUsuario = ''
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
                    print(palabraUsuario)
        # render
        renderText(screen, mensaje, COLOR_LETRAS, TAMANNO_LETRA_GRANDE, 5)

        renderText(screen, palabraUsuario, COLOR_TEXTO, TAMANNO_LETRA_GRANDE, 9)

        pygame.display.flip()