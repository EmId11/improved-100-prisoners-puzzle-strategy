import random

def generate_boxes():
    return random.sample(range(1, 101), 100)

def strategy1(boxes): #strategy 1 is the popular method that everyone follows to solve this puzzle
    for prisoner in range(1, 101):
        opened = set()
        current = prisoner
        for _ in range(50):
            if current == boxes[current - 1]:
                break
            opened.add(current)
            current = boxes[current - 1]
            if current in opened:
                break
        else:
            return False
    return True

def strategy2(boxes): #strategy 2 is my technique
    for prisoner in range(1, 101):
        opened_count = 0
        current_row = 0
        last_opened_in_row = [-1] * 10
        
        while opened_count < 50:
            row_start = current_row * 10
            row_end = row_start + 10
            
            for i in range(last_opened_in_row[current_row] + 1, row_end):
                opened_count += 1
                if opened_count > 50:
                    return False
                
                if boxes[i] == prisoner:
                    return True
                
                smaller_count = sum(1 for j in range(row_start, i + 1) if boxes[j] < prisoner)
                larger_count = sum(1 for j in range(row_start, i + 1) if boxes[j] > prisoner)
                
                if (boxes[i] // 10 == prisoner // 10 or
                    boxes[i] % 10 == prisoner % 10 or
                    smaller_count == prisoner // 10 or
                    larger_count == 10 - (prisoner // 10) or
                    i == row_end - 1):
                    last_opened_in_row[current_row] = i
                    break
            
            current_row = (current_row + 1) % 10
            
            if current_row == 0 and all(last_opened == 9 for last_opened in last_opened_in_row):
                return False
    
    return True

def run_simulation():
    boxes = generate_boxes()
    return strategy1(boxes), strategy2(boxes)

def main():
    num_simulations = 100
    strategy1_successes = 0
    strategy2_successes = 0

    for i in range(num_simulations):
        success1, success2 = run_simulation()
        strategy1_successes += success1
        strategy2_successes += success2
        
        print(f"Simulation {i+1}:")
        print(f"  Strategy 1 success rate: {100 if success1 else 0}%")
        print(f"  Strategy 2 success rate: {100 if success2 else 0}%")
        print()

    avg_success1 = (strategy1_successes / num_simulations) * 100
    avg_success2 = (strategy2_successes / num_simulations) * 100

    print("Final Results:")
    print(f"Strategy 1 average success rate: {avg_success1:.2f}%")
    print(f"Strategy 2 average success rate: {avg_success2:.2f}%")

if __name__ == "__main__":
    main()