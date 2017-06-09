import sample30
from pprint import pprint
from collections import defaultdict


def count_word(lis):
    dic = defaultdict(int)
    for line in lis:
        #pprint(line)
        dic[line['pos']] += 1

    return dic

lis = sample30.open_text()
kadai = count_word(lis)
kadai = sorted(kadai.items(), key=lambda x: x[1], reverse=True)
pprint(kadai[0:10:])
