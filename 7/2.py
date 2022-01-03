import math

crab_position = []
left_most = math.inf
right_most = -math.inf
with open('./7/input', 'r') as f:
    for pos in map(int, f.readline().split(',')):
        left_most = min(left_most, pos)
        right_most = max(right_most, pos)
        crab_position.append(pos)

min_val = math.inf
min_pos = None

for check in range(left_most, right_most+1):
    test = 0
    for val in crab_position:
        n = abs(check-val)
        test += (n*(n+1)/2)

    if test < min_val:
        min_val = test
        min_pos = check

print(min_val)
print(min_pos)
