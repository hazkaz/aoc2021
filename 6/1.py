fishies = []
step = []

with open('./6/input') as f:
    fishies = [(int(x), 0) for x in f.readline().split(',')]

for _ in range(256):
    step = []
    for f, cycle in fishies:
        if f == 0:
            step.append((6, cycle+1))
            step.append((8, 0))
        else:
            step.append((f-1, cycle+1))

    fishies = step

print(len(fishies))
