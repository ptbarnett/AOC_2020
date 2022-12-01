
data = [int(line) for line in open('2020_Day_10/input.txt', 'r').readlines()]

results = [0]
i = 0
done = False

while not done:
    done = True
    picks = [i+1, i+2, i+3]
    for pick in picks:
        if pick in data:
            results.append(pick)
            done = False
    i = max(results)
        
results.append(max(results)+3)
dist = [results[i] - results[i-1] for i in range(1, len(results))]
ones = dist.count(1)
threes = dist.count(3)
answer = ones * threes

print(f"Answer: {answer}")