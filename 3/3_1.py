sums = [0]*12
count = 0

with open("./3/input") as f:
    for line in f:
        for i in range(len(line)-1):
            sums[i]+=int(line[i])
        count+=1

gamma = ''
for value in sums:
    if value/float(count)>=0.5:
        gamma+='1'
    else:
        gamma+='0'

gamma = int(gamma,2)
epsilon = (2**12-1)-gamma

print(gamma)
print(epsilon)
print(bin(gamma))
print(bin(epsilon))
print((epsilon+gamma+1)/8)
print(epsilon*gamma)