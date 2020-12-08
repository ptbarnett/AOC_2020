from functools  import reduce

def load_data(fname):
    # return each groups answers as a list of lists
    # no blank lists allowed so watch for '\n' which strip() to ''
    with open(fname, 'r') as f:
        for item in f.read().strip().split('\n\n'):
            yield item.split()
            
# Anyone
data = load_data('2020_Day_06/input.txt')
sum = 0
for group in data:
    sum += len(set.union(*map(set, group)))
print(f"Sum for Anyone =   {sum}")

# Everyone
data = load_data('2020_Day_06/input.txt')
sum = 0
for group in data:
    sum += len(set.intersection(*map(set, group)))
print(f"Sum for Everyone = {sum}")

####### BONUS ####################################################
# # Anyone
# data = load_data('2020_Day_06/input.txt')
# sum = 0
# for group in data:
#     sum += len(reduce(lambda a, b: a | b, (set(n) for n in group)))
# print(f"Sum for Anyone =   {sum}")

# # Everyone
# data = load_data('2020_Day_06/input.txt')
# sum = 0
# for group in data:
#     sum += len(reduce(lambda a, b: a & b, (set(n) for n in group)))
# print(f"Sum for Everyone = {sum}")


# Note the 'yield' in the load_data function is a 'generator'
# it returns the first group to the calling function
# when line 8 is run.
# When you ask for the next group, the code runs line 9
# and carries on until the yield command is run again & repeats
# The load_data function yields one group at a time until the
# input file is finished.  Keeps memmory usage low but the 
# generator is exhausted when the file is finished so you have to 
# reload it a seocnd time.

# The reduce function is used a lot in cluster computing so I
# am always looking for ways to use it, since I need the practice,
# and this was a very elegant fit.

# Oring and Anding of sets return a new set with either all elements
# or only common elements!  Very sneaky!!
