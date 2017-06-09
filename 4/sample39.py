import sample30
from pprint import pprint
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = 'TakaoPGOthic'


def count_word(lis):
    dic = defaultdict(int)
    for line in lis:
        dic[line['pos']] += 1

    return dic

def count_count(dic):
    dic_count = defaultdict(int)
    dic2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(dic)):
        dic_count[dic2[i][1]] += 1

    return dic_count

lis = sample30.open_text()
dic = count_word(lis)
kadai = count_count(dic)
kadai = sorted(kadai.items(), key=lambda x: x[1], reverse=True)
#pprint(kadai[0:10:])

x, y, word = [], [], []
for i in range(len(kadai)):
    x.append(i+1)
    #word.append(kadai[i][0])
    y.append(kadai[i][1])
plt.xscale("log")
plt.yscale("log")
plt.plot(x, y)
plt.title("Zipf")
plt.show()


