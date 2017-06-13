import re

with open('nlp.txt.xml') as f:
    line = f.readline()
    while line:
        word = re.search("<word>(.*?)</word>", line)
        lemma = re.search("<lemma>(.*?)</lemma>", line)
        pos = re.search("<POS>(.*?)</POS>", line)
        if word:
            print(word.group(1), end='\t')
        if lemma:
            print(lemma.group(1),end='\t')
        if pos:
            print(pos.group(1))

        line = f.readline()