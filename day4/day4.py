from collections import defaultdict

data = []
with open('day4', 'r') as f:
  for line in f:
    data.append(line.strip())


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = defaultdict(dict)
counter = 0
for line in data:
  #print(line)
  for field in line.split(' '):
    if len(field) > 0:
      key, value = field.split(':')
      passports[counter][key] = value
    else:
      counter += 1


#part 1

result = 0
for key, passport in passports.items():
  #print(list(passport.keys()))
  if all(fields in passport for fields in required_fields):
    result += 1

print(result)

#part 2

def validate(key, value):
  if key == 'byr':
    return int(value) >= 1920 and int(value) <= 2002

  if key == 'iyr':
    return int(value) >= 2010 and int(value) <= 2020

  if key == 'eyr':
    return int(value) >= 2020 and int(value) <= 2030

  if key == 'hgt':
    if value[-2:] == 'cm':
      return int(value[:-2]) >= 150 and int(value[:-2]) <= 193
    if value[-2:] == 'in':
      return int(value[:-2]) >= 59 and int(value[:-2]) <= 76
    return False

  if key == 'hcl':
    if value[0] != '#':
      return False

    if len(value) != 7:
      return False

    for l in value:
      if l not in ['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
        return False

    return True

  if key == 'ecl':
    valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return value in valid

  if key == 'pid':
    if len(value) != 9:
      return False

    try: 
        int(value)
        return True
    except ValueError:
        return False


result = 0
for key, passport in passports.items():
  #print(list(passport.keys()))
  is_valid = True
  if all(fields in passport for fields in required_fields):
    for field, value in passport.items():
      #print(field, value)
      if validate(field, value) == False:
        is_valid = False
    if is_valid:
      result += 1

print(result)

# print(validate('byr', '1996'))
# print(validate('byr', '1800'))
# print(validate('iyr', '2015'))
# print(validate('iyr', '2030'))
# print(validate('eyr', '2022'))
# print(validate('eyr', '20020'))
# print(validate('hgt', '160cm'))
# print(validate('hgt', '130in'))
# print(validate('hcl', '#abc123'))
# print(validate('hcl', '#abch99'))
# print(validate('ecl', 'amb'))
# print(validate('ecl', 'nope'))
# print(validate('pid', '000045678'))
# print(validate('pid', '0102030405'))




