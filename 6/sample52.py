
from stemming.porter2 import stem
from sample51 import make_word_list


if __name__ == '__main__':
    word_list = make_word_list()
    stem_list = []
    word_list2 = []
    for i in word_list:
        for j in i:
            word_list2.append(j)

    for i in word_list2:
        stem_list.append(stem(i))

    for i in range(10):
        print(word_list2[i], stem_list[i])
