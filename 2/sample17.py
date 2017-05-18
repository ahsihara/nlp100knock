with open('hightemp.txt') as f:
    lines = f.readlines()
lis = []
for i in range(len(lines)):
    a = lines[i].split()
    lis.append(a[0])
lis = set(lis)
print(lis)
'''
for i in range(len(lis)):
    print(lis[i])
'''