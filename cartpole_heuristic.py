"""Simple hand-written policy for CartPole, not reinforcement learning."""
import gymnasium as gym

def main():
    env = gym.make("CartPole-v1", render_mode="human")
    try:
        for episode in range(3):
            observation, info = env.reset(seed=42 + episode)
            total_reward = 0
            while True:
                position, velocity, angle, angular_velocity = observation
                action = 1 if angle + 0.1 * angular_velocity > 0 else 0
                observation, reward, terminated, truncated, info = env.step(action)
                total_reward += reward
                if terminated or truncated:
                    break
            print(f"Episode {episode + 1}: reward = {total_reward}")
    finally:
        env.close()

if __name__ == "__main__":
    main()
