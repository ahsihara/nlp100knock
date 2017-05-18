x, y, z = '12', '気温', '22.4'
def f(x, y, z):
    print(x + '時の' + y + 'は' + z)
    print('%s時の%sは%s' % (x, y, z))
f(x, y, z)