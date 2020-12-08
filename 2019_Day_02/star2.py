import csv
from datetime import datetime

def  execProgram(opcodes):
    i = 0
    op = opcodes[i]
    while op != 99:
        if opcodes[i+1] >= len(opcodes) or opcodes[i+2] >= len(opcodes) or opcodes[i+3] >= len(opcodes):
            return 0
        if op == 1:
            # addition
            result = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]] 
        elif op == 2:
            # multiplication
            result = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]] 
        else:
            return 0
        # store result
        opcodes[opcodes[i+3]] = result
        i += 4
        op = opcodes[i]

    return opcodes[0]

# load opcodes
opcodes = []
with open('Day_02/opcodes.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for elem in row:
            opcodes.append(int(elem))

def pairRange(limit1, limit2):
    for i in range(limit1):
        for j in range(limit2):
            yield i, j

# save the original opcodes
original_opcodes = opcodes.copy()

t1 = datetime.now()
for noun, verb in pairRange(100,100):
    opcodes = original_opcodes.copy()
    opcodes[1] = noun
    opcodes[2] = verb
    result = execProgram(opcodes)
    if result == 19690720:
        print(noun*100 + verb)
        break

t2 = datetime.now() - t1
print(f"Elapsed time: {t2.total_seconds():.2f} seconds.")






