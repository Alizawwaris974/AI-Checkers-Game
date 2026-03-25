# AI Playing Checkers

An advanced AI-based checkers game on a **16x16 board** with extended mechanics and multiple AI agents. This project compares the performance of traditional game-playing algorithms (Minimax, Alpha-Beta Pruning) against modern reinforcement learning approaches (Tabular Q-Learning).

## 🎯 Project Overview

### Abstract
This project explores the development of AI agents for a custom 16x16 Checkers game with extended mechanics. Our goal was to create intelligent agents capable of competitive gameplay against both human and AI opponents. We implemented three agents—Minimax, Alpha-Beta Pruning, and Tabular Q-Learning—to compare strategic reasoning and learning efficiency. The game was developed in Python using Pygame, with a graphical interface for intuitive interaction.

**Research Goal:** Determine which algorithmic approach performs best in competitive game scenarios—greedy algorithms or reinforcement learning.

**Keywords:** Checkers AI, Minimax, Alpha-Beta Pruning, Tabular Q-Learning, Game AI, Reinforcement Learning

## 🎮 Game Modes

1. **Human vs Human** - Two human players compete on the same machine
2. **Human vs Minimax** - Human player against minimax algorithm
3. **Human vs Minimax with Alpha-Beta Pruning** - Human player against optimized minimax
4. **Human vs Q-Learning** - Human player against reinforcement learning agent
5. **Minimax with Alpha-Beta Pruning vs Q-Learning** - AI vs AI comparison mode

## 🎲 Game Board & Rules

### Board Specifications
- **Board Size:** 16x16 (expanded from standard 8x8 checkers)
- **Internal Representation:** 2D matrix tracking empty cells and pieces (red/black, regular/king)
- **Input Method:** Mouse clicks for human players; board state and algorithm decisions for AI agents
- **Output:** Visual display via Pygame, terminal logs for game statistics, timeout notifications

### Modified Moves & Special Rules

Our implementation includes innovative rule modifications that extend standard checkers gameplay:

#### 1. **Extended Move Range (1-2 Block Skips)**
- Normal pieces can move by skipping exactly 1 or 2 diagonal blocks in any direction
- Destination must be valid with no blocking pieces
- Provides more strategic flexibility compared to standard adjacent-only moves

#### 2. **Omni-Directional Movement for All Pieces**
- **Standard Rule:** Only kings can move backward
- **Modified Rule:** All pieces (regular and king) can move forward AND backward in all four diagonal directions
- Increases board control options and tactical depth

#### 3. **Accelerated King Promotion (2-Capture Rule)**
- **Standard Rule:** Pieces become kings only upon reaching the opponent's end
- **Modified Rule:** Any piece becomes a king after capturing exactly 2 enemy pieces (not necessarily in a single turn)
- The system tracks captures per piece for accurate promotion
- Encourages aggressive play and mid-game king promotions

#### 4. **Extended King Movement Range (Up to 4 Steps)**
- Kings can move or jump up to 4 diagonal blocks in any direction
- Path must be clear for regular moves, or correctly jump over opponent pieces for captures
- Significantly increases king power and end-game dynamics

#### 5. **Turn Skip After Inactivity (30-Second Timer)**
- Each player has 30 seconds per turn
- Failure to move within the time limit automatically skips the turn
- Prevents stalling and maintains game pace
- Notifications displayed when timeout occurs

## 🤖 AI Algorithms

### 1. Minimax Algorithm
- Classic game-theory approach using minimax evaluation
- Explores all possible game states within depth limit
- Evaluates positions using heuristic scoring function
- Suitable for comparing against optimized variants

### 2. Alpha-Beta Pruning (Optimized Minimax)
- Enhancement of minimax with pruning capabilities
- Eliminates branches that cannot affect final decision
- Significantly reduces computation time compared to standard minimax
- Enables deeper search within reasonable time constraints

### 3. Tabular Q-Learning (Reinforcement Learning)
- Model-free reinforcement learning approach
- Learns optimal action policies through self-play
- Stores Q-values in lookup table for state-action pairs
- Adapts strategy based on game outcomes and reward signals
- Can be trained offline before deployment

## 💻 Technical Stack

- **Language:** Python 100%
- **GUI Framework:** Pygame
- **Game Logic:** Python with NumPy for efficient board operations
- **AI Implementation:** Custom algorithms for minimax, alpha-beta pruning, and Q-learning

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Pygame library
- NumPy (optional, for enhanced board operations)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Alizawwaris974/AI-Project.git
cd AI-Project
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## 📊 Game Statistics & Output

The game provides detailed feedback through:
- **Visual Display:** Real-time board rendering with Pygame
- **Terminal Logs:** 
  - Game winner announcement
  - Number of captures by each player
  - Turn sequence and move history
- **Timeout Notifications:** Alerts when a player exceeds 30-second turn limit
- **AI Performance Metrics:** Win/loss statistics and move evaluation times

## 🎯 Research Findings

This project evaluates AI performance across multiple dimensions:
- **Strategic Depth:** How well each algorithm handles the expanded 16x16 board
- **Computational Efficiency:** Comparison of execution time (minimax vs alpha-beta pruning)
- **Learning Capability:** Q-learning agent improvement over training episodes
- **Cross-Play Performance:** Win rates in direct AI vs AI matchups

## 📝 File Structure

```
AI-Project/
├── README.md
├── main.py
├── requirements.txt
├── game/
│   ├── board.py          # 16x16 board representation
│   ├── rules.py          # Modified game rules implementation
│   ├── pieces.py         # Piece and king logic
│   └── game_state.py     # Game state management
├── ai/
│   ├── minimax.py        # Minimax algorithm
│   ├── alpha_beta.py     # Alpha-Beta pruning implementation
│   └── q_learning.py     # Q-Learning agent
├── ui/
│   ├── pygame_ui.py      # Pygame interface
│   └── game_display.py   # Board visualization
└── utils/
    ├── timer.py          # 30-second turn timer
    └── logger.py         # Game logging and statistics
```

## 🎓 Educational Value

This project serves as a comprehensive study in:
- Game theory and AI decision-making
- Minimax algorithm and tree search optimization
- Reinforcement learning applications
- Game design with extended rule sets
- Python game development with Pygame

## 📈 Future Enhancements

- Deep Q-Learning for improved AI performance
- Neural network-based evaluation functions
- Online multiplayer support
- Advanced statistics and replay system
- Agent self-play tournament mode
- Alternative board sizes and rule variants

## 📄 License

This project is open source and available for educational and research purposes.

## 👨‍💻 Author

Developed as an AI research project exploring optimal strategies in extended checkers gameplay.

---

**Note:** This is a research and educational project designed to compare algorithmic approaches in competitive game environments.