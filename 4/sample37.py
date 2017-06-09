import sample30
from pprint import pprint
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = 'TakaoPGOthic'


def count_word(lis):
    dic = defaultdict(int)
    for line in lis:
        #pprint(line)
        dic[line['pos']] += 1

    return dic

lis = sample30.open_text()
kadai = count_word(lis)
kadai = sorted(kadai.items(), key=lambda x: x[1], reverse=True)
#pprint(kadai[0:10:])

x, y, word = [], [], []
for i in range(10):
    x.append(i+1)
    word.append(kadai[i][0])
    y.append(kadai[i][1])

plt.bar(x, y, align='center')
plt.xticks(x, word)
plt.title("頻度上位10語")
plt.show()
