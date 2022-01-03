import math

crab_position = []
with open('./7/input', 'r') as f:
    for pos in map(int, f.readline().split(',')):

        crab_position.append(pos)

min_val = math.inf

for check in crab_position:
    test = 0
    for val in crab_position:
        test += abs(check-val)

    min_val = min(min_val, test)

print(min_val)
