import re

def load_data(fname):
    with open(fname, 'r') as f:
        for item in f.read().strip().split('\n'):
            yield item

def get_outer_bag(rule_text):
    # returns text string
    return re.search(r'^(\w+\s\w+)\sbags contain',rule_text).group(1)

def get_inner_bags(rule_text):
    # returns a dict of bags & quantities
    # {'dotted black': 2, 'mirrored fuschia': 3, 'wavy aqua': 5}
    # if none then returns {}
    matches = re.findall(r'(\d)\s(\w+\s\w+)\sbag', rule_text)
    d = {}
    for match in matches:
        d[match[1]] = int(match[0])
    return d

def can_contain(rules, bag, searchbag):
    # return True or False
    count = 0
    for bag in rules[bag].keys():
        if bag == searchbag:
            count += 1
        else:
            count += can_contain(rules, bag, searchbag)
    return 1 if count>0 else 0


data = load_data('2020_Day_07/input.txt')

rules = {}
for item in data:
    rules[get_outer_bag(item)] = get_inner_bags(item)

result = 0
for outer_bag in rules.keys():
    result += can_contain(rules, outer_bag, 'shiny gold')
print(f"\nNumber of Bags that can contain a shiny gold bag: {result}")

#
# Data structure
#{
#   'pale fushsia' : {'dim tan': 5, 'dark blue': 5},
#   'drab tomato': {},
#   'dim tan': {'shinny gold': 1}
#}
