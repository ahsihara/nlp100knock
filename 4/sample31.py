
from pprint import pprint
import sample30


def kadai(morphemes):
    verbs = []
    for morpheme in morphemes:
        if morpheme['pos1'].find('動詞') == 0:
            verbs.append(morpheme['surface'])

    pprint(verbs[0:10:])

lis = sample30.open_text()
kadai(lis)


