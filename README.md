
# Flappy Bird AI Agent 🐦🤖

An intelligent, self-learning agent built with **Python** and **Pygame** that masters Flappy Bird using **Reinforcement Learning (Q-Learning)**.

## 🎓 Background & Project Story
This project was developed in **2021** by **Nitay Grande** as a final project for the **High School Computer Science & AI major** (Rabin High School, Kfar Saba).

The goal was to move beyond static algorithms and explore **Machine Learning**. I wanted to see a computer "grow" and improve its performance over time through trial and error. The ultimate challenge was to reach a score of **10,000,000**, proving the agent is virtually unbeatable in its environment.

## 🛠️ Tech Stack
* **Language:** Python
* **GUI & Physics:** Pygame (Handling rendering, keyboard input, and object collisions).
* **AI Algorithm:** Q-Learning (Reinforcement Learning) based on the Bellman Equation.
* **Data Storage:** `pickle` (Used to save and load the agent's "brain" - the Q-Table).

## 🧠 The Learning Logic
The agent perceives the world through a set of **States** and receives **Rewards** for its actions.

### The State (What the bird "sees")
To make a decision, the agent tracks:
1. **Horizontal Distance** to the next pipe.
2. **Vertical Distance** to the pipe's gap.
3. **Velocity:** Crucial for understanding momentum and direction.
4. **Pipe Height Differences:** Helps the agent prepare for the next obstacle.

### The Reward System
* **+1 (Survival):** Awarded for every frame the bird stays alive.
* **-1000 (Penalty):** A heavy penalty for hitting a pipe or the ground.
* **Optimization:** For stable results, the survival reward can be set to **0**, forcing the agent to focus only on avoiding death.

## 📈 Training Insights
* **Speed Mastery:** Disabling visual rendering allows the agent to simulate games much faster than real-time.
* **The "Check Point" Advantage:** I discovered that spawning the bird at a checkpoint (slightly before where it died) is far more effective than random spawning. It forces the agent to master specific difficult sequences.
* **Results:** After dying approximately **50,000 times**, the agent learned over **300,000 unique states**.

## 🚀 How to Run & Use

1. **Install Requirements:**
   ```bash
   pip install pygame

```

2. **Run the Game:**
```bash
python main.py

```


3. **Menu Navigation:**
* Use **Arrow Keys** to move and **Enter** to select.
* Press **Esc** to go back.


4. **Training Your Own Agent:**
* In **Options**, set a name for your agent (e.g., `dreambig`).
* In the **Agent** screen:
* Press **`S`** to toggle visual rendering (Fast-Forward).
* Press **`R`** to switch training methods (Random vs. Checkpoint).
* Press **`Enter`** to save the progress.


