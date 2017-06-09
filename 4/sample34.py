import sample30
import ngram
from pprint import pprint

def ngramed(lis):
    n = 3
    index = ngram.NGram(N=n)

    ngram_returm = []
    for term in index.ngrams(lis):
        ngram_returm.append(term)

    return ngram_returm


lis = sample30.open_text()
kadai = []
ngram_lis = ngramed(lis)
'''
for words in ngram_lis:
    if (type(words) == list) and (len(words) == 3) and \
           (words[0]['pos1'].find('名詞') == 0) and \
           (words[1]['surface'] == 'の') and \
           (words[2]['pos1'].find('名詞') == 0):
        kadai.append(words[0]['surface']+words[1]['surface']+words[2]['surface'])

pprint(kadai[0:10:])
'''
pprint(ngram_lis)