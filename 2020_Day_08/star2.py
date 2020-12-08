
def load_data(fname):
    with open(fname, 'r') as f:
        for line in f.read().strip().split('\n'):
            yield line

def run_program(program):
    acc_value = 0
    pc = 0
    while pc < len(program):
        if program[pc][0] == 'jmp':
            if program[pc][2] > 0:
                return False, acc_value
            program[pc][2] += 1
            pc += program[pc][1]
        elif program[pc][0] == 'acc':
            if program[pc][2] > 0:
                return False, acc_value
            program[pc][2] += 1
            acc_value += program[pc][1]
            pc += 1
        elif program[pc][0] == 'nop':
            if program[pc][2] > 0:
                return False, acc_value
            program[pc][2] += 1
            pc += 1
        else:
            pc += 1
    return True, acc_value

def reset_program(program):
    for line in program:
        line[2] = 0
    return program

def print_program(program):
    for idx, line in enumerate(program):
        print(f"Line: {idx:03d} {line}")
    print()

#data = load_data('2020_Day_08/test.txt')
data = load_data('2020_Day_08/input.txt')
program = []
for line in data:
    program.append([line.split(' ')[0], int(line.split(' ')[1]), 0])

print("=== PROGRAM ===")
print_program(program)

print("=== 1st TEST RUN ===")
result, accum = run_program(program)
print(f"Result: {result}, Accumulator: {accum}")
print()

print("=== 2nd TEST RUN ===")
program = reset_program(program)
result, accum = run_program(program)
print(f"Result: {result}, Accumulator: {accum}")
print()

print('=== NOP/JMP ===')
result = False
line_index = 0
while line_index < len(program):
    print(f"Processing line: {line_index:03d}")
    if program[line_index][0] == 'nop':
        program[line_index][0] = 'jmp'
        result, accum = run_program(program)
        if result:
            break
        program[line_index][0] = 'nop'
        program = reset_program(program)

    if program[line_index][0] == 'jmp':
        program[line_index][0] = 'nop'
        result, accum = run_program(program)
        if result:
            break
        program[line_index][0] = 'jmp'
        program = reset_program(program)
    line_index += 1

print()
print('=== SOLUTION ===')
if result:
    print(f"Found solution on line {line_index}, Accumulator = {accum}")
else:
    print('No solution')