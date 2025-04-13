# Improved Solution to the 100 Prisoners Puzzle

This repository contains an improved solution to the famous 100 Prisoners Problem, achieving a success rate of approximately 57% compared to the standard solution's 31%.

## The Problem

The 100 prisoners problem is a mathematical puzzle with the following setup:

- 100 prisoners are numbered from 1 to 100
- 100 boxes are numbered from 1 to 100
- Inside each box is a slip of paper with a number from 1 to 100 (randomly distributed)
- Each prisoner, one at a time, can open up to 50 boxes
- Each prisoner must find the box containing their own number
- The prisoners win freedom only if ALL prisoners find their numbers
- Prisoners cannot communicate once the search begins
- Boxes are left exactly as they were found for the next prisoner

## Standard Solution (31% Success Rate)

The standard solution to this problem involves each prisoner:
1. Opening the box with their own number
2. Opening the box with the number found inside
3. Continuing until they either find their number or open 50 boxes

This approach gives about a 31% success rate.

## My Improved Solution (57% Success Rate)

My solution leverages the statistical distribution of numbers to make more intelligent choices about which boxes to open. The core insight is that when numbers are randomly distributed, the proportion of numbers smaller or larger than any given value should follow predictable patterns.

By detecting when a row contains an unexpected distribution of numbers relative to a prisoner's target, they can strategically skip to more promising rows.

### How It Works

1. We mentally organize the 100 boxes into 10 rows of 10 boxes each
2. Prisoners search row by row, but move to the next row when they encounter:
   - Too many numbers smaller than their target (e.g., prisoner #73 finding more than 7 numbers smaller than 73)
   - Too many numbers larger than their target (e.g., prisoner #73 finding more than 3 numbers larger than 73)
   - The end of the current row
3. This distribution-based approach allows for more efficient use of the 50-box limit by focusing the search on rows where the prisoner's number is statistically more likely to be found

## Installation

You can download and run this code using any of the following methods:

### Clone the repository

```bash
git clone https://github.com/EmId11/improved-100-prisoners-puzzle-strategy.git
cd improved-100-prisoners-puzzle-strategy
```

### Run the simulation

```python
python prisoners_puzzle.py
```

## Requirements

- Python 3.x
- No external dependencies required

## Results

Based on extensive testing with millions of simulations, the distribution-based strategy consistently achieves approximately 57% success rate, compared to the standard strategy's 31% - a remarkable improvement of around 26 percentage points.

Here are the results from a simulation with 1,000,000 runs:

```
FINAL RESULTS
============================================================
Total simulations: 1000000

Strategy 1 (chain following) success rate:    31.20%
Strategy 2 (distribution analysis) success rate:  57.71%
============================================================
```

![image](https://github.com/user-attachments/assets/14bbf8e8-4e39-4b21-b825-dff875760fa9)


## How to Modify

You can change the number of simulations by modifying the `num_simulations` variable in the `main()` function.
