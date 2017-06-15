
import xml.etree.ElementTree as ET
from pprint import pprint

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
coreference = root.findall('document/coreference/coreference')

#[置き換え単語, 何文目, 開始単語位置, 終了単語位置]
def make_coreference():
    coreference_list = []
    for i in coreference:
        sentence_num = i.findall('mention/sentence')
        start_num = i.findall('mention/start')
        end_num = i.findall('mention/end')

        coreference_list.append([' '.join(word_list[int(sentence_num[0].text)-1][int(start_num[0].text)-1:int(end_num[0].text)-1])])
        for  j in range(1, len(sentence_num)):
            coreference_list[-1].append([int(sentence_num[j].text)-1, int(start_num[j].text)-1, int(end_num[j].text)-1])

    return coreference_list

#その単語を開始位置とする共参照表現はあるか調べる
def check_co(sentence, start):
    #flg = 0
    #flg_list = []
    for i in range(len(coreference_list)):
        for j in range(1, len(coreference_list[i])):
            if sentence == coreference_list[i][j][0] and start == coreference_list[i][j][1]:
                return [coreference_list[i][0], coreference_list[i][j][2]]
    return 0

def print_ans():
    i, j = 0, 0
    while i < len(word_list):
        j = 0
        while j < len(word_list[i]):
            flg = check_co(i, j)

            if flg != 0:
                print('[', end=' ')
                while j != flg[1]:
                    print(word_list[i][j], end=' ')
                    j += 1
                print('({})'.format(flg[0]), ']', end=' ')
            if j >= len(word_list[i]):
                break
            print(word_list[i][j],end=' ')

            j += 1
        print('\n')
        i += 1



if __name__ == "__main__":

    word_list = []
    with open('output.txt') as f:
        line = f.readline()
        while line:
            line = line.replace('-RRB-', ')')
            line = line.replace('-LRB-', '(')
            word_list.append(line.split())
            line = f.readline()

    coreference_list = make_coreference()
    #pprint(coreference_list)
    print_ans()

