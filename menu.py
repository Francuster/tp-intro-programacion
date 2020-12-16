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
    buttonsArray.append(['button 2', widthPart * 7, heightPart * 3, 140, 40])
    buttonsArray.append(['button 3', widthPart * 3, heightPart * 5, 140, 40])
    buttonsArray.append(['button 4', widthPart * 7, heightPart * 5, 140, 40])


    renderButtonsAndWaitForAction(screen, buttonsArray)
