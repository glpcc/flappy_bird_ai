from neuron import Neuron

network = []
network = [Neuron([],0,2)]
network.append(Neuron([network[0]],1,0))
network[1].calculate_value()
print(network[1].value)
