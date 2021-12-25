horizontal,depth=0,0

with open('./2/input') as f:
    for line in f:
        if "forward" in line:
            horizontal+= int(line[8:])
        elif "down" in line:
            depth+=int(line[5:])
        elif "up" in line:
            depth-=int(line[3:])
    
print(horizontal*depth)
