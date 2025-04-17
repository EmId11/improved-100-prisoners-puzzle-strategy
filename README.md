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

The core insight is simple: in a random distribution across rows of equal size, the proportion of numbers smaller and larger than any given prisoner's number should approximately reflect their position in the range 1-100. For example, prisoner #73 should expect roughly 73% of randomly distributed numbers within each row to be smaller than 73, and about 27% to be larger. 

When prisoners encounter a row where this expected distribution is reached (e.g., prisoner #73 finding 7 numbers smaller than 73 or 3 numbers larger than 73 within a row of 10 boxes), they move to the next row because statistically, if the expected proportion of smaller or larger values has been found without finding their own number, it's unlikely their number will be among the remaining boxes in that row.

### How It Works

1. We mentally organize the 100 boxes into 10 rows of 10 boxes each
2. Prisoners search row by row, but move to the next row when they encounter:
   - Too many numbers smaller than their target (e.g., prisoner #73 finding more than 7 numbers smaller than 73)
   - Too many numbers larger than their target (e.g., prisoner #73 finding more than 3 numbers larger than 73)
   - The end of the current row
3. This distribution-based approach allows for more efficient use of the 50-box limit by focusing the search on rows where the prisoner's number is statistically more likely to be found

![image](https://github.com/user-attachments/assets/956e81a2-99dc-4136-a93d-50ec59d4187a)

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

Based on extensive testing with millions of simulations, the distribution-based strategy consistently achieves approximately 57% success rate, compared to the standard strategy's 31%.

Here are the results from a simulation with 1,000,000,000 runs:

```
FINAL RESULTS
============================================================
Total simulations: 1,000,000,000

Strategy 1 (chain following) success rate:    31.18%
Strategy 2 (distribution analysis) success rate:  57.68%
============================================================
```
![1_billion_simulation_runs](https://github.com/user-attachments/assets/77520471-40d1-49c5-834b-48620ea21f97)




## How to Modify

You can change the number of simulations by modifying the `num_simulations` variable in the `main()` function.
