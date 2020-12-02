passwords = []
with open('day2', 'r') as f:
  for line in f:
    (num, char, pw) = line.split()
    num1, num2 = num.split('-')
    passwords.append((int(num1), int(num2), char[:-1], pw))

#part 1
valid = 0
for x in passwords:
  (num1, num2, char, pw) = x
  count = pw.count(char)
  if (count >= num1 and count <= num2):
    valid += 1

print(valid)

#part 2
valid = 0
for x in passwords:
  (num1, num2, char, pw) = x
  pos1 = pw[num1 - 1]
  pos2 = pw[num2 - 1]
  if ((pos1 == char) != (pos2 == char)):
    valid += 1

print(valid)