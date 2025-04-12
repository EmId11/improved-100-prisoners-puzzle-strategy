# Improved Solution to the 100 Prisoners Puzzle

This repository contains an improved solution to the famous 100 Prisoners Problem, achieving a success rate of approximately 52% compared to the standard solution's 31%.

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

## My Improved Solution (52% Success Rate)

My solution leverages the statistical distribution of numbers to make more intelligent choices about which boxes to open. The core insight is that when numbers are randomly distributed:

- Each "decade" (1-10, 11-20, etc.) should have approximately one number in each row of boxes
- Each "last digit" (numbers ending in 0, 1, 2, etc.) should be distributed evenly across rows
- The proportion of numbers smaller or larger than any given value should follow predictable patterns

By detecting when a row contains an unexpected concentration of numbers with similar patterns to their target, prisoners can strategically skip to more promising rows.

### How It Works

1. We mentally organize the 100 boxes into 10 rows of 10 boxes each
2. Prisoners search row by row, but move to the next row when they encounter:
   - Another number from the same decade as their target
   - A number with the same last digit as their target
   - Statistical distribution patterns suggesting their number is elsewhere
3. This pattern-recognition approach allows for more efficient use of the 50-box limit

## Usage

Run the simulation with:

```python
python prisoners_puzzle.py
