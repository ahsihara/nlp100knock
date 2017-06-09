
import corenlp
from sample50 import kadai50

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

if __name__ == '__main__':
    kadai = kadai50()
    for j in range(len(kadai)):
        for i in parser.raw_parse(kadai[j])["sentences"][0]["words"]:
            if i[0] != '.':
                print(i[0])
            else:
                print('')

