import pygame
from pygame.locals import *
from configuracion import *
from helpers import *

def dibujarMenu(screen):


    widthPart = getWithPart(screen)

    heightPart = getHeightPart(screen)

    setFondoMenu(screen)

    #Array de botones a renderizar
    buttonsArray = []

    buttonsArray.append(['Jugar', widthPart * 3, heightPart * 3, 140, 40])
    buttonsArray.append(['Puntajes', widthPart * 7, heightPart * 3, 140, 40])

    return renderButtonsAndWaitForAction(screen, buttonsArray)
