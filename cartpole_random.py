"""CartPole baseline: random actions (not a trained policy)."""
import gymnasium as gym

def main():
    env = gym.make("CartPole-v1")
    try:
        for episode in range(5):
            observation, info = env.reset(seed=42 + episode)
            total_reward = 0.0
            while True:
                action = env.action_space.sample()
                observation, reward, terminated, truncated, info = env.step(action)
                total_reward += reward
                if terminated or truncated:
                    break
            print(f"Episode {episode + 1}: reward = {total_reward:.0f}")
    finally:
        env.close()

if __name__ == "__main__":
    main()
