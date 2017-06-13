import re

with open('nlp.txt.xml') as f:
    line = f.readline()

    while line:
        word = re.search("<word>(.*?)</word>", line)
        ner = re.search("<NER>(.*?)</NER>", line)
        if word:
            candidate = word.group(1)
        try:
            if ner.group(1) == 'PERSON':
                print(candidate)
        except:
            pass
        line = f.readline()