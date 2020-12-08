import re

def loadPasswords(fname):
    __doc__ = " Load password data from file & return dict. "
    passwords = []
    pwd = {}
    with open(fname, 'r') as f:
        for line in f.readlines():
            if line == '\n':
                # only '\n' indicates end of password
                passwords.append(pwd)
                pwd = {}
                continue
            for elem in line.strip().split(' '):
                pwd[elem.split(':')[0]] = elem.split(':')[1]
        # append last password in file in case there is no blank line
        passwords.append(pwd)
    return passwords

def validate_keys(pwd, keys):
    __doc__ = " Return bool. True if valid, False if not valid. "
    key_count = 0
    for key in keys:
        if key in pwd:
            key_count += 1
    if key_count == len(keys):
        return True
    return False

def validate_values(pwd):
    __doc__ = " Return bool, list. True if valid, False if not. List of invalid keys. "
    valid = True
    reason = []

    m = re.search(r'^([0-9]{4})$', pwd['byr'])
    if not m or (int(m.group(1)) < 1920 or int(m.group(1)) > 2002):
        valid = False
        reason.append('byr')

    m = re.search(r'^([0-9]{4})$', pwd['iyr'])
    if not m or (int(m.group(1)) < 2010 or int(m.group(1)) > 2020):
        valid = False
        reason.append('iyr')

    m = re.search(r'^([0-9]{4})$', pwd['eyr'])
    if not m or (int(m.group(1)) < 2020 or int(m.group(1)) > 2030):
        valid = False
        reason.append('eyr')

    m = re.search(r'^([0-9]+)([ci][nm])$', pwd['hgt'])
    if not m:
        valid = False
        reason.append('hgt')
    elif m.group(2) == 'cm' and (int(m.group(1)) < 150 or int(m.group(1)) > 193):
        valid = False
        reason.append('hgt')
    elif m.group(2) == 'in' and (int(m.group(1)) < 59 or int(m.group(1)) > 76):
        valid = False
        reason.append('hgt')

    if not re.search(r'^#[0-9a-f]{6}$', pwd['hcl']):
        valid = False
        reason.append('hcl')

    if not re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', pwd['ecl']):
        valid = False
        reason.append('ecl')

    if not re.search(r'^[0-9]{9}$', pwd['pid']):
        valid = False
        reason.append('pid')

    return valid, reason


test_pwd = {
    'byr': '2002',      # 4 digits: 1920 to 2002 inclusive
    'iyr': '2020',      # 4 digits: 2010 to 2020 inclusive
    'eyr': '2030',      # 4 digits: 2020 to 2030 inclusive
    'hgt': '76in',      # Any number of digits followed by in or cm
    'hcl': '#abc123',   # a # followed by exactly 6 characters 0-9 or a-f
    'ecl': 'blu',       # exactly one of amb, blu, brn, gry, grn, hzl, oth
    'pid': '003420632', # nine digits, each one 0-9
    'cid': '280'        # ignore it whether present or absent
}
req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  #cid not required

#
# Test a single password
#
valid_keys = validate_keys(test_pwd, req_keys)
valid, reason = validate_values(test_pwd)
print("=== TEST PASSWORD ===")
print(test_pwd)
print(f"Keys valid: {valid_keys}, Values valid: {valid}, Reason: {reason}")
print()

#
# Test all passwords
#
passwords = loadPasswords('2020_Day_04/input.txt')
valid_keys_count = 0
valid_values_count = 0
for pwd in passwords:
    if validate_keys(pwd, req_keys):
        valid_keys_count += 1
        valid, reason = validate_values(pwd)
        if valid == True:
            valid_values_count += 1
        else:
            #print(pwd); print(reason)
            pass

print("=== RESULTS ===")
print(f"Total passwords: {len(passwords)}")
print(f"Passwords with valid keys: {valid_keys_count}")
print(f"Passwords with Valid keys & values: {valid_values_count}")
