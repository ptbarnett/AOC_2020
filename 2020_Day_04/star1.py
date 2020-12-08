
def loadPasswords(fname):
    passwords = []
    pwd = {}
    with open(fname, 'r') as f:
        for line in f.readlines():
            if line == '\n':
                passwords.append(pwd)
                pwd = {}
                continue
            for elem in line.strip().split(' '):
                pwd[elem.split(':')[0]] = elem.split(':')[1]
    return passwords

def validate_keys(pwd, keys):
    key_count = 0
    for key in keys:
        if key in pwd:
            key_count += 1
    if key_count == len(keys):
        return 1
    return 0

def validate_values():
    pass


req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
passwords = loadPasswords('2020_Day_04/input.txt')
print(f"Total passwords: {len(passwords)}")

count = 0
for pwd in passwords:
    count += validate_keys(pwd, req_keys)
print(f"Count of optional cid: {count}")



