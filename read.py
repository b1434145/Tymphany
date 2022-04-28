lines = []
with open('0_80.fcf') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(float(line))