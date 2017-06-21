import corenlp
from pprint import pprint

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

text = 'pops a question'

for i in parser.raw_parse(text)["sentences"][0]["words"]:
    #word_list.append(i[1]['Lemma'])
    print(i[1]['Lemma'], i)

print()
pprint(parser.raw_parse(text))