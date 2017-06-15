
import xml.etree.ElementTree as ET
import pydot
from graphviz import Digraph
from pprint import pprint

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
coreference = root.findall('document/sentences/sentence/dependencies[@type="collapsed-dependencies"]')

def make_graph(co_dependence):
    G = Digraph(format='png')
    G.attr('node', shape='circle')
    dep = co_dependence.findall('dep')
    for i in dep:
        governor = i.find('governor')

        dependent = i.find('dependent')
        a = governor.text
        b = dependent.text
        G.node(governor.get('idx'), a)
        G.node(dependent.get('idx'), b)
        G.edge(governor.get('idx'),dependent.get('idx'))
    G.render(view=True)

if __name__ == '__main__':
    n = 2 #何文目？
    make_graph(coreference[n-1])