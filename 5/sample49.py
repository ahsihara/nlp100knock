import sample41
from sample48 import path_to_root, join_chunks_by_arrow

def noun_pairs(_sentence):
    from itertools import combinations
    _noun_chunks = [_chunk for _chunk in _sentence if _chunk.has_noun()]
    return list(combinations(_noun_chunks, 2))


def common_chunk(path_i, path_j):
    _chunk_k = None
    path_i = list(reversed(path_i))
    path_j = list(reversed(path_j))
    for idx, (c_i, c_j) in enumerate(zip(path_i, path_j)):
        if c_i.srcs != c_j.srcs:
            _chunk_k = path_i[idx - 1]
            break

    return _chunk_k

if __name__ == '__main__':
    chunkeds = sample41.list('neko.txt.cabocha')
    ans = []
    for sentence in chunkeds:
        n_pairs = noun_pairs(sentence)
        if len(n_pairs) == 0:
            continue

        for n_pair in n_pairs:
            chunk_i, chunk_j = n_pair

            chunk_i.replace_noun('X')
            chunk_j.replace_noun('Y')

            path_chunk_i_to_root = path_to_root(chunk_i, sentence)
            path_chunk_j_to_root = path_to_root(chunk_j, sentence)

            if chunk_j in path_chunk_i_to_root:
                idx_j = path_chunk_i_to_root.index(chunk_j)
            else:
                chunk_k = common_chunk(path_chunk_i_to_root, path_chunk_j_to_root)
                if chunk_k is None:
                    continue

                idx_k_i = path_chunk_i_to_root.index(chunk_k)
                idx_k_j = path_chunk_j_to_root.index(chunk_k)

                ans.append(' | '.join([join_chunks_by_arrow(path_chunk_i_to_root[0: idx_k_i]),
                                  join_chunks_by_arrow(path_chunk_j_to_root[0: idx_k_j]),
                                  chunk_k.join_morphs()]))

    for i in range(10):
        print(ans[i])