
def load_data(fname):
    with open(fname, 'r') as f:
        group = []
        for line in f:
            group.extend(list(line.strip()))
            if line == '\n':
                yield set(group)
                group = []


data = load_data('2020_Day_06/input.txt')

sum = 0
for group in data:
    sum += len(group)

print(f"Sum = {sum}")

# Note the 'yield' in the load_data function is a 'generator'
# it returns the first group to the calling function
# when line 8 is run.
# When you ask for the next group, the code runs line 9
# and carries on until the yield command is run again & repeats
# The load_data function yields one group at a time until the
# input file is finished.  Keeps memmory usage low.