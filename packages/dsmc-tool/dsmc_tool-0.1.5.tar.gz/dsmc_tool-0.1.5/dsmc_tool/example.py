import gymnasium as gym
from gymnasium.wrappers import FlattenObservation
import pgtg
from stable_baselines3 import DQN
from dsmc_tool.evaluator import Evaluator
import dsmc_tool.property as prop

#env = gym.make("pgtg-v3")
env = gym.make("MountainCarContinuous-v0")
env = FlattenObservation(env)

model = DQN("MlpPolicy", env,verbose=1)
model.learn(total_timesteps=1000, log_interval=1)

evaluator = Evaluator(env=env, initial_episodes=100, evaluation_episodes=50)
property = prop.ReturnProperty(gamma=1)
evaluator.register_property(property)
results = evaluator.eval(model, epsilon=0.1, kappa=0.05, save_interim_results=True, relative_epsilon=True)