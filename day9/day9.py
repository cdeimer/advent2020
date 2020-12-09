import itertools

with open('day9', 'r') as f:
  data = [int(line.strip()) for line in f]

preamble = 25

def get_sums(sequence):
  return [x + y for (x, y) in list(itertools.combinations(sequence, 2))]

def get_break(data):
  for x in range(preamble, len(data)):
    if data[x] in get_sums(data[x-preamble:x]):
      continue
    else:
      return(data[x])

#part 1
number = get_break(data)
print(number)

#part 2

#algorithm adopted from https://www.geeksforgeeks.org/find-subarray-with-given-sum/
def get_sub_array_sum(data, target):
  total = data[0]
  start = 0

  i = 1
  while i <= len(data):
    while total > target and start < i - 1:
      total = total - data[start]
      start += 1

    if total == target:
      return data[start:i]
      break

    if i < len(data):
      total += data[i]
      i += 1

sub_array = get_sub_array_sum(data, number)
print(min(sub_array) + max(sub_array))