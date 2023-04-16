#Pruebas para el main
#Test to the main class
import pygame
import asyncio
from FramesPersonaje import Frames
from Texto import TextoPersonaje
#Dimensions of the window
ANCHO = 800
LARGO = 600
#Colors
NEGRO = pygame.Color(0,0,0)
ROJO = pygame.Color(255,0,0)
VERDE = pygame.Color(0,255,0)
AZUL = pygame.Color(0,0,255)
BLANCO = pygame.Color(255,255,255)
MORADO = pygame.Color(70,31,120)
#Instancias
def retratoGuerrero(sprites):
    retrato = pygame.sprite.Sprite()

    retrato.image = pygame.image.load("retratoProta1.png")
    
    retrato.rect = retrato.image.get_rect()
    retrato.rect.x = 100
    retrato.rect.y = 100

    sprites.add(retrato)
    return retrato

def retratoVampiro(sprites):
    retrato = pygame.sprite.Sprite()

    retrato.image = pygame.image.load("retratoProta2.png")
    
    retrato.rect = retrato.image.get_rect()
    retrato.rect.x = 320
    retrato.rect.y = 100

    sprites.add(retrato)
    return retrato

def retratoVikingoReforzado(sprites):
    retrato = pygame.sprite.Sprite()

    retrato.image = pygame.image.load("retratoProta3.png")
    
    retrato.rect = retrato.image.get_rect()
    retrato.rect.x = 540
    retrato.rect.y = 100

    sprites.add(retrato)
    return retrato

def cuadroSeleccion(sprites):
    cuadro = pygame.sprite.Sprite()

    cuadro.image = pygame.Surface([170,179])
    cuadro.image.fill(ROJO)

    cuadro.rect = cuadro.image.get_rect()
    cuadro.rect.x = 90
    cuadro.rect.y = 90

    sprites.add(cuadro)
    return cuadro

def moverCuadro(cuadro,contador):
    teclaPulsada = pygame.key.get_pressed()
    if(teclaPulsada[pygame.K_d] or teclaPulsada[pygame.K_RIGHT]):
        if((cuadro.rect.x<530 or cuadro.rect.x!=530) and contador==0):
            cuadro.rect.x += 220
            contador += 1
    elif(teclaPulsada[pygame.K_a] or teclaPulsada[pygame.K_LEFT]):
        if((cuadro.rect.x>90 or cuadro.rect.x!=90) and contador==0):
            cuadro.rect.x -=220
            contador+=1
    elif(contador!=0 and contador!=50):
        contador+=1
        if(contador==50):
            contador = 0
    return contador

def crearProta1(sprites):
    protagonista = pygame.sprite.Sprite()

    protagonista.spriteSheet = pygame.image.load("prota1.png").convert()

    Frames.obenerFramesDerechaProta1(protagonista)
    Frames.obtenerFramesIzquierdaProta1(protagonista)
    Frames.obtenerFramesArribaProta1(protagonista)
    Frames.obtenerFramesAbajoProta1(protagonista)

    protagonista.rect.x = 400
    protagonista.rect.y = 300

    sprites.add(protagonista)
    return protagonista

pygame.init()
textoPersonaje = pygame.font.Font(None,35)
pantalla = pygame.display.set_mode((ANCHO,LARGO))
comenzar = True
Seleccion = pygame.sprite.Group() 
cuadro = cuadroSeleccion(Seleccion)
retrato1 = retratoGuerrero(Seleccion)
retrato2 = retratoVampiro(Seleccion)
retrato3 = retratoVikingoReforzado(Seleccion)
funcionando = True
contador = 0
while funcionando:
    pantalla.fill(NEGRO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            funcionando = False

    if(comenzar==True):
        pantalla.fill(MORADO)
        Seleccion.draw(pantalla)
        contador = moverCuadro(cuadro,contador) 
        TextoPersonaje.mostrarTexto(cuadro,textoPersonaje,pantalla,BLANCO)     
    
    pygame.display.flip()

pygame.quit()