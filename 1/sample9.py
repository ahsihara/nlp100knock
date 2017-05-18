import random

data = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
data2 = data.split()
ans = ''

def shaffl(data):
    s = list(data)
    random.shuffle(s)
    t = ''
    for i in range(len(s)):
        t = t + s[i]
    return  t

for i in range(len(data2)):
    if len(data2[i]) <= 4:
        ans = ans + data2[i]
    else:
        a, b = data2[i][0], data2[i][-1]
        c = data2[i][1:-1]
        d = shaffl(c)
        ans = ans + a + d + b
    ans = ans + ' '

print(data)
print(ans)
