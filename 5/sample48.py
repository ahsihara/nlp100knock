import sample41

def path_to_root(_chunk: sample41.Chunk, _sentence):
    if _chunk.dst == -1:
        return [_chunk]
    else:
        root = [_chunk] + path_to_root(_sentence[_chunk.dst], _sentence)
        return root


def join_chunks_by_arrow(_chunks):
    arrow = ' -> '.join([c.join_morphs() for c in _chunks])
    return arrow


if __name__ == '__main__':
    chunkeds = sample41.list('neko.txt.cabocha')
    for sentence in chunkeds[0:10]:
        for chunk in sentence:
            if chunk.has_noun():
                print(join_chunks_by_arrow(path_to_root(chunk, sentence)))