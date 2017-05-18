data1 = 'パトカー'
data2 = 'タクシー'
ans = ''
for i in range(len(data1)):
    ans += data1[i] + data2[i]
print(ans)

ans2 = ''
for i, j in zip(data1, data2):
    ans2 += i + j
print(ans2)
