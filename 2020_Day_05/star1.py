
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

test_data = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

data = loadData('2020_Day_05/input.txt')
data = subIn(data, 'B', '1')
data = subIn(data, 'F', '0')
data = subIn(data, 'R', '1')
data = subIn(data, 'L', '0')
data = list(map(lambda x: int(x, base=2), data))
max_seat = max(data)
print(max_seat)