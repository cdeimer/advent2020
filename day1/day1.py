numbers = []
with open('day1', 'r') as f:
  for line in f:
    numbers.append(int(line))

#print(numbers)

for x in numbers:
  for y in numbers:
    if (x + y == 2020):
      print(x, y)
      print(x + y)
      print(x * y)
      print()

for x in numbers:
  for y in numbers:
    for z in numbers:
      if (x + y + z == 2020):
        print(x, y, z)
        print(x + y + z)
        print(x * y * z)
        print()
