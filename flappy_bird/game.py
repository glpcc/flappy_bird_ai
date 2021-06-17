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

birds = [Bird([0,255,0]) for i in range(1)]

def check_colissions(birds,pipes):
    for pipe in pipes:
        if -50 < pipe.x - 100 < 100:
            for i in range(len(birds)):
                if birds[i].y+50 > pipe.y+pipe.opening/2 or birds[i].y-50 < pipe.y-pipe.opening/2:
                    birds.pop(i) 
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
        for i in birds: i.jump()
        pressed = True
    elif not pygame.key.get_pressed()[K_SPACE]:
        pressed = False
    for i in birds: i.update()
    for i in birds: i.draw(canvas)
    check_colissions(birds,pipes)

    pygame.draw.rect(canvas,(255,255,255),(0,800,1000,1000))
    pygame.display.flip()


pygame.quit()