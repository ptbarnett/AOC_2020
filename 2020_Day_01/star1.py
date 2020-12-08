
def loadValues(path):
    values = []
    with open(path, 'r') as reader:
        for line in reader.readlines():
            values.append(int(str(line).strip('\n')))
    return values

def find2Values(arry, sumValue):
    for i in range(0, len(arry)-1):
        for j in range(i+1, len(arry)):
            if arry[i] + arry[j] == sumValue:
                return [arry[i], arry[j]]
    return 0

values = loadValues('2020_Day_01/input.txt')
results = find2Values(values, 2020)
print(f"Values are: {results}")
print(f"Answer is: {results[0] * results[1]}")