
# Flappy Bird AI Agent 🐦🤖

An intelligent, self-learning agent built with **Python** and **Pygame** that masters Flappy Bird using **Reinforcement Learning (Q-Learning)**.

## 🎓 Background & Project Story
[cite_start]This project was developed in **2021** by **Nitay Grande** as a final project for the **High School Computer Science & AI major** (Rabin High School, Kfar Saba)[cite: 1, 8, 11].

[cite_start]The goal was to move beyond static algorithms and explore **Machine Learning**[cite: 21, 26]. [cite_start]I wanted to see a computer "grow" and improve its performance through trial and error[cite: 21, 147]. [cite_start]The ultimate challenge was to reach a score of **10,000,000**, proving the agent is virtually unbeatable in its environment[cite: 55, 467].

## 🛠️ Tech Stack
* [cite_start]**Language:** Python [cite: 29]
* [cite_start]**GUI & Physics:** Pygame (Handling rendering, keyboard input, and object collisions) [cite: 31, 83, 84]
* [cite_start]**AI Algorithm:** Q-Learning (Reinforcement Learning) based on the Bellman Equation [cite: 75, 187, 188]
* [cite_start]**Data Storage:** `pickle` (Used to save and load the agent's "brain" - the Q-Table) [cite: 92, 451]

## 🧠 The Learning Logic
[cite_start]The agent perceives the world through a set of **States** and receives **Rewards** for its actions[cite: 145, 146, 164].



### [cite_start]The State (What the bird "sees") [cite: 199]
To make a decision, the agent tracks:
1. [cite_start]**Horizontal Distance** to the next pipe[cite: 200].
2. [cite_start]**Vertical Distance** to the pipe's gap[cite: 201].
3. [cite_start]**Velocity:** Crucial for understanding momentum and direction[cite: 202].
4. [cite_start]**Pipe Height Differences:** Helps the agent prepare for the next obstacle when inside a pipe[cite: 209, 210].

### The Reward System
* [cite_start]**+1 (Survival):** Awarded for every frame the bird stays alive[cite: 225].
* [cite_start]**-1000 (Penalty):** A heavy penalty for hitting a pipe or the ground[cite: 226].
* [cite_start]**Optimization:** During advanced training, the survival reward can be set to **0** to force the agent to focus solely on long-term stability and avoiding death[cite: 443].

## 📈 Training Insights
* [cite_start]**Speed Mastery:** To optimize learning, I implemented an option to **disable visual rendering**, allowing the agent to simulate games much faster than real-time[cite: 457, 458].
* [cite_start]**The "Check Point" Advantage:** I discovered that spawning the bird at a checkpoint (slightly before where it died) is significantly more effective than random spawning[cite: 442]. [cite_start]It forces the agent to master specific difficult sequences, leading to faster mastery[cite: 442, 445].
* [cite_start]**Results:** After dying approximately **50,000 times**, the agent learned over **300,000 unique states** and successfully reached the 10M score mark[cite: 467, 469].

## 🚀 How to Run & Use
1. **Install Requirements:**
   ```bash
   pip install pygame

```

2. **Run the Game:**
```bash
python main.py

```


3. 
**Menu Navigation:** 


* Use **Arrow Keys** to move and **Enter** to select.
* Press **Esc** to go back.


4. **Training Your Own Agent:**
* In **Options**, set a name for your agent (e.g., `dreambig`).
* In the **Agent** screen:
* Press **`S`** to toggle visual rendering (Fast-Forward).


* Press **`R`** to switch training methods (Random vs. Checkpoint).


* Press **`Enter`** to save the progress.
