from collections import defaultdict

ans = defaultdict(int)

with open('hightemp.txt') as f:
    line = f.readlines()

for i in range(len(line)):
    ans[line[i].split()[0]] += 1

for i, j in sorted(ans.items(), key=lambda x: x[1], reverse=True):
    print(i, j)
