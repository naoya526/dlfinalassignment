import gymnasium as gym
import ale_py

# 明示的に ALE の環境を登録
gym.register_envs(ale_py)

env = gym.make("ALE/Breakout-v5", render_mode="human")
obs, info = env.reset()

done = False
while not done:
    obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
    done = terminated or truncated
env.close()
