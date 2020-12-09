with open('day8', 'r') as f:
  instructions = [tuple(line.strip().split(' ')) for line in f]

#print(instructions[:10])

#part 1

def process(index, instructions, accumulator = 0):
  if index == len(instructions):
    print ('terminated: ' + str(accumulator))
    return
  op, num, visited = instructions[index]
  if visited == 0:
    instructions[index] = (op, num, 1)
    if op == 'nop':
      process(index + 1, instructions, accumulator)
    if op == 'jmp':
      process(index + num, instructions, accumulator)
    if op == 'acc':
      accumulator += num
      process(index + 1, instructions, accumulator)
  else:
    print(accumulator)
    return

def process_instructions(instructions):
  instructions_helper = [(x, int(y), 0) for (x, y) in instructions]
  return process(0, instructions_helper)


process_instructions(instructions)
process_instructions(instructions)
process_instructions(instructions)

#part 2

def swap(instruction):
  op, num = instruction
  if op == 'nop':
    return ('jmp', num)
  if op == 'jmp':
    return ('nop', num)
  return (op, num)

instructions_swapped = instructions
for x in range(len(instructions_swapped)):
  instructions_swapped[x] = swap(instructions_swapped[x])
  process_instructions(instructions_swapped)
  instructions_swapped[x] = swap(instructions_swapped[x])
