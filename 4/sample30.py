from pprint import pprint

def make_dict(line):
    elements = line.split()
    if 0 < len(elements) < 4:
        return {'surface': elements[0], 'base': '', 'pos': '', 'pos1': ''}
    else:
        return {'surface': elements[0], 'base': elements[1], 'pos': elements[2], 'pos1': elements[3]}


def make_sentence(morphemes):
    sentences = []
    sentence = []

    for morpheme in morphemes:
        sentence.append(morpheme)
        if morpheme['pos1'] == '記号-句点':
            sentences.append(sentence)
            sentence = []

    return sentences

def open_text():
    lis = []
    with open('neko.txt.mecab') as f:
        for line in f:
            lis.append(make_dict(line))
    return lis

if __name__ == '__main__':
    lis = open_text()
    sentences = make_sentence(lis)

    # 結果の確認
    #pprint(lis[0:2:])
    print()
    pprint(sentences[0:2:])
