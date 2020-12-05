passes = []
with open('day5', 'r') as f:
  for line in f:
    row = int(line[0:7].replace('B', '1').replace('F', '0'), 2)
    seat = int(line[7:10].replace('R', '1').replace('L', '0'), 2)
    passes.append((row, seat))

def getid(pss):
  row, seat = pss
  return row * 8 + seat

#part 1

highest = 0
for pss in passes:
  if getid(pss) > highest:
    highest = getid(pss)

print(highest)

#part 2

ids = []
for pss in passes:
  ids.append(getid(pss))

ids.sort()
missing = set(range(min(ids), max(ids))) - set(ids)
print(missing)