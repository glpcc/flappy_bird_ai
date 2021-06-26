import pygame
from pygame.locals import *
from pipe import Pipe
from bird import Bird
from neural_net.controller import Controller
import math
import random
controller = Controller()
canvas = pygame.display.set_mode((1000,1000))
pygame.init()
runnig = True
init_height = 500
pipes = []
pressed = False
for i in range(4):
    pipes.append(Pipe(500 + 300*i,init_height))
    init_height = pipes[-1].y
nearest_pipe = 0    
last_one_died = False

# Networks parameters
number_of_species = 20
number_of_layers = 2
number_of_neurons_per_layer = 3
number_of_inputs = 3
number_of_final = 1
initial_amount_of_change = 20



birds = [Bird([random.randint(0,255),random.randint(0,255),random.randint(0,255)]) for i in range(number_of_species)]
controller.create_networks(number_of_species,number_of_layers,number_of_neurons_per_layer,number_of_inputs,number_of_final)

def check_colissions(birds,pipes):
    for bird in birds:
        for pipe in pipes:
            if -50 < pipe.x - 100 < 100:
                if bird.y+50 > pipe.y+pipe.opening/2 or bird.y-50 < pipe.y-pipe.opening/2:
                    if len(birds) > 1:
                        bird_index = birds.index(bird)
                        birds.pop(bird_index) 
                        controller.networks.pop(bird_index) 
                    else:
                        return True
        if bird.y >= 950 or bird.y < 0:
            if len(birds) > 1:
                bird_index = birds.index(bird) 
                birds.pop(bird_index) 
                controller.networks.pop(bird_index) 
            else:
                return True


def give_scores():
    for i in range(len(birds)):
        birds[i].score +=1



while runnig :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    canvas.fill((0,0,0))
    for i in pipes: 
        i.update()
        i.draw(canvas)
        if i.x <  0 : 
            give_scores()
            nearest_pipe = (nearest_pipe+1)%4
            i.restart()

    # if (pygame.key.get_pressed()[K_SPACE] and not pressed):
    #     for i in birds: i.jump()
    #     pressed = True
    # elif not pygame.key.get_pressed()[K_SPACE]:
    #     pressed = False


    for i in range(len(controller.networks)):
        bird_y = birds[i].y
        distance_to_upper_pipe = math.sqrt((pipes[nearest_pipe].x - 100)**2 + ((pipes[nearest_pipe].y - 150) - bird_y)**2)
        distance_to_lower_pipe = math.sqrt((pipes[nearest_pipe].x - 100)**2 + ((pipes[nearest_pipe].y + 150) - bird_y)**2)
        controller.networks[i].give_initial_values([bird_y,distance_to_upper_pipe,distance_to_lower_pipe])
        controller.networks[i].calculate_values()
        values = controller.networks[i].show_final_values()
        if values[0] > 0.5:
            birds[i].jump()


    for i in birds: i.update()
    for i in birds: i.draw(canvas)
    last_one_died = check_colissions(birds,pipes)
    if last_one_died:
        winner_w,winner_b = controller.networks[0].get_network_wb()
        change_amount = initial_amount_of_change/((birds[0].score*3)+1)
        print(change_amount)
        controller.networks = []
        birds = []
        birds = [Bird([random.randint(0,255),random.randint(0,255),random.randint(0,255)]) for i in range(number_of_species)]
        controller.create_networks(number_of_species,number_of_layers,number_of_neurons_per_layer,number_of_inputs,number_of_final)
        controller.set_networks_wb(winner_w,winner_b)
        controller.change_networks_neurons(change_amount,change_amount)
        controller.networks[0].set_neuron_wb(winner_w,winner_b)
        pipes = []
        for i in range(4):
            pipes.append(Pipe(500 + 300*i,init_height))
            init_height = pipes[-1].y
            nearest_pipe = 0    
        last_one_died = False

    pygame.draw.rect(canvas,(255,255,255),(0,800,1000,1000))
    pygame.display.flip()


pygame.quit()