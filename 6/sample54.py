import pprint
import json
import corenlp

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"

parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

with open('easy_text.txt', encoding='utf-8') as NLP:
    count = 0
    for line in NLP:
        # XMLで取り出すことは諦めた
        for i in parser.raw_parse(line)["sentences"][0]["words"]:
            print(i)
