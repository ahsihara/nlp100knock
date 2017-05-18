with open('hightemp.txt') as f:
    lines = f.readlines()
n = int(input())
for i in range(n):
    print(lines[i], end='')
