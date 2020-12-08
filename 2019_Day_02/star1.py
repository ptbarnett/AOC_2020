import csv

# load opcodes
opcodes = []
with open('Day_02/opcodes.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        for elem in row:
            opcodes.append(int(elem))

# reset opcodes
opcodes[1] = 12
opcodes[2] = 2

# foprmat: opcode, pos1, pos2, output
# 1 = addition
# 2 = multiplication

# Test cases
#opcodes = [1,0,0,0,99]
#opcodes = [2,3,0,3,99]
#opcodes = [2,4,4,5,99,0]
#opcodes = [1,1,1,4,99,5,6,0,99]

i = 0
op = opcodes[i]
while op != 99:
    if opcodes[i+1] >= len(opcodes) or opcodes[i+2] >= len(opcodes) or opcodes[i+3] >= len(opcodes):
        print("Invalid opcode sequence.")
        break
    if op == 1:
        # addition
        result = opcodes[opcodes[i+1]] + opcodes[opcodes[i+2]] 
    if op == 2:
        # multiplication
        result = opcodes[opcodes[i+1]] * opcodes[opcodes[i+2]] 

    # store recult
    opcodes[opcodes[i+3]] = result

    i += 4
    op = opcodes[i]

print(opcodes[0])
print(opcodes)