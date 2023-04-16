import pygame
class TextoPersonaje:
    
    def mostrarTexto(cuadro,textoPersonaje,pantalla,BLANCO):
        titulo = "SELECCIONA TU PERSONAJE"
        colocar = textoPersonaje.render(titulo,1,BLANCO)
        pantalla.blit(colocar,(220,20))
        if(cuadro.rect.x==90):
            personaje = "Guerrero:"
            transmitir = textoPersonaje.render(personaje,1,BLANCO)
            pantalla.blit(transmitir,(340,300))
            primerMensaje = "Este personaje cuenta con 150 de vida y 20 de ataque"
            transmitir2 = textoPersonaje.render(primerMensaje,1,BLANCO)
            pantalla.blit(transmitir2,(90,340))
            segundoMensaje = "Su habilidad especial es FLECHA VENENOSA:"
            transmitir3 = textoPersonaje.render(segundoMensaje,1,BLANCO)
            pantalla.blit(transmitir3,(90,380))
            tercerMensaje = "Dispara una flecha envenenada que inflinge 10 de daño"
            transmitir4 = textoPersonaje.render(tercerMensaje,1,BLANCO)
            pantalla.blit(transmitir4,(90,420))
            cuartoMensaje = "por segundo durante 3 segundos si fuera critico hara 30"
            transmitir5 = textoPersonaje.render(cuartoMensaje,1,BLANCO)
            pantalla.blit(transmitir5,(90,460))
            quintoMensaje = "la habilidad se recarga acertando 10 tiros"
            transmitir6 = textoPersonaje.render(quintoMensaje,1,BLANCO)
            pantalla.blit(transmitir6,(90,500))
        elif(cuadro.rect.x==310):
            personaje = "Vampiro:"
            transmitir = textoPersonaje.render(personaje,1,BLANCO)
            pantalla.blit(transmitir,(340,300))
            primerMensaje = "Este personaje cuenta con 100 de vida y 30 de ataque"
            transmitir2 = textoPersonaje.render(primerMensaje,1,BLANCO)
            pantalla.blit(transmitir2,(90,340))
            segundoMensaje = "su habilidad especial es CHUPA SANGRE:"
            transmitir3 = textoPersonaje.render(segundoMensaje,1,BLANCO)
            pantalla.blit(transmitir3,(90,380))
            tercerMensaje = "muerde un area inflingiendo 50 de daño y curandose 40"
            transmitir4 = textoPersonaje.render(tercerMensaje,1,BLANCO)
            pantalla.blit(transmitir4,(90,420))
            cuartoMensaje = "de vida, si fuera critico hara 60 y se curara 50"
            transmitir5 = textoPersonaje.render(cuartoMensaje,1,BLANCO)
            pantalla.blit(transmitir5,(90,460))
            quintoMensaje = "la habilidad se recarga acertando 20 tiros"
            transmitir6 = textoPersonaje.render(quintoMensaje,1,BLANCO)
            pantalla.blit(transmitir6,(90,500))
        else:
            personaje = "Vikingo reforzado:"
            transmitir = textoPersonaje.render(personaje,1,BLANCO)
            pantalla.blit(transmitir,(340,300))
            primerMensaje = "Este personaje cuenta con 200 de vida y 15 de ataque"
            transmitir2 = textoPersonaje.render(primerMensaje,1,BLANCO)
            pantalla.blit(transmitir2,(90,340))
            segundoMensaje = "su habilidad especial es VALHALLA:"
            transmitir3 = textoPersonaje.render(segundoMensaje,1,BLANCO)
            pantalla.blit(transmitir3,(90,380))
            tercerMensaje = "pegas un pisoton que hace daño en area inflingiendo"
            transmitir4 = textoPersonaje.render(tercerMensaje,1,BLANCO)
            pantalla.blit(transmitir4,(90,420))
            cuartoMensaje = "30 de daño y volviendote invulnerable durante 5 segundos"
            transmitir5 = textoPersonaje.render(cuartoMensaje,1,BLANCO)
            pantalla.blit(transmitir5,(90,460))
            quintoMensaje = "si resultara critico haces 40 y la invulnerabilidad de 7"
            transmitir6 = textoPersonaje.render(quintoMensaje,1,BLANCO)
            pantalla.blit(transmitir6,(90,500))
            sextoMensaje = "la habilidad se recarga acertando 30 tiros"
            transmitir7 = textoPersonaje.render(sextoMensaje,1,BLANCO)
            pantalla.blit(transmitir7,(90,540))