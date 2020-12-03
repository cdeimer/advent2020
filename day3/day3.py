grid = []
with open('day3', 'r') as f:
  for line in f:
    grid.append(line.strip())

right = 3
down = 1

x = 0
y = 0
trees = 0

while y < len(grid) - 1:
  x = (x + right) % (len(grid[0]))
  y += down
  if grid[y][x] == '#':
    trees += 1

print(trees)

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
treeproduct = 1

for slope in slopes:
  right, down = slope
  x = 0
  y = 0
  trees = 0

  while y < len(grid) - 1:
    x = (x + right) % (len(grid[0]))
    y += down
    if grid[y][x] == '#':
      trees += 1

  treeproduct = treeproduct * trees
  print(treeproduct)

