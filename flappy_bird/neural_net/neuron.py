import numpy as np
import math
import sys
"""
the neuron would request to all previous neurons and calculate its value based on the formula value = tanh(weights[0]*val[0] + biases[0] + weights[1]*val[1] + biases[1] + ... )
"""
class Neuron():
    def __init__(self,prev_connections,id):
        self.id = id
        self.value = 0
        self.prev_connections = prev_connections  #this will be an array of the neurons that connect to this one
        self.weights = [0 for i in range(len(prev_connections))] #an array of the wieghts (def=1) that will multiply the values of the previous connections
        self.biases = [0 for i in range(len(prev_connections))] # the array of biases

    def change_weights_and_biases(self,weights,biases):
        if len(weights) == len(self.weights) and len(biases) == len(self.biases):
            self.weights = weights
            self.biases = biases

    def calculate_value(self):
        for i in range(len(self.prev_connections)):
            self.value += self.prev_connections[i].value*self.weights[i] + self.biases[i]
        self.value = self.value



sys.path.append(".")