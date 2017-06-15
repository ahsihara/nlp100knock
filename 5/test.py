
a = [[1,2]]
b = []
b.extend(a)
b.extend([*a])
print(b)

def f(a, b, *c):
    x = []
    x.append([a,b,*c])
    print(a, b, c)
    print(x)


f(1,2,3,4,5,6)

a = [[1,2], 2, [1,4,5,6], [1,5]]
c = [1,4,5,6]
b = [1,4]
print(c in a)

a = set(['1','2','3','4','5','6'])
b = set([])
print(list(a & b))

a = list(a)
a = [1,2,3,4,5,6,7]
print(a)
print(a[2:])