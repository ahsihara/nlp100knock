import codecs
#codecs.open('.txt', 'r', 'utf-8')

with codecs.open('col1.txt', 'r', 'utf-8') as f, codecs.open('col2.txt', 'r', 'utf-8') as g:
    lines1 = f.readlines()
    lines2 = g.readlines()

with codecs.open('merge.txt', 'w', 'utf-8') as h:
    for col1, col2 in zip(lines1, lines2):
        h.write('\t'.join([col1.rstrip(), col2]))
