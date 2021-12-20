
count = 0
with open("./1/input") as f:
    prev_value = int(f.readline())
    for line in f:
        if int(line)>prev_value:
            count+=1
        prev_value = int(line)

print(count)
