# Snake-Game
This project is a console-based implementation of the classic Snake game, built in Python using fundamental data structures and functional programming principles. The game is played on a 2D grid (board), where a snake moves around, grows by eating food, and must avoid colliding with itself.


# 🐍 Python Snake Game

A console-based implementation of the classic **Snake** game built in Python. This project demonstrates fundamental programming concepts including data structures, game logic, coordinate manipulation, and modular software design.

---

##  Overview

The Snake Game is played on a 2D grid where the player controls a snake that moves around the board collecting food. Each time the snake eats food, it grows longer. The objective is to survive as long as possible while avoiding collisions with the snake's own body.

The project focuses on implementing the game's core mechanics using Python functions and lists without relying on external libraries.

---

##  Features

-  Dynamic 2D game board generation
-  Snake movement and growth mechanics
-  Food placement and consumption
-  Wrap-around movement at board boundaries
-  Self-collision detection
-  Direction updates with prevention of illegal reverse movement
-  Text-based board rendering
- Built-in doctests for function validation

---

##  Technologies Used

- Python 3
- Lists and nested lists (2D arrays)
- Functions and modular programming
- Coordinate-based movement
- Algorithmic problem solving
- Doctest unit testing

---

##  Project Structure

```
snake_game.py      # Core game logic
constants.py       # Game constants and direction values
README.md          # Project documentation
```

---

##  Core Functions

| Function | Description |
|----------|-------------|
| `make_board()` | Creates an empty game board. |
| `clear_board()` | Resets every board cell to empty. |
| `place_snake_and_food()` | Displays the snake and food on the board. |
| `board_to_string()` | Converts the board into a printable string. |
| `move_snake()` | Moves the snake and handles growth after eating food. |
| `update_direction()` | Updates movement direction while preventing reverse movement. |
| `check_self_collision()` | Detects when the snake collides with itself. |
| `would_collide_after_move()` | Predicts whether the next move results in a collision. |

---

##  Game Representation

Each board cell is represented by a single character:

| Symbol | Meaning |
|--------|---------|
| `.` | Empty cell |
| `H` | Snake head |
| `S` | Snake body |
| `F` | Food |

Example board:

```
. . . F
S H . .
S . . .
```

---

##  Example Usage

```python
board = make_board(4, 3)

snake = [[1, 1], [0, 1], [0, 2]]
food = [3, 0]

place_snake_and_food(board, snake, food)

print(board_to_string(board))
```

Output:

```
. . . F
S H . .
S . . .
```

---

##  Testing

This project uses Python's built-in **doctest** module.

Run all tests using:

```bash
python snake_game.py
```

Every function includes doctests to verify expected behavior.

---

##  Learning Objectives

This project demonstrates practical experience with:

- Python programming
- Data structures
- 2D arrays
- Coordinate systems
- State management
- Collision detection algorithms
- Functional decomposition
- Game logic implementation
- Debugging and testing

---

## Skills Demonstrated

- Python
- Algorithm Design
- Object & Data Modeling
- List Manipulation
- Problem Solving
- Modular Programming
- Software Testing
- Computational Thinking

---

