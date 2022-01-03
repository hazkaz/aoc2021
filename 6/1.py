from collections import defaultdict

fishies = [0]*9
step = []

with open('./6/input') as f:
    for x in f.readline().split(','):
        fishies[int(x)] += 1

print(fishies)
count = 0
for _ in range(256):
    step = [0]*9
    for idx, f in enumerate(fishies):
        if idx == 0:
            step[8] = fishies[0]
            step[6] = fishies[0]
        else:
            step[idx-1] += fishies[idx]

    fishies = step
    # print(sum(v for k, v in fishies.items()))
    # print(fishies)

print(sum(fishies))
