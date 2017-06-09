from sample41 import list

if __name__ == '__main__':
    chunkeds = list('neko.txt.cabocha')

    for sentence in chunkeds:
        for chunk in sentence:
            if chunk.has_noun() and chunk.dst > -1 and sentence[chunk.dst].has_verb():
                print(chunk.pair(sentence))
