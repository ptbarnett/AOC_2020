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
    count = 0
    for bag in rules[bag].keys():
        if bag == searchbag:
            count += 1
        else:
            count += can_contain(rules, bag, searchbag)
    return 1 if count > 0 else 0




# load data
data = load_data('2020_Day_07/input.txt')

# load rules into { 'shiny gold': {'dark plum': 2, 'pale green': 4} }
rules = {}
for item in data:
    rules[get_outer_bag(item)] = get_inner_bags(item)

# find how many bags can contain a shiny gold bag
result = 0
for outer_bag in rules.keys():
    result += can_contain(rules, outer_bag, 'shiny gold')
print(f"\nNumber of Bags that can contain a shiny gold bag: {result}")



def must_contain(rules, searchbag):
    count = 0
    print(searchbag)
    for bag_name, bag_count in rules[searchbag].items():
        print(f"{bag_name} : {bag_count}")
        count += bag_count + bag_count * must_contain(rules, bag_name)
    print(f"Return count: {count}")
    return count

data = load_data('2020_Day_07/input.txt')
rules = {}
for item in data:
    rules[get_outer_bag(item)] = get_inner_bags(item)

# find how many bags must be inside a shiny gold bag
result = 0
print(rules['shiny gold'].items())
for name, count in rules['shiny gold'].items():
    print(name, count)
    result += count + count * must_contain(rules, name)
print(f"\nNumber of Bags required inside a shiny gold bag: {result}")


