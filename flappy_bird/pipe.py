import pygame
import random
import sys
class Pipe():
    def __init__(self,init_x,prev_y):
        self.y = random.randint(150,650)
        self.x = init_x
        self.width = 100
        self.opening = 300
    def update(self):
        self.x -=0.2

    def draw(self,canvas):
        pygame.draw.rect(canvas,(255,0,0),(self.x-self.width/2,0,self.width,self.y-self.opening/2))
        pygame.draw.rect(canvas,(255,0,0),(self.x-self.width/2,self.y+self.opening/2,self.width,1000-self.y))
    def restart(self):
        self.x = 1200
        self.y = random.randint(150,650)
sys.path.append(".")