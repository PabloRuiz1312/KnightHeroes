import pygame
class Frames:
    
    def obtenerFrame(spriteSheet,x,y,ancho,largo):
        NEGRO = pygame.Color(0,0,0)
        frame = pygame.Surface([ancho,largo]).convert()

        frame.blit(spriteSheet,(0,0),(x,y,ancho,largo))

        frame.set_colorkey(NEGRO)

        return frame
    def obenerFramesDerechaProta1(protagonista):
        protagonista.FramesDerecha = []
        frame = Frames.obtenerFrame(protagonista.spriteSheet,0,94.5,32,47.25)

        protagonista.FramesDerecha.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,32,94.5,32,47.25)

        protagonista.FramesDerecha.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,64,94.5,32,47.25)

        protagonista.FramesDerecha.append(frame)
    
    def obtenerFramesIzquierdaProta1(protagonista):
        protagonista.FramesIzquierda = []
        frame = Frames.obtenerFrame(protagonista.spriteSheet,0,47.25,32,47.25)

        protagonista.FramesIzquierda.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,32,47.25,32,47.25)

        protagonista.FramesIzquierda.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,64,47.25,32,47.25)
    
    def obtenerFramesAbajoProta1(protagonista):
        protagonista.FramesAbajo = []
        frame = Frames.obtenerFrame(protagonista.spriteSheet,0,0,32,47.25)

        protagonista.FramesAbajo.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,32,0,32,47.25)

        protagonista.FramesAbajo.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,64,0,32,47.25)

        protagonista.FramesAbajo.append(frame)

        protagonista.image = protagonista.FramesAbajo[0]
        protagonista.rect = protagonista.image.get_rect()
    
    def obtenerFramesArribaProta1(protagonista):
        protagonista.FramesArriba = []
        frame = Frames.obtenerFrame(protagonista.spriteSheet,0,141.75,32,47.25)

        protagonista.FramesArriba.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,32,141.75,32,47.25)

        protagonista.FramesAbajo.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,64,141.75,32,47.25)

        protagonista.FramesAbajo.append(frame)

    def actualizarFrameProta1(protagonista):

        if (protagonista.velocidad_x > 0):

            frame = (protagonista.rect.x // 50) % len(protagonista.FramesDerecha)
            protagonista.image = protagonista.FramesDerecha[frame]

        elif (protagonista.velocidad_x < 0):

            frame = (protagonista.rect.x // 50) % len(protagonista.FramesIzquierda)
            protagonista.image = protagonista.FramesIzquierda[frame]

        elif (protagonista.velocidad_y > 0):
            
            frame = (protagonista.rect.y // 50) % len(protagonista.FramesAbajo)
            protagonista.image = protagonista.FramesAbajo[frame]

        elif (protagonista.velocidad_y < 0):

            frame = (protagonista.rect.y // 50) % len(protagonista.FramesArriba)
            protagonista.image = protagonista.FramesArriba[frame]