
with open('hightemp.txt') as f:
    lines = f.readlines()

ans = sorted(lines, key=lambda x: x.strip().split()[2], reverse=True)
for i in range(len(ans)):
    print(ans[i],end='')