def validatePwd(low, high, letter, pwd):
    occur = pwd.count(letter)
    if occur < low or occur > high:
        return False
    return True

data = []
with open('2020_Day_02/input.txt', 'r') as f:
    for line in f.readlines():
        items = line.strip('\n').split(' ')
        low = int(items[0].split('-')[0])
        high = int(items[0].split('-')[1])
        letter = items[1].split(':')[0]
        pwd = items[2]
        data.append([low, high, letter, pwd])

count = 0
for line in data:
    if validatePwd(line[0], line[1], line[2], line[3]):
        count += 1

print(count)