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
        # 名詞句ペアのリスト
        n_pairs = noun_pairs(sentence)
        if len(n_pairs) == 0:
            continue

        for n_pair in n_pairs:
            chunk_i, chunk_j = n_pair

            # 文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
            chunk_i.replace_noun('X')
            chunk_j.replace_noun('Y')

            # 文節iとjからrootへのパス(Chunk型のlist)
            path_chunk_i_to_root = path_to_root(chunk_i, sentence)
            path_chunk_j_to_root = path_to_root(chunk_j, sentence)

            if chunk_j in path_chunk_i_to_root:
                # 文節iから構文木の根に至る経路上に文節jが存在する場合

                # 文節jの文節iから構文木の根に至る経路上におけるインデックス
                idx_j = path_chunk_i_to_root.index(chunk_j)

                # 文節iから文節jのパスを表示
                #print(join_chunks_by_arrow(path_chunk_i_to_root[0: idx_j + 1]))
            else:
                # 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合

                # 文節kを取得
                chunk_k = common_chunk(path_chunk_i_to_root, path_chunk_j_to_root)
                if chunk_k is None:
                    continue

                # 文節kの文節iから構文木の根に至る経路上におけるインデックス
                idx_k_i = path_chunk_i_to_root.index(chunk_k)

                # 文節kの文節jから構文木の根に至る経路上におけるインデックス
                idx_k_j = path_chunk_j_to_root.index(chunk_k)

                # 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
                '''                print(' | '.join([join_chunks_by_arrow(path_chunk_i_to_root[0: idx_k_i]),
                                  join_chunks_by_arrow(path_chunk_j_to_root[0: idx_k_j]),
                                  chunk_k.join_morphs()]))
                '''
                ans.append(' | '.join([join_chunks_by_arrow(path_chunk_i_to_root[0: idx_k_i]),
                                  join_chunks_by_arrow(path_chunk_j_to_root[0: idx_k_j]),
                                  chunk_k.join_morphs()]))

    for i in range(10):
        print(ans[i])