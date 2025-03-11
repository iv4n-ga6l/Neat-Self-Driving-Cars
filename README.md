# 🚗 Neat Cars: An AI-Driven Racing Experience

This is an project that allows users to draw a track, select a starting point, and watch as cars autonomously navigate the course while improving their driving skills. The project utilizes a genetic algorithm known as **NEAT (NeuroEvolution of Augmenting Topologies)**, which enables the cars to evolve their neural networks over time.


https://github.com/user-attachments/assets/c50fb10b-a1bb-492f-8d36-d6a186e281bf



## Key Features
- **Live Neural Network Visualization**: Observe the neural network of the best-performing car in real-time.
- **Two Track Options**:
  - **Track 1**: Infinite track with sensors.
  - **Track 2**: Finite track without sensors.

### Prerequisites
- Python 3.7.0 or higher.

### Install
```bash
pip install -r requirements.txt
```

### Run
Start the program by executing `main.py`. 

## AI Mechanics
The AI is trained using the NEAT algorithm, which evolves a basic neural network into a more complex one based on a fitness function. The car uses five sensors to detect walls and has four possible actions: turn left, turn right, accelerate, and brake. The fitness of the car is determined by the distance it drives, encouraging continuous improvement.


## Learn More
For a deeper understanding of the NEAT algorithm, refer to the [neat-python documentation](https://neat-python.readthedocs.io/en/latest/neat_overview.html) and the original [NEAT paper](https://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf).
