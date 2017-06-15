
import corenlp
from sample50 import kadai50
from pprint import pprint

corenlp_dir = "/home/ashihara/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

def make_word_list():
    kadai = kadai50()
    word_list = []
    for j in range(len(kadai)):
        word_list.append([])
        for i in parser.raw_parse(kadai[j])["sentences"][0]["words"]:
            if i[0] != '.':
                word_list[j].append(i[0])
            else:
                #記入するときだけ
                #word_list[j].append('.')
                word_list[j].append('')
    return word_list

if __name__ == '__main__':
    word_list = make_word_list()
    '''
    with open('output.txt', 'w') as f:
        for i in range(len(word_list)):
            f.write(' '.join(word_list[i]))
            f.write('\n')
            if i == 11:
                f.write('.')
                f.write('\n')
    '''

    pprint(word_list)

