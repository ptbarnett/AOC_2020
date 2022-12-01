
import re

file = open("2020_Day_10/input.txt", "r")
raw = [(lambda a: [max(0,int(a)-3), int(a)])(*re.findall(r'\w+', line)) for line in file.readlines()]
file.close()

# syntax is [adaptor - 3, adaptor ]

maxda = max(raw, key=lambda x: x[1])[1]+3
print(f"Max Adaptor size = {maxda}")

sortedraw = sorted(raw, key = lambda x: x[1])

jolts1 = 1 # compensate for the first step
jolts2 = 0
jolts3 = 1 # compensate for the final step to the device
for x in range(0,len(sortedraw)-1) :
    if sortedraw[x][0] == maxda :
        break
    if sortedraw[x+1][0] - sortedraw[x][0] <= 1 :  jolts1 += 1
    if sortedraw[x+1][0] - sortedraw[x][0] == 2 :  jolts2 += 1
    if sortedraw[x+1][0] - sortedraw[x][0] == 3 :  jolts3 += 1
    
print(f"Part 1:  found differences of 1 = {jolts1}   2 = {jolts2} and 3 = {jolts3}  for a answer of {jolts1 * jolts3}")
