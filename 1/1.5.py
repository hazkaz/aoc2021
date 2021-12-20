import matplotlib.pyplot as plt
import numpy as np

values = []
sums = []
window_size = 1

with open('./1/input') as f:
    for line in f:
        values.append(int(line))

prev_sum = sum(values[:window_size])

sums.append(prev_sum/window_size)
sums.append(prev_sum/window_size)
count = 0
for idx, val in enumerate(values[window_size:], window_size):
    if val > values[idx-window_size]:
        count += 1
    prev_sum = prev_sum-values[idx-window_size]+val
    sums.append(prev_sum/window_size)

sums.append(prev_sum/window_size)

plt.plot(values)
plt.plot(sums,c='red')
plt.show()
