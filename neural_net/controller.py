from network import Network

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


    def show_networks_values(self):
        for network in self.networks:
            network.show_final_values()

contr = Controller()
contr.create_networks(10,2,3,1,1)
contr.calculate_values([3])
contr.show_networks_values()
contr.change_networks_neurons(0,7)
contr.calculate_values([3])
contr.show_networks_values()
            



