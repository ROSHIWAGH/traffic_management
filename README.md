# traffic_management

We are making an IoT based solution enabling vehicles to communicate each other and microcontrollers to coordinate traffic signals across the network helping to reduce traffic density.

This is a sub module of our application. In this module, we focuses on managing traffic at a single intersection. We can also deploy the same algorithm for city network containing multiple intersection, algorithm learns the traffic pattern/behaviours in the environment.
A framework where deep q learning reinforcement learning agent tries to coordinate various systems in the road network to maximise traffic efficiency 

Getting Started
We need to install the below softwares in order to run this application
1 Download Anaconda and install
2 Download SUMO and install
3 Install tensorflow and keras API
4 Install OpenCV library

Running the Algorithm
To run the algorithm, you need to run the file training_main.py by executing the following the simple commands on Anaconda prompt or any other terminal and the agent will start the training.

python training_main.py

You don't need to open the SUMO software , since everything is loaded and done in the background, if you want to see training process, as it goes, you need to set to true the parameter gui contained in the file trainin_settings.ini, keep in mind that viewing the simulation is very slow in gui as compared to background training  and you need to close SUMO-gui everytime simulation ends, which is not practical

the file training_settings.ini contains all different parameters, used by the agen in simulation, default parameters are not optimized, so a bit testing will increase performance of the agent.

when the training ends the results will be stored in "./models/model_x/" where x is increasing integer starting from 1, generated automatically. Results will include some graphs, and data used to generate the graphs, the trained neural network and copy of the .ini file where the agent settings are.


