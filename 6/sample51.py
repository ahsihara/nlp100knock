
import corenlp
from sample50 import kadai50
from pprint import pprint

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

def make_word_list():
    kadai = kadai50()
    word_list = []
    for j in range(len(kadai)):
        for i in parser.raw_parse(kadai[j])["sentences"][0]["words"]:
            if i[0] != '.':
                word_list.append(i[0])
            else:
                word_list.append('')
    return word_list


if __name__ == '__main__':
    word_list = make_word_list()
    for i in range(10):
        print(word_list[i])

