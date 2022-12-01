
data = [list(line.strip()) for line in open('2020_Day_11/test.txt', 'r').readlines()]

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'L':
            data[i][j] = 0
        elif data[i][j] == '#':
            data[i][j] = 1
        else:
            data[i][j] = None

for row in data:
    print(row)

def adjacentSeats(i,j):
    data[i-1][j-1], data[i-1][j], data[i-1][j+1]
    data[i][j-1],   data[i][j+1]
    data[i+1][j-1], data[i+1][j], data[i+1][j+1]

    if i-1 < 0: