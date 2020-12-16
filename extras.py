import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    elif key == K_KP0 or key == K_0:
        return("0")
    elif key == K_KP1 or key == K_1:
        return ("1")
    elif key == K_KP2 or key == K_2:
        return ("2")
    elif key == K_KP3 or key == K_3:
        return ("3")
    elif key == K_KP4 or key == K_4:
        return ("4")
    elif key == K_KP5 or key == K_5:
        return ("5")
    elif key == K_KP6 or key == K_6:
        return ("6")
    elif key == K_KP7 or key == K_7:
        return ("7")
    elif key == K_KP8 or key == K_8:
        return ("8")
    elif key == K_KP9 or key == K_9:
        return ("9")
    else:
        return("")


def dibujar(screen, palabraUsuario, lista, puntos, segundos, ayuda):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), TAMANNO_LETRA)

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #fondo de pantalla
    background = pygame.image.load(".//resources//elysium.png")
    background = pygame.transform.scale(background, (ANCHO, ALTO))
    screen.blit(background, (0,0))

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    #muestra el nombre
    if(ayuda != ""):
        mensajeAyuda = "Artista anterior: " + ayuda
        screen.blit(defaultFont.render(mensajeAyuda, 1, COLOR_PELI), (ANCHO//4-len(ayuda)*TAMANNO_LETRA//4,(TAMANNO_LETRA)))

    #muestra las 2 lineas

    #divido las lineas por
    renderLetras(screen, lista)



#divide y renderiza las letras de la cancion dependiendo del tamaño maximo
def renderLetras(screen, letras):
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)

    positionMultiplier = 2;
    for letra in letras:
        partes = []
        #divido en 2 el render si es muy largo
        if len(letra) > CANT_MAX_CARACTERES:
            partes = textoEnPartes(letra)
        else:
            partes.append(letra)


        for parte in partes:
            screen.blit(defaultFontGrande.render(parte, 1, COLOR_LETRAS),
                        (ANCHO // 2 - len(parte) * TAMANNO_LETRA_GRANDE // 4, (TAMANNO_LETRA_GRANDE) * positionMultiplier))

            positionMultiplier = positionMultiplier + 2

#divide al string por cantidad maxima de caracteres y devuleve un array
def textoEnPartes(letra):
    listas = []
    frase = ''

    palabras = letra.split(" ")
    for palabra in palabras:
        if len(frase) > CANT_MAX_CARACTERES:
            listas.append(frase)
            frase = ''

        frase = frase + palabra + ' '
    if frase != '':
        listas.append(frase)
    return listas
