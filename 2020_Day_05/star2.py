
def loadData(fname):
    data = []
    with open(fname, 'r') as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def subIn(data, old, new):
    for i in range(len(data)):
        data[i] = data[i].replace(old, new)
    return data

def findMissing(data):
    sdata = sorted(data)
    for i in range(len(sdata)-1):
        if sdata[i+1] != sdata[i] + 1:
            return int((sdata[i] + sdata[i+1])/2)

def findRows(data):
    sdata = sorted(data)
    for i in range(len(sdata)):
        sdata[i] = sdata[i] >> 3
    return set(sdata)


test_data = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

# substitue to make it a real binary code
data = loadData('2020_Day_05/input.txt')
data = subIn(data, 'B', '1') # upper = 1
data = subIn(data, 'F', '0') # lower = 0
data = subIn(data, 'R', '1') # upper = 1
data = subIn(data, 'L', '0') # lower = 0

# convert to a number using base 2
data = list(map(lambda x: int(x, base=2), data))

# find highest seat ID
print(f"Max seat ID: {max(data)}")

# find missing seat - sort data and start at lowest number and work to highest
seat = findMissing(data)
print(f"Your seat ID: {seat}")

# just for fun lets find your seat in row & column rather than ID
row_data = findRows(data)
print(f"You are in row {seat>>3}, column {seat & 0b00000111}")
print(f"Rows start at {min(row_data)} and end at {max(row_data)}")