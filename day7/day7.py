rules = {}
with open('day7', 'r') as f:
  for line in f:
    rules[' '.join(line.strip().split(' ')[:2])] = line.strip().split(' ')[4:]

rules_1 = {}
for key, value in rules.items():
  if 'other' in value:
    rules_1[key] = []
  else:
    contents = [' '.join(x) for x in list(zip(value[1::4], value[2::4]))]
    rules_1[key] = contents

#part 1

def get_bags(source_bag, bags = []):
  for bag, contents in rules_1.items():
    if source_bag in contents:
      bags.append(bag)
      get_bags(bag, bags)
  return set(bags)

print(len(get_bags('shiny gold')))

#part 2
rules_2 = {}
for key, value in rules.items():
  if 'other' in value:
    rules_2[key] = []
  else:
    contents = list(zip(value[0::4], value[1::4], value[2::4]))
    rules_2[key] = [(int(x), y + ' ' + z) for (x, y, z) in contents]

def get_bag_count(root_bag):
  bag_count = 0
  for contents in rules_2[root_bag]:
    count, child_bag = contents
    bag_count += count * get_bag_count(child_bag) + count
  return bag_count

print(get_bag_count('shiny gold'))



