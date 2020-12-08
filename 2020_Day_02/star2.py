def validatePwd(pos1, pos2, letter, pwd):
    isValidPos1 = False
    isValidPos2 = False
    if pwd[pos1-1] == letter:
        isValidPos1 = True
    if pwd[pos2-1] == letter:
        isValidPos2 = True
    
    if isValidPos1 and not isValidPos2:
        return True
    if not isValidPos1 and isValidPos2:
        return True
    return False

data = []
with open('2020_Day_02/input.txt', 'r') as f:
    for line in f.readlines():
        items = line.strip('\n').split(' ')
        low = int(items[0].split('-')[0])
        high = int(items[0].split('-')[1])
        letter = items[1].split(':')[0]
        pwd = items[2]
        data.append([low, high, letter, pwd])

print("Tests:")
print(f"True: {validatePwd(1,3,'a','abcde')}")
print(f"False: {validatePwd(1,3,'b','cdefg')}")
print(f"False: {validatePwd(2,9,'c','ccccccccc')}")

count = 0
for line in data:
    if validatePwd(line[0], line[1], line[2], line[3]):
        count += 1

print(f"Count of valid password: {count}")