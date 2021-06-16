import pygame
from pygame.locals import *
from pipe import Pipe
from bird import Bird
canvas = pygame.display.set_mode((1000,1000))
pygame.init()
runnig = True
init_height = 500
pipes = []
pressed = False
for i in range(4):
    pipes.append(Pipe(500 + 300*i,init_height))
    init_height = pipes[-1].y

pj = Bird((0,255,0))


while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    canvas.fill((0,0,0))
    for i in pipes: 
        i.update()
        i.draw(canvas)
        if i.x < -50 : 
            i.restart()

    if (pygame.key.get_pressed()[K_SPACE] and not pressed):
        pj.jump()
        pressed = True
    elif not pygame.key.get_pressed()[K_SPACE]:
        pressed = False
    pj.update()

    pj.draw(canvas)

    pygame.draw.rect(canvas,(255,255,255),(0,800,1000,1000))
    pygame.display.flip()

pygame.quit()