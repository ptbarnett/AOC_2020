from functools import reduce

data = [int(line) for line in open('2020_Day_10/test1.txt', 'r').readlines()]
data.sort()
largest = max(data)
steps = largest // 3 + 1
print(data)
print(f"largest = {largest}")
print(f"steps = {steps}")

# solution is sum of 2^(count of numbers in step), for all steps

counts = []
for step in range(0, steps):
    count = 0
    valid_nums = [step*3 + 1, step*3 + 2, step*3 + 3]    
    print(valid_nums)
    for valid_num in valid_nums:
        if valid_num in data:
            count += 1
    counts.append(count)
    print(count)

# do the calc on counts
permutations = reduce(lambda a, b: a + 2^b, counts)
print(permutations)