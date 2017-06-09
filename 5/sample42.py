from sample41 import list
from pprint import pprint

def is_valid_chunk(_chunk, sentence):
    return _chunk.join_morphs() != '' and _chunk.dst > -1 and sentence[_chunk.dst].join_morphs() != ''

def make_paired(chunkeds):
    paired_sentences = []
    for sentence in chunkeds:
        if len(sentence) > 1:
            paired_sentences.append([])
            for chunk in sentence:
                if is_valid_chunk(chunk, sentence):
                    paired_sentences[-1].append(chunk.pair(sentence))
    return paired_sentences

if __name__ == '__main__':
    chunkeds = list('neko.txt.cabocha')
    paired_sentences = make_paired(chunkeds)
    for i in range(10):
        print('\t'.join(paired_sentences[i]))
