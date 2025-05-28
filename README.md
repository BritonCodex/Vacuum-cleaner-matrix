# 🧹 Vacuum Cleaner Matrix Simulation

This is a simple Python simulation of a vacuum cleaner robot operating in a 4x4 grid environment. The robot detects dirt randomly scattered across the grid and cleans it, reporting its performance at the end.

---

## 📋 Description

- The environment is represented as a 4x4 matrix (`room`), where:
  - `1` indicates a **dirty** tile
  - `0` indicates a **clean** tile
- Initially, the room starts fully dirty.
- Dirt is then **randomized** using Python’s `random.choice`.
- The robot scans the entire matrix:
  - Cleans any dirty tile (`1` becomes `0`)
  - Logs each cleaning operation
- At the end, the program prints:
  - Final room state
  - Number of tiles cleaned
  - Cleaning performance as a percentage

---

## 🧠 Key Concepts

- **Matrix representation** of an environment
- **Randomization** of dirt locations
- **Simulation of a reflex-based agent**
- **Performance metric** based on coverage

---

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Save the code to a file, for example: `vacuum_simulation.py`
3. Run it using:

```bash
python vacuum_simulation.py
