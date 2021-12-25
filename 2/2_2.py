horizontal,depth,aim=0,0,0

with open('./2/input') as f:
    for line in f:
        if "forward" in line:
            horizontal+= int(line[8:])
            depth+=aim*int(line[8:])
        elif "down" in line:
            aim+=int(line[5:])
        elif "up" in line:
            aim-=int(line[3:])
    
print(horizontal*depth)
