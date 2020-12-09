import re
data = [(lambda a,b,c,d: [int(a), int(b), c, d])(*re.findall(r'\w+', line)) for line in open('2020_Day_02/input.txt').readlines()]
print(f"PART 1: {sum(a <= d.count(c) <= b for a,b,c,d in data)}")
print(f"PART 2: {sum((d[a-1] == c) != (d[b-1] == c) for a,b,c,d in data)}")