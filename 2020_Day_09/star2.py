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

print('=== PART 1 ===')
for i in range(preamble_length, len(data)):
    if not validate(list(data[i-preamble_length:i]), data[i]):
        break
secret_number = data[i]
print(secret_number)

print('=== PART 2 ===')
found = False
for i in range(len(data)):
    values = [data[i]]
    for j in range(i+1, len(data)):
        values.append(data[j])
        if sum(values) == secret_number:
            found = True
            break
        elif sum(values) > secret_number:
            break
    if found:
        break
   
print(values, "Sum:", sum(values))
values.sort()
low = values[0]
high = values[-1]
print(f"Low: {low}, high: {high}, SUM: {low+high}")
