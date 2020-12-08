file = open("/Users/Brian/Documents/Advent of Code/AOC Day 6/input.txt", "r")
raw = file.read().strip().split('\n\n')   # line by line use read().splitlines to avoid \n  if multiline use .strip().split('\n\n' and then split to access lines) 
file.close()

#raw = ['abc','a\nb\nc\n','ab\nac','a\na\na\na','b']

qlperg = []
count = 0
for x in raw :
    y = x.split()
    temp = []
    for z in y :
        temp.append(set(z))
    qlperg.append(set.union(*temp))
    count += len(qlperg[-1])

print(f"Part 1 has sum of groups individual responses of {count}")

commonql = []
count = 0
for x in raw :
    y = x.split()
    temp = []
    for z in y :
        temp.append(set(z))
    commonql.append(set.intersection(*temp))
    count += len(commonql[-1])

print(f"Part 2 has sum of groups common responses of {count}")
