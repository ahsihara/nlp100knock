import re  # 正規表現で置き換え
from stemming.porter2 import stem
from sample51 import make_word_list


if __name__ == '__main__':
    word_list = make_word_list()
    stem_list = []
    for i in range(len(word_list)):
        stem_list.append(stem(word_list[i]))

    for i in range(10):
        print(word_list[i], stem_list[i])

