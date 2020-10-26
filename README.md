# LunarLander-v2
Use DDPG to solve the LunarLander environment with a continuous action space.

## Installation

The following dependencies need to be installed:

```
pip install gym
pip install Box2D
pip install torch torchvision
pip install ipython
pip install matplotlib
pip install nose
```

## Run 

1. Go to following part of the code in lunar_lander.py

```
# Uncomment the following functions to train, test, or play

train()
test()
play(env)
```

2. Uncomment train() to train an agent, test() to simulate the agent solving the environment, and play() to play LunarLander with agent assistance.
