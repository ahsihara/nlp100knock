import sys
with open('hightemp.txt') as f:
    lines = f.readlines()

n = int(input())
#n = int(sys.argv[1])

len_lines = len(lines)
gyo = int(len_lines / n)
amari = len_lines % n
#a = []
for i in range(n):
    for j in range(gyo):
        print(lines[0],end='')
        lines.pop(0)
    if i < amari:
        print(lines[0], end='')
        #a.append(lines[0])
        lines.pop(0)
    print()
#print(a)