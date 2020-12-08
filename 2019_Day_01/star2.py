#
# Day 2 - Total Fuel for Take-Off Including Fuel for Fuel mass
#

def calcFuel(mass):
    fuel = (mass // 3) - 2
    return fuel + calcFuel(fuel) if (fuel > 0) else 0

masses = []
with open('Day_01/mass.txt', 'r') as reader:
    for line in reader.readlines():
        masses.append(int(str(line).strip('\n')))

fuel = 0
for mass in masses:
    fuel += calcFuel(mass)
   
print(fuel)