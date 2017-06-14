
import os
import subprocess
import xml.etree.ElementTree as ET
import pydot

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'


def parse_nlp():
    if not os.path.exists(fname_parsed):
        subprocess.run(
            'java -cp "/usr/local/lib/stanford-corenlp-full-2016-10-31/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' + fname + ' 2>parse.out',
            shell=True,
            check=True
        )


def graph_from_edges_ex(edge_list, directed=False):
    if directed:
        graph = pydot.Dot(graph_type='digraph')

    else:
        graph = pydot.Dot(graph_type='graph')

    for edge in edge_list:

        id1 = str(edge[0][0])
        label1 = str(edge[0][1])
        id2 = str(edge[1][0])
        label2 = str(edge[1][1])

        # ノード追加
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # エッジ追加
        graph.add_edge(pydot.Edge(id1, id2))

    return graph

parse_nlp()
root = ET.parse(fname_parsed)
count = 1
for sentence in root.iterfind('./document/sentences/sentence'):
    count += 1
    sent_id = int(sentence.get('id'))
    edges = []

    for dep in sentence.iterfind(
        './dependencies[@type="collapsed-dependencies"]/dep'
    ):

        if dep.get('type') != 'punct':

            govr = dep.find('./governor')
            dept = dep.find('./dependent')
            edges.append(
                ((govr.get('idx'), govr.text), (dept.get('idx'), dept.text))
            )

    if len(edges) > 0:
        graph = graph_from_edges_ex(edges, directed=True)
        graph.write_png('{}.png'.format(sent_id))

    if count == 5:
        break