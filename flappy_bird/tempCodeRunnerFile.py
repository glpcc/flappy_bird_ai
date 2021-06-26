    if last_one_died:
        winner_w,winner_b = controller.networks[0].get_network_wb()
        change_amount = initial_amount_of_change/((birds[0].score*3)+1)
        controller.networks = []
        birds = []
        birds = [Bird([0,255,0]) for i in range(number_of_species)]
        controller.create_networks(number_of_species,number_of_layers,number_of_neurons_per_layer,number_of_inputs,number_of_final)
        controller.set_networks_wb(winner_w,winner_b)
        controller.change_networks_neurons(change_amount,change_amount)
        controller.networks[0].set_neuron_wb(winner_w,winner_b)
        last_one_died = False