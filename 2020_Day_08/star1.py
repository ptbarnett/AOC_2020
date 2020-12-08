
def load_data(fname):
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            yield line


data = load_data('2020_Day_08/input.txt')
program = []
for line in data:
    program.append([line.split(' ')[0], int(line.split(' ')[1]), 0])

print("=== PROGRAM ===")
for line in program:
    print(line)
print()

acc_value = 0
pc = 0
while pc < len(program):
    print(f"Line: {program[pc]}, \tAccumulator value: {acc_value}")
    if program[pc][0] == 'jmp':
        if program[pc][2] > 0:
            break
        else:
            program[pc][2] += 1
        pc += program[pc][1]
    elif program[pc][0] == 'acc':
        if program[pc][2] > 0:
            break
        else:
            program[pc][2] += 1
        acc_value += program[pc][1]
        pc += 1
    elif program[pc][0] == 'nop':
        if program[pc][2] > 0:
            break
        else:
            program[pc][2] += 1
        pc += 1
    else:
        pass

