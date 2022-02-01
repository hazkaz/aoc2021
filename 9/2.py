
from functools import reduce


depth = []
grad = []
with open('./9/input') as f:
    for line in f:
        vals = list(map(int, line.strip()))
        depth.append(vals)
        grad.append([0]*len(vals))

lowest = []
rows = len(depth)
cols = len(depth[0])

for i, y in enumerate(depth):
    for j, x in enumerate(y):
        # if (i == rows-1 and j == cols-1) or (i == 0 and j == cols-1) or (i == 0 and j == 0) or (i == rows-1 and j == 0):
        #     grad[i][j] += 2
        # elif i == rows-1 or j == cols-1 or i == 0 or j == 0:
        #     grad[i][j] += 1

        if i < rows-1 and depth[i+1][j] > x:
            grad[i][j] += 1
        if j < cols-1 and depth[i][j+1] > x:
            grad[i][j] += 1
        if i < rows-1 and depth[i+1][j] < x:
            grad[i+1][j] += 1
        if j < cols-1 and depth[i][j+1] < x:
            grad[i][j+1] += 1

        if x == 9:
            grad[i][j] = -1

for i, y in enumerate(grad):
    for j, x in enumerate(y):
        if x == 4:
            print('\033[91m'+'4\t'+'\033[0m', end='')
        else:
            print(x, '\t', end='')
            pass

    print()

basins = []
for i, y in enumerate(grad):
    for j, x in enumerate(y):
        if x != -1:
            a, b = i, j
            test = set()
            q = [(i, j)]
            while(len(q) != 0):
                a, b = q.pop()
                test.add((a, b))
                grad[a][b] = -1
                if a+1 < rows and grad[a+1][b] != -1:
                    q.append((a+1, b))
                if b+1 < cols and grad[a][b+1] != -1:
                    q.append((a, b+1))
                if a-1 >= 0 and grad[a-1][b] != -1:
                    q.append((a-1, b))
                if b-1 >= 0 and grad[a][b-1] != -1:
                    q.append((a, b-1))
            if(len(test) != 0):
                basins.append(test)

basins.sort(key=lambda x: len(x), reverse=True)
print(reduce(lambda a, b: a*b, (len(b) for b in basins[:3])))
