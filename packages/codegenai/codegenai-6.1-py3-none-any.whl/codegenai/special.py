pwd = """12345"""
sudoku_lb = """
import math 
import random
from tqdm import tqdm

def display(board):
    for row in board:
        print(' '.join(str(num) if num != 0 else '.' for num in row))
    print()
def fill(board):
    for i in range(9):
        choices = list(set(range(1,10)) - set(board[i]) - {0})
        random.shuffle(choices)
        for j in range(9):
            if board[i][j] == 0:
                board[i][j] = choices.pop()
def cost(board):
    conflicts = 0
    for n in range(9):
        row = board[n]
        col = [x[n] for x in board]
        conflicts += len(row) - len(set(row))
        conflicts += len(col) - len(set(col))
    for l in [0,3,6]:
        for k in [0,3,6]:
            block = []
            for i in range(0+l,3+l):
                for j in range(0+k,3+k):
                    block.append(board[i][j])
            conflicts += 9 - len(set(block))
    return conflicts
def next(board, fixed):
    neighbor = [[x for x in row] for row in board]
    i = random.randint(0,8)
    cols = [j for j in range(9) if (i,j) not in fixed]
    if len(cols) >= 2:
        j1, j2 = random.sample(cols, 2)
        neighbor[i][j1], neighbor[i][j2] = neighbor[i][j2], neighbor[i][j1]
    return neighbor
def simulated_annealing(board, initial_temp = 1.0, cooling_rate = 0.99, min_temp = 0.001):
    board = [[x for x in row] for row in board]
    fixed = [(x,y) for x in range(9) for y in range(9) if board[x][y] != 0]
    fill(board)
    current = best = board
    temp = initial_temp
    while temp > min_temp:
        neighbor = next(current,fixed)
        delta = cost(neighbor) - cost(current)
        if delta < 0:
            current = neighbor
            if cost(neighbor) < cost(best):
                best = neighbor
        else:
            if random.random() < math.exp(-delta/temp):
                current = neighbor
        temp *= cooling_rate
    return best


board =[[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

best = simulated_annealing(board)
for i in tqdm (range (1000), desc="Solving "):
    if cost(best) == 0:continue
    result = simulated_annealing(board)
    if cost(result) < cost(best):
        best = result
print(f"Sudoku ({'Best Possible State | Attacks = '+str(cost(best)) if cost(best) else 'Solved'})") 
display(best)
"""
