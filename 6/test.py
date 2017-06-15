with open('output.txt') as f:
    content = []
    line = f.readline()
    while line:
        content.append(line)
        line = f.readline()

    print(len(content[25]))
    print(content[12])