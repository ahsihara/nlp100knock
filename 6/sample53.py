import re

WORD = re.compile(r"<word>(\w+)</word>")

with open('nlp.txt.xml', 'r') as f:
    for line in f:
        word = WORD.search(line.strip())
        if word:
            print(word.group(1))