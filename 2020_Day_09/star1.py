import re

preamble_length = 25
data = [(lambda a: int(a))(*re.findall(r'\w+', line)) for line in open('2020_Day_09/input.txt').readlines()]

def validate(values: list[int], num: int) -> bool:
    values.sort()
    for i in range(len(values)):
        pair = values.pop(i)
        if num - pair in values:
            values.append(pair)
            values.sort()
            return True
        values.append(pair)
        values.sort()
    return False

print(data[:preamble_length])
for i in range(preamble_length, len(data)):
    isValid = validate(list(data[i-preamble_length:i]), data[i])
    print(data[i], isValid)
    if not isValid:
        break





#print(f"PART 1: {sum(a <= d.count(c) <= b for a,b,c,d in data)}")