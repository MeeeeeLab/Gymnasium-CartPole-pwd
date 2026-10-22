# Gymnasium CartPole — pwd

个人强化学习入门实验，使用 [Farama Foundation Gymnasium](https://github.com/Farama-Foundation/Gymnasium) 的 CartPole-v1 环境。本项目不是官方仓库的 Fork，也不是 Gymnasium 完整源码镜像。

## 运行（macOS / Python 3.10+）

```bash
git clone https://github.com/MeeeeeLab/Gymnasium-CartPole-pwd.git
cd Gymnasium-CartPole-pwd
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python cartpole_random.py
python cartpole_heuristic.py
```

- `cartpole_random.py`：随机动作基线，无窗口。
- `cartpole_heuristic.py`：手写启发式控制器，显示窗口，需要图形桌面。

**注意：这两个示例都没有进行强化学习训练。**

## 关键概念

| 概念 | CartPole-v1 |
| --- | --- |
| Observation | 小车位置、小车速度、杆角度、杆角速度（4 个数） |
| Action | 0 向左施力；1 向右施力 |
| Reward | 每步 +1 |
| Episode | 从 reset 开始，直到 terminated 或 truncated |
| terminated | 杆倾斜过大、小车越界等任务终止 |
| truncated | 达到时间限制，默认最多 500 步 |

`reset()` 返回 observation 和 info；`step(action)` 返回 observation、reward、terminated、truncated、info。

## 科研练习

1. 先运行随机策略，记录每轮奖励。
2. 运行启发式控制器，比较奖励。
3. 用相同的一组随机种子各测试至少 30 轮，报告平均奖励与标准差。当前示例使用不同 episode 种子，适合入门演示；严格比较时还需要控制动作采样的随机性。
4. 思考：手写控制器表现更好，为什么不代表它“学会”了？
5. 后续学习：状态离散化 + Q-learning → DQN → Model-Based RL。

官方参考：[CartPole 文档](https://gymnasium.farama.org/environments/classic_control/cart_pole/) · [Gymnasium 基础用法](https://gymnasium.farama.org/introduction/basic_usage/)

Gymnasium 的版权和许可证以原项目为准；本仓库只提供个人编写的使用示例。
