import pygame
from configuracion import *


def setFondoMenu(screen):
    # fondo de pantalla
    background = pygame.image.load(".//resources//menu.jpg")
    background = pygame.transform.scale(background, (ANCHO, ALTO))
    screen.blit(background, (0, 0))

def setFondoJuego(screen):
    # fondo de pantalla
    background = pygame.image.load(".//resources//elysium.png")
    background = pygame.transform.scale(background, (ANCHO, ALTO))
    screen.blit(background, (0, 0))

def getWithPart(screen):
    # stores the width of the
    # screen into a variable
    width = screen.get_width()
    widthPart = width / 12
    return widthPart


def getHeightPart(screen):
    # stores the height of the
    # screen into a variable
    height = screen.get_height()
    heightPart = height / 12
    return heightPart

#ejecuta el sonido una vez
def correctAnswerSound():
    pygame.mixer.music.load('resources/Obtain_Ring.wav')
    pygame.mixer.music.play(0)

#ejecuta el sonido una vez
def multipleCorrectSound():
    pygame.mixer.music.load('resources/Checkpoint.wav')
    pygame.mixer.music.play(0)

#ejecuta el sonido una vez
def wrongAnswerSound():
    pygame.mixer.music.load('resources/Lose_Rings.wav')
    pygame.mixer.music.play(0)

#ejecuta el sonido una vez
def deadSound():
    pygame.mixer.music.load('resources/Death.wav')
    pygame.mixer.music.play(0)

#Verifica si el puntaje ingresado le gana a alguno de los 10 mejores
def isPuntajeAlto(puntaje):
    arrayHighScores = leerPuntajes()
    nuevoPuntajeAlto = False

    for highscore in arrayHighScores:
        if(int(puntaje) > highscore[1]):
            nuevoPuntajeAlto = True
            break

    return nuevoPuntajeAlto

#Metodo que inserta el nuevo puntaje en su lugar correspondiente y elimina el 11 de la lista
def escribirPuntajes(usuario, puntaje):
    arrayHighScores = leerPuntajes()
    index = 0
    for highScore in arrayHighScores:

        if puntaje > highScore[1]:
            arrayHighScores.insert(index, [usuario, puntaje])
            break
        index = index + 1

    if len(arrayHighScores) > 10:
        arrayHighScores.pop(10)

    highscoresWrite = open('resources/highscore.txt', 'w', encoding='utf-8')

    for highscore in arrayHighScores:
        highscoresWrite.write(highscore[0] + "," + str(highscore[1]))
        highscoresWrite.write("\n")

    highscoresWrite.close()

# metodo para leer puntajes y devuelve un array de ellos
def leerPuntajes():
    arrayHighScores = []

    highscoresRead = open('resources/highscore.txt', 'r', encoding='utf-8')

    for line in highscoresRead.readlines():
        line = line.rstrip("\n")
        usuarioPuntaje = line.split(",")
        arrayHighScores.append([usuarioPuntaje[0], usuarioPuntaje[1]])

    highscoresRead.close()

    return arrayHighScores

def renderButtonArray(screen, buttonArray):
    for button in buttonArray:
        renderButton(screen, button[0], button[1], button[2], button[3], button[4])

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
    screen.blit(text, (coordX + 15, coordY))

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

def renderButtonsAndWaitForAction(screen, buttonsArray):

    while True:

        # listening click events
        buttonClicked = listenButtonEvents(buttonsArray)

        if (buttonClicked != ''):
            return buttonClicked

        renderButtonArray(screen, buttonsArray)

        # updates the frames of the game
        pygame.display.update()