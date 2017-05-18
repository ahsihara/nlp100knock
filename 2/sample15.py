with open('hightemp.txt') as f:
    lines = f.readlines()
n = int(input())
len_lines = len(lines)
for i in range(n):
    print(lines[len_lines - n + i], end='')
