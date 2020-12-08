#
# Day 1 - Total Fuel for Take-Off
#

masses = []
with open('Day_01/mass.txt', 'r') as reader:
    for line in reader.readlines():
        masses.append(int(str(line).strip('\n')))

# Test Cases:
#masses = [12]
#masses = [14]
#masses = [1969]
#masses = [100756]

fuel = 0
for mass in masses:
    fuel += mass // 3 - 2

print(fuel)


