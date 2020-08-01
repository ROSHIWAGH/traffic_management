from __future__ import absolute_import
from __future__ import print_function

import os
import datetime
from shutil import copyfile

from simulation_while_training import Simulation
from generator import TrafficGenerator
from memory import Memory
from model import TrainModel
from visualization import Visualization
from utils import import_train_configuration, set_sumo, set_train_path


if __name__ == "__main__":

    
    sumo_cmd = set_sumo(False, 'sumo_config.sumocfg', 5400)
    path = set_train_path('models')

    Model = TrainModel(
        num_layers=4, 
        width_layers=400, 
        batch_size=100, 
        learning_rate =0.01, 
        input_dim=80,               #num of states
        output_dim=4                #num of actions
    )

    TrafficGen = TrafficGenerator(
        5400,            #max steps
        1000      #n cars generated
    )
        
    Simulation = Simulation(
        Model,
        Memory,
        TrafficGen,
        sumo_cmd,
        gamma=0.75,            #gamma value
        max_steps=5400,        #max steps during simulation
        green_duration=10,   #green duration
        yellow_duration=4,
        num_states=60,
        num_actions=4,
        training_epochs=800
    )
    
    episode = 0
    timestamp_start = datetime.datetime.now()
    
    while episode < config['total_episodes']:
        print('\n     Episode', str(episode+1), 'of 100')
        epsilon = 1.0 - (episode / 100)  # set the epsilon for this episode according to epsilon-greedy policy
        simulation_time, training_time = Simulation.run(episode, epsilon)  # run the simulation
        print('Simulation time:', simulation_time, 's - Training time:', training_time, 's - Total:', round(simulation_time+training_time, 1), 's')
        episode += 1

    print("\n----- Start time:", timestamp_start)
    print("----- End time:", datetime.datetime.now())
    print("----- Session info saved at:", path)

    Model.save_model(path)

    
