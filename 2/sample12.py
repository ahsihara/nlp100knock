with open('hightemp.txt') as f:
    lines = f.readlines()

with open('col1.txt', 'w') as g:
    #g.writelines(lines[0])
    print(lines[0], file=g)
with open('col2.txt', 'w') as g:
    #g.writelines(lines[1])
    print(lines[1], file=g)