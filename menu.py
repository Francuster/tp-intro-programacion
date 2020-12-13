import pygame
from pygame.locals import *
from configuracion import *

def dibujarMenu(screen):

    # stores the width of the
    # screen into a variable
    width = screen.get_width()
    widthPart = width / 12

    # stores the height of the
    # screen into a variable
    height = screen.get_height()
    heightPart = height/12

    # fondo de pantalla
    background = pygame.image.load(".//resources//menu.jpg")
    background = pygame.transform.scale(background, (ANCHO, ALTO))

    #Array de botones a renderizar
    buttonsArray = []

    buttonsArray.append(['button 1', widthPart * 3, heightPart * 3, 140, 40])
    buttonsArray.append(['button 2', widthPart * 7, heightPart * 3, 140, 40])
    buttonsArray.append(['button 3', widthPart * 3, heightPart * 5, 140, 40])
    buttonsArray.append(['button 4', widthPart * 7, heightPart * 5, 140, 40])

    while True:

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        #listening click events
        buttonClicked = listenButtonEvents(buttonsArray)

        if(buttonClicked != ''):

            if(buttonClicked == 'button 1'):
                ##go to
                return

            if (buttonClicked == 'button 4'):
                ##go to
                return


        # fills the screen with a color
        screen.fill((60, 25, 60))


        screen.blit(background, (0, 0))

        for button in buttonsArray:
            renderButton(screen, button[0], button[1], button[2], button[3], button[4])

        # updates the frames of the game
        pygame.display.update()

def renderButton(screen, buttonText, coordX, coordY, width, height):

    # white color
    color = (255, 255, 255)

    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # defining a font
    smallfont = pygame.font.SysFont('Corbel', 35)

    # rendering a text written in
    # this font
    text = smallfont.render(buttonText, True, color)

    # if mouse is hovered on a button it
    # changes to lighter shade
    if coordX <= mouse[0] <= coordX + width and coordY <= mouse[1] <= coordY + height:
        pygame.draw.rect(screen, color_light, [coordX, coordY, width, height])

    else:
        pygame.draw.rect(screen, color_dark, [coordX, coordY, 140, 40])

    # superimposing the text onto our button
    screen.blit(text, (coordX + 10, coordY))

def listenButtonEvents(buttonsArray):
    buttonClicked = ''

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # listening click events
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button do action
            for button in buttonsArray:
                if button[1] <= mouse[0] <= button[1] + button[3] and button[2] <= mouse[1] <= button[2] + button[4]:

                    buttonClicked = button[0]
                    break;

    return buttonClicked