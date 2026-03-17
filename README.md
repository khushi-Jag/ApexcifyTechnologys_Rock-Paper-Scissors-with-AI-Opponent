# 🎮 Rock Paper Scissors — AI Opponent

[![Contributors](https://img.shields.io/github/contributors/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/network/members)
[![Stars](https://img.shields.io/github/stars/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/stargazers)
[![Issues](https://img.shields.io/github/issues/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/issues)
[![License](https://img.shields.io/github/license/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/blob/main/LICENSE)

> A **Python-based Rock Paper Scissors game** featuring an AI opponent with **adaptive move prediction** — the AI learns your patterns and predicts your next move to beat you.

🌐 **[Explore the docs »](#)**
🚀 **[View Demo](#)** · 🐛 **[Report Bug](#)** · 🌟 **[Request Feature](#)**

---

## 📌 Table of Contents

* [About The Project](#-about-the-project)
* [Key Features](#-key-features)
* [How It Works](#-how-it-works)
* [Getting Started](#-getting-started)
* [Usage](#-usage)
* [Project Structure](#-project-structure)
* [Contributing](#-contributing)
* [License](#-license)
* [Contact](#-contact)

---

## 💡 About The Project

This is not your average Rock Paper Scissors game. Instead of a purely random AI opponent, this project implements a **probability-based pattern learning system** that tracks your move transitions and predicts what you are likely to play next.

The AI starts with random choices but gradually learns your tendencies — if you tend to play **paper after rock**, the AI will notice and counter accordingly. The longer you play, the smarter the AI becomes.

---

## ✨ Key Features

* **Adaptive AI Opponent** – Learns your move patterns using transition history tracking.
* **Probability-Based Prediction** – AI predicts your next move based on what you played most after your last move.
* **Score Tracking** – Live score display across all rounds (Win / Loss / Tie).
* **AI Transparency** – Each round shows the AI's reasoning (e.g. *"AI predicted you might play 'paper' after 'rock'"*).
* **Graceful Learning Phase** – Falls back to random choice until enough data is collected.
* **Zero Dependencies** – Uses only Python's built-in `random` module.
* **Clean Terminal UI** – Simple, readable round-by-round output.

---

## 🛠 Built With

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core language |
| `random` module | Random choice generation (learning phase) |
| Dictionary-based transition matrix | Pattern learning & move prediction |

---

## 🧠 How It Works

### Transition History Matrix
The AI maintains a dictionary tracking how often you switch between moves:

```
After playing "rock", you played:
  → rock:     3 times
  → paper:    7 times  ← most frequent
  → scissors: 1 time

AI Prediction: you will play "paper" next
AI Counter:    plays "scissors" to beat it
```

### AI Decision Flow

```
User plays a move
        │
        ▼
First round? (no history)
  Yes → Random choice
        │
        ▼
Any transition data available?
  No  → Random choice (learning phase)
        │
        ▼
Find most frequent move after last user move
        │
        ▼
Play the counter move to beat the prediction
```

### AI Behavior Table

| Situation | AI Behavior |
|---|---|
| First round (no data) | Random choice |
| Learning phase (no history yet) | Random choice |
| Enough history available | Predicts your next move and counters it |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent.git
cd ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent
```

**2. Run the game**

```bash
python main.py
```

> No external packages needed — runs out of the box with standard Python.

---

## 📝 Usage

```
=================================
 Rock Paper Scissors AI Game
=================================
Type rock, paper, or scissors
Type exit to stop the game

----- Round 1 -----
Your move: rock
AI chose: scissors
AI Logic: AI used random choice (no data yet)
Result: You win this round!
Score -> You: 1 | AI: 0 | Ties: 0

----- Round 2 -----
Your move: paper
AI chose: scissors
AI Logic: AI predicted you might play 'paper' after 'rock'
Result: AI wins this round!
Score -> You: 1 | AI: 1 | Ties: 0

====== FINAL RESULT ======
You: 1
AI: 1
Ties: 0
Thanks for playing!
```

**Valid Commands:**

| Input | Action |
|---|---|
| `rock` | Play rock |
| `paper` | Play paper |
| `scissors` | Play scissors |
| `exit` or `quit` | End game and see final score |

---

## 📁 Project Structure

```
ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/
│
├── main.py       # Game logic, AI prediction engine & main loop
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes:

```bash
git commit -m "Add AmazingFeature"
```

4. Push and open a Pull Request:

```bash
git push origin feature/AmazingFeature
```

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 📫 Contact

**Khushi Jagwani**
GitHub: [https://github.com/khushi-Jag](https://github.com/khushi-Jag)

---

## 🙏 Acknowledgments

* Python Documentation
* Open Source Community ❤️
