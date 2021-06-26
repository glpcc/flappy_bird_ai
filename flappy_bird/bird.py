import pygame

class Bird():
    def __init__(self,color):
        self.score = 0
        self.color = color
        self.y = 500
        self.vel = 0
    def jump(self):
        self.vel = -1
    def update(self):
        self.vel += 0.005
        self.y += self.vel
    def draw(self,canvas):
        pygame.draw.circle(canvas,self.color,(100,self.y),50)