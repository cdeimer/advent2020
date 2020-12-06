from collections import defaultdict
forms = []
with open('day6', 'r') as f:
  for line in f:
    forms.append(line.strip())

#extra line at the end to not break the for loops below
forms.append('')

# part 1

group = ''
groups = []
for form in forms:
  if form:
    group += form
  else:
    groups.append(list(set(group)))
    group = ''

total = 0
for group in groups:
  total += len(group)

print(total)


# part 2

group = []
groups = []
for form in forms:
  if form:
    group.append(set(form))
  else:
    groups.append(group)
    group = []

total = 0
for group in groups:
  total += len(set.intersection(*group))

print(total)