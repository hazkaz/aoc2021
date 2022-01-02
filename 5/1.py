max_x, max_y = 0, 0
segments = []
with open('./5/input') as f:
    for line in f:
        (x1, y1), (x2, y2), *_ = [map(int, a.split(','))
                                  for a in line.split('->')]
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
        segments.append(((x1, y1), (x2, y2)))

max_x+=1
max_y+=1
data = [[0]*(max_x) for _ in range(max_y)]

for s in segments:
    x_delta = s[1][0]-s[0][0]
    y_delta = s[1][1]-s[0][1]
    max_delta = max(abs(x_delta), abs(y_delta))
    x_d = int(x_delta/max_delta)
    y_d = int(y_delta/max_delta)
    x = s[0][0]
    y = s[0][1]
    if x_delta == 0 or y_delta == 0:
        while not (x == s[1][0] and y == s[1][1]):
            data[y][x] += 1
            x += x_d
            y += y_d
        data[y][x] += 1

count = 0

for i in range(max_x):
    for j in range(max_y):
        if data[i][j] > 1:
            count += 1

# print(data)
print(count)
