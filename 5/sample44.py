from sample41 import list
from sample42 import make_paired
import pydotplus

def sentence_to_dot(idx, sentence):
    head = "digraph sentence{} ".format(idx)
    body_head = "{ graph [rankdir = LR]; "
    body_list = ['"{}"->"{}"; '.format(*chunk_pair.split()) for chunk_pair in sentence]

    return head + body_head + ''.join(body_list) + '}'
'''
def sentence_to_dot2(sentence, data):
    sentence = sentence.split('\t')
    for i in sentence:
        if i not in data:
            data.updata(i:len(data))
    return data
'''
def sentences_to_dots(sentences):
    _dots = []
    #data = {}
    for idx, sentence in enumerate(sentences):
        #print(idx , sentence)
        #data = sentence_to_dot(sentence, data)

        _dots.append(sentence_to_dot(idx, sentence))
    return _dots


def save_graph(dot, file_name):
    g = pydotplus.graph_from_dot_data(dot)
    g.write_jpeg(file_name, prog='dot')

if __name__ == '__main__':
    chunkeds = list('neko.txt.cabocha')
    paired_sentences = make_paired(chunkeds)
    dots = sentences_to_dots(paired_sentences)

    for idx in range(1):
        save_graph(dots[idx], 'graph.jpg')

    #print(dots[0])
    #print(dots[0][0])


    '''
    from graphviz import Digraph

    # formatはpngを指定(他にはPDF, PNG, SVGなどが指定可)
    G = Digraph(format='png')
    G.attr('node', shape='square')

    N = 15  # ノード数

    # ノードの追加
    for i in range(N):
        G.node(str(i), str(i + 1))

    # 辺の追加
    for i in range(N):
        if (i - 1) // 2 >= 0:
            G.edge(str((i - 1) // 2), str(i))

    # print()するとdot形式で出力される
    print(G)

    # binary_tree.pngで保存
    G.render('binary_tree')
    '''