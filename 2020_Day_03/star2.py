from functools import reduce

def loadPattern(fname):
    pattern = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            pattern.append(line.strip())
    return pattern

def routeCount(right, down, pattern):
    pattern_width = len(pattern[0])
    col = 0
    count = 0
    # range(start, stop, step)
    for row in range(down, len(pattern), down):
        col += right
        if col >= pattern_width:
            col = col - pattern_width
        if(pattern[row][col] == '#'):
            count += 1
            print(f"row index: {row-1}, col index: {col}, tree!")
    return count

#
# Test Pattern
# 
print("\n----------- TEST PATTERN -----------------")
pattern = loadPattern('2020_Day_03/test_pattern.txt')
routes = [ [1,1], [3,1], [5,1], [7,1], [1,2]]  # [right,down]
counts = []
for route in routes:
    # *route = 3, 1 as parameters to function when route = [3, 1]
    counts.append(routeCount(*route, pattern))
result = reduce(lambda a, b: a*b, counts)
print()
print(f"Counts: {counts}", end=" --> [2, 7, 3, 4, 2]\n")
print(f"Result: {result}", end=f" --> {2*7*3*4*2}\n")

#
# Real Route
#
print("\n----------- REAL PATTERN -----------------")
pattern = loadPattern('2020_Day_03/input.txt')
routes = [ [1,1], [3,1], [5,1], [7,1], [1,2]]
counts = []

for route in routes:
    counts.append(routeCount(*route, pattern))

result = reduce(lambda a, b: a*b, counts)
print(f"Counts: {counts}")
print(f"Answer: {result}")


