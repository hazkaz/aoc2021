depth = []
grad = []
with open('./9/test') as f:
    for line in f:
        vals = list(map(int, line.strip()))
        depth.append(vals)
        grad.append([0]*len(vals))

lowest = []
rows = len(depth)
cols = len(depth[0])

for i, y in enumerate(depth):
    for j, x in enumerate(y):
        if (i == rows-1 and j == cols-1) or (i == 0 and j == cols-1) or (i == 0 and j == 0) or (i == rows-1 and j == 0):
            grad[i][j] += 2
        elif i == rows-1 or j == cols-1 or i == 0 or j == 0:
            grad[i][j] += 1

        if i < rows-1 and depth[i+1][j] > x:
            grad[i][j] += 1
        if j < cols-1 and depth[i][j+1] > x:
            grad[i][j] += 1
        if i < rows-1 and depth[i+1][j] < x:
            grad[i+1][j] += 1
        if j < cols-1 and depth[i][j+1] < x:
            grad[i][j+1] += 1

count = 0

for i, y in enumerate(grad):
    for j, x in enumerate(y):
        if x == 4:
            print('\033[91m'+'4  '+'\033[0m', end='')
            count += (1+depth[i][j])
        else:
            print(x, ' ', end='')
            pass

    print()

print(count)
