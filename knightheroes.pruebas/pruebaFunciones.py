#Pruebas para el main
#Test to the main class
import pygame
import asyncio
import time
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
def empezarPartida(cuadro,perso1,perso2,perso3):
   
    teclaPulsada = pygame.key.get_pressed()
    if(perso1==False):
        if(teclaPulsada[pygame.K_e]):
            if(cuadro.rect.x == 90):
                perso1 = True
            if(cuadro.rect.x == 310):
                perso2 = True
            if(cuadro.rect.x==530):
                perso3 = True
           
            
    return perso1,perso2,perso3
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
def crearProta2(sprites):
    protagonista = pygame.sprite.Sprite()

    protagonista.spriteSheet = pygame.image.load("prota2.png").convert()

    Frames.obenerFramesDerechaProta2(protagonista)
    Frames.obtenerFramesIzquierdaProta2(protagonista)
    Frames.obtenerFramesArribaProta2(protagonista)
    Frames.obtenerFramesAbajoProta2(protagonista)

    protagonista.rect.x = 400
    protagonista.rect.y = 300

    sprites.add(protagonista)
    return protagonista

def crearProta3(sprites):
    protagonista = pygame.sprite.Sprite()

    protagonista.spriteSheet = pygame.image.load("prota3.png").convert()

    Frames.obenerFramesDerechaProta3(protagonista)
    Frames.obtenerFramesIzquierdaProta3(protagonista)
    Frames.obtenerFramesArribaProta3(protagonista)
    Frames.obtenerFramesAbajoProta3(protagonista)

    protagonista.rect.x = 400
    protagonista.rect.y = 300

    sprites.add(protagonista)
    return protagonista

def gestionarMovimiento(protagonista,derecha,izquierda,abajo,arriba):
    teclaPulsada = pygame.key.get_pressed()
    if(teclaPulsada[pygame.K_d]):
        protagonista.rect.x +=1
        derecha = 1   
        izquierda = 0
        abajo = 0
        arriba = 0 
    if(teclaPulsada[pygame.K_a]):
        protagonista.rect.x-=1
        izquierda = 1
        derecha = 0
        abajo = 0
        arriba = 0
    if(teclaPulsada[pygame.K_w]):
        protagonista.rect.y -=1
        arriba = 1
        derecha = 0
        abajo = 0
        izquierda = 0
    if(teclaPulsada[pygame.K_s]):
        protagonista.rect.y +=1 
        abajo = 1
        arriba = 0
        derecha = 0
        izquierda = 0
    else:
        protagonista.rect.x += 0
        protagonista.rect.y += 0
       
    return derecha,izquierda,arriba,abajo   
pygame.init()
textoPersonaje = pygame.font.Font(None,35)
pantalla = pygame.display.set_mode((ANCHO,LARGO))
comenzar = True
perso1 = False
perso2 = False
perso3 = False
izquierda = 0
derecha = 0
abajo = 0
arriba = 0
Seleccion = pygame.sprite.Group() 
cuadro = cuadroSeleccion(Seleccion)
retrato1 = retratoGuerrero(Seleccion)
retrato2 = retratoVampiro(Seleccion)
retrato3 = retratoVikingoReforzado(Seleccion)
prota1 = pygame.sprite.Group()
guerrero = crearProta1(prota1)
prota2 = pygame.sprite.Group()
vampiro = crearProta2(prota2)
prota3 = pygame.sprite.Group()
vikingo = crearProta3(prota3)
funcionando = True
contador = 0
while funcionando:
    pantalla.fill(NEGRO)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            funcionando = False

    if(comenzar==True and (perso1==False and perso2==False and perso3==False)):
        pantalla.fill(MORADO)
        Seleccion.draw(pantalla)
        contador = moverCuadro(cuadro,contador) 
        TextoPersonaje.mostrarTexto(cuadro,textoPersonaje,pantalla,BLANCO)
        perso1,perso2,perso3 = empezarPartida(cuadro,perso1,perso2,perso3)
        print(cuadro.rect.x)
    if(perso1==True):
        prota1.draw(pantalla)
        time.sleep(0.007)
        derecha,izquierda,arriba,abajo = gestionarMovimiento(guerrero,derecha,izquierda,abajo,arriba)    
        Frames.actualizarFrameProta(guerrero,arriba,derecha,izquierda,abajo)
    if(perso2==True):
        prota2.draw(pantalla)
        time.sleep(0.007)
        derecha,izquierda,arriba,abajo = gestionarMovimiento(vampiro,derecha,izquierda,abajo,arriba)    
        Frames.actualizarFrameProta(vampiro,arriba,derecha,izquierda,abajo)
    if(perso3==True):
        prota3.draw(pantalla)
        time.sleep(0.007)
        derecha,izquierda,arriba,abajo = gestionarMovimiento(vikingo,derecha,izquierda,abajo,arriba)    
        Frames.actualizarFrameProta(vikingo,arriba,derecha,izquierda,abajo)
    pygame.display.flip()

pygame.quit()