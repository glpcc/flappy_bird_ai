from typing import ChainMap
from network import Network
import math
class Controller():
    def __init__(self):
        self.networks = []

        
    def create_networks(self,num_of_networks,num_of_layers_in_between,num_neurons_per_layer,num_of_initial,num_of_final):
         for i in range(num_of_networks):
            self.networks.append(Network(num_of_initial,'initial'))
            for j in range(num_of_layers_in_between): 
                self.networks[i].add_layer(num_neurons_per_layer)
            self.networks[i].add_layer(num_of_final)


    def change_networks_neurons(self,amount_of_changeW,amount_of_changeB):
        for network in self.networks:
            network.change_neuron_wb(amount_of_changeW,amount_of_changeB)

            
    def calculate_values(self,initial_values):
        for network in self.networks:
            network.give_initial_values(initial_values)
            network.calculate_values()

    def set_networks_wb(self,wieghts,biases):
        for network in self.networks:
            network.set_neuron_wb(wieghts,biases)
        
    def show_networks_values(self):

        return [network.show_final_values() for network in self.networks]


contr = Controller()
contr.create_networks(10,1,1,1,1)
change_amount = 10
winner_w,winner_b = contr.networks[0].get_network_wb()
for i in range(50):
    contr.change_networks_neurons(change_amount,0)
    contr.networks[0].set_neuron_wb(winner_w,winner_b)
    contr.calculate_values([i+5])
    results  = contr.show_networks_values()
    results = [abs(j[0]-(i+5)*3) for j in results]
    winner_result = min(results)
    winner_index = results.index(min(results))
    winner_w,winner_b = contr.networks[winner_index].get_network_wb()
    contr.set_networks_wb(winner_w,winner_b)
    change_amount = winner_result
    print(f"the winner result was: {winner_result} with value {i+5} and change amount {change_amount}")





