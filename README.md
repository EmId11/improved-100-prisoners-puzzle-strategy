# Improved Solution to the 100 Prisoners Puzzle

This repository contains an improved solution to the famous 100 Prisoners Problem, achieving a success rate of approximately 58% compared to the standard solution's 31%.

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

<mark>The core insight is simple:</mark> As box numbers are randomly distribution across rows of equal size, the proportion of box numbers smaller or larger than any given number (e.g. a prisoner's number) should roughly correspond to that given number's position in the range 1-100. For example, a prisoner with number 70 would expect approximately 70% of randomly distributed box numbers in any row to be smaller than 70, and approximately 30% to be larger.
When searching a row of 10 boxes, prisoner #70 should typically find about 7 boxes with numbers smaller than 70 and 2 boxes with numbers larger. If the prisoner encounters more than the expected threshold before finding their own number, they should move to the next row. This is because exceeding the expected threshold without finding their number makes it statistically less likely that their number appears in the remaining boxes of that row. <mark>Why?</mark> Because there will be *n* fewer boxes that could contain the prisoner's number in that row, reducing the probability (where n represents the amount by which the threshold is exceeded). Starting with a fresh row offers better chances of success.


### How It Works

1. **Organize the Boxes:** Divide the 100 boxes into 10 rows of 10 boxes each. This is just a conceptual organization - we're simply treating each group of 10 boxes as a "row."
2. **Search Process:**
    * Each prisoner starts with the first row and opens boxes one by one
    * As they open boxes, they count how many numbers smaller and larger than their target they've found
3. **Moving Between Rows:**
    * A prisoner moves to the next row when any of these occurs:
        * They've found N/10 numbers smaller than their target number N (e.g., prisoner #73 finding 7 smaller numbers)
        * They've found (10 - N/10) numbers larger than their target (e.g., prisoner #73 finding 3 larger numbers)
        * They've reached the end of the current row
    * After row 10, they circle back to row 1 if they still have boxes remaining in their 50-box limit.
4. **Continuing the Search:**
    * When returning to a previously visited row, the prisoner continues from where they left off. The new starting position in each row is the position immediately after the last box they opened in that row during their previous visit.
    * They keep applying the same rules for moving between rows.
    * This process continues until either they find their number or reach the 50-box limit.
5. **Group Success:**
    * The entire group succeeds only if every prisoner finds their number within their 50-box limit
![image](https://github.com/user-attachments/assets/956e81a2-99dc-4136-a93d-50ec59d4187a)

**An example of a successful search (for a single prisoner):**
![prisoners_solution_first_scan_success](https://github.com/user-attachments/assets/52b5eda7-ff34-44ac-bffb-00e12f73b348)

**An example of a failed search (for a single prisoner):**
![prisoners_solution_failure](https://github.com/user-attachments/assets/66ed06bd-4a7a-4557-8566-04db95c535b1)

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

Based on extensive testing with 1 billion simulation runs, the distribution-based strategy achieves a 57.68% success rate.

Here are the results from a simulation with 1,000,000,000 runs:

```
FINAL RESULTS
============================================================
Total simulations: 1,000,000,000

Strategy 1 (chain following) success rate:    31.18%
Strategy 2 (distribution analysis) success rate:  57.68%
============================================================
```
![image](https://github.com/user-attachments/assets/19d0d13d-071e-4148-9740-5cae8491733b)





## How to Modify

You can change the number of simulations by modifying the `num_simulations` variable in the `main()` function.

## Get in touch!

Would love to hear your thoughts! email me aymannidriss@gmail.com


