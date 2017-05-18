with open('hightemp.txt') as fin:
    for line in fin:
        new_lines = line.strip().replace('    ', ' ')
        print(new_lines)
#lines = lines.strip().replace('\t', ' ')
#print(lines)