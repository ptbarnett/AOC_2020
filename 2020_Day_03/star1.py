
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
    print(f"Pattern width= {pattern_width}")
    for row in range(1, len(pattern), down):
        tree = 0
        col += right
        if col >= pattern_width:
            col = col - pattern_width
        if(pattern[row][col] == '#'):
            tree = 1
            count += 1
        print(f"row: {row}, col: {col}, tree: {tree}")
    return count

pattern = loadPattern('2020_Day_03/test_pattern.txt')
count = routeCount(3, 1, pattern)
print(f"Total Trees = {count}")
print()

pattern = loadPattern('2020_Day_03/input.txt')
count = routeCount(3, 1, pattern)
print(f"Total Trees = {count}")


