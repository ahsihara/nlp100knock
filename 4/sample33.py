
from pprint import pprint
import sample30

def kadai(morphemes):
    nouns_suru = []

    for morpheme in morphemes:
        if morpheme['pos1'] == '名詞-サ変接続':
            nouns_suru.append(morpheme['surface'])

    pprint(nouns_suru[0:10:])

lis = sample30.open_text()
kadai(lis)


