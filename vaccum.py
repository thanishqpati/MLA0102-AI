import random

grid = [
    ['Dirty', 'Clean', 'Dirty'],
    ['Clean', 'Dirty', 'Clean'],
    ['Dirty', 'Clean', 'Dirty']
]

pos = [0, 0]
moves = 0
cleaned = 0

def display_grid(g):
    for row in g:
        print(row)
    print()

while True:
    if grid[pos[0]][pos[1]] == 'Dirty':
        grid[pos[0]][pos[1]] = 'Clean'
        cleaned += 1
        print(f"Cleaned cell at {pos}")
    if cleaned == 9:
        break
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    dx, dy = random.choice(directions)
    new_x, new_y = pos[0] + dx, pos[1] + dy
    if 0 <= new_x < 3 and 0 <= new_y < 3:
        pos = [new_x, new_y]
        moves += 1

print("All cells are clean!")
print("Total Moves:", moves)
display_grid(grid)
