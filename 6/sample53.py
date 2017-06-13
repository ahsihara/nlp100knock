import re

with open('nlp.txt.xml') as f:
    line = f.readline()
    while line:
        word = re.search("<word>(.*?)</word>", line)
        if word:
            print(word.group(1))
        line = f.readline()