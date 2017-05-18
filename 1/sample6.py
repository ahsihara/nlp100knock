#import sample5

data1 = 'paraparaparadise'
data2 = 'paragraph'

def check(x, y):
    global ans1, ans2, ans3
    ans1, ans2, ans3 = [], [], []
    ans1.extend(x)
    ans3.extend(x)

    for i in range(len(y)):
        if y[i] not in x:
            ans1.append(y[i])
        if y[i] in x:
            ans2.append(y[i])
            ans3.remove(y[i])
    print('sum is',ans1)
    print('product is',ans2)
    print('difference is',ans3)


def ngram(text1, text2, n):
    x, y = [], []

    for i in range(len(text1) - n + 1):
        a = ''
        for j in range(n):
            a = a + text1[i+j]
        x.append(a)
    x_ans = list(set(x))
    print('X is',x_ans)

    for i in range(len(text2) - n + 1):
        a = ''
        for j in range(n):
            a = a + text2[i+j]
        y.append(a)
    y_ans = list(set(y))
    print('y is',y_ans)

    check(x_ans, y_ans)
    word = 'se'
    if word in x_ans:
        print('\'se\' in x')
    else:
        print('\'se\' not in x')
    if word in y_ans:
        print('\'se\' in y')
    else:
        print('\'se\' not in y')

ngram(data1, data2, 2)

