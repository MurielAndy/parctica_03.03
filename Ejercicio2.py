import pygame  

pygame.init()  

# Creamos la ventana
ventana = pygame.display.set_mode((720, 640))  
pygame.display.set_caption("HaxBall miami 5.0")  

ball = pygame.image.load("ball.png")#crea el objeto pelota

ballrect = ball.get_rect()#obtiene hitbox de pelota

speedball = [0, 0]

# Pongo la pelota en el centro restandole el ancho del png de la bola
ballrect.move_ip((ventana.get_width()-(ball.get_width()))/2, (ventana.get_height()-(ball.get_width()))/2)


jugando = True  
while jugando:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  # Si cierra la ventana
            jugando = False  # Terminamos el bucle

    ballrect = ballrect.move(speedball)#se mueve la bola


    #se comprueba que toque los limites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speedball[0] = -speedball[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speedball[1] = -speedball[1]

    ventana.fill((150, 255, 255))  # Color de fondo
    ventana.blit(ball, ballrect) #pelota agregada
    pygame.display.flip()  # Actualizamos la pantalla
    pygame.time.Clock().tick(60)  # Limitamos a 60 FPS


pygame.quit()  # Cerramos pygame