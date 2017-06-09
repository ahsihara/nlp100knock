import sample30
from pprint import pprint


def check(lis):
    kadai = []
    words = ''
    n = 0
    for line in lis:
        if line['pos1'].find('名詞') >= 0:
            words += line['pos']
            n += 1
        elif (line['pos1'] == '記号-句点') | (line['pos1'].find('名詞') == -1):
            if n >= 2:
                kadai.append(words)
            words = ''
            n = 0

    return kadai


lis = sample30.open_text()
kadai = check(lis)

pprint(kadai[0:10:])