length = 12
def get_gamma(test):
    sums = [0]*length
    count = 0
    for number in test:
        for idx,digit in enumerate(number[2:]):
            sums[idx]+=int(digit)
        count+=1

    gamma = 0
    for c in sums:
        gamma*=2
        gamma+= 1 if c/count>=0.5 else 0

    return format(gamma,f"#0{length+2}b")
        
def get_bin(num):
    return format(num,f"#0{length+2}b")

data = []

with open('./3/input') as f:
    for line in f:
        data.append('0b'+line.strip())

valid = data[:]

for position in range(length):
    gamma = get_gamma(valid)    
    temp=[]
    for num in valid:
        if num[position+2] == gamma[position+2]:
            temp.append(num)

    valid = temp
    if len(valid)==1:
        break

oxygen = valid[0]

valid = data[:]

for position in range(length):
    gamma = get_gamma(valid)    
    temp=[]
    for num in valid:
        if num[position+2] != gamma[position+2]:
            temp.append(num)

    valid = temp
    if len(valid)==1:
        break

co2 = valid[0]
oxygen = int(oxygen,2)
co2 = int(co2,2)

print(oxygen*co2)