
import xml.etree.ElementTree as ET
from pprint import pprint

tree = ET.parse('nlp.txt.xml')
root = tree.getroot()
parse_nnp = root.findall('document/sentences/sentence/parse')

def search_NNP(parse):
    parse = parse.text.replace('(', '( ')
    parse = parse.replace(')', ' )')
    parse = parse.split()
    nnp_list = []
    for i in range(len(parse)):
        if parse[i] == 'NP':
            right, left = 0, 0
            for j in range(1, len(parse)):
                if parse[i + j] == '(':
                    left += 1
                elif parse[i + j] == ')':
                    right += 1
                if right > left:
                    nnp_list.append(' '.join(parse[i+1:i+j]))
                    break
    return nnp_list

def clean_print(nnp_list):
    delete_list = ['(', ')','NNPS', 'NNS', 'NNP', 'JJR', 'NN', 'NP', 'JJ',
                   'NNS', 'VP', 'JJ', 'CC', 'VBZ','DT', 'PP', 'S', 'VBN',
                   'IN', 'NNP', 'PRN', 'PRPS']
    for i in delete_list:
        nnp_list = nnp_list.replace(i, '')

    nnp_list = nnp_list.replace('-RRB- -RRB-', ')')
    nnp_list = nnp_list.replace('-LRB- -LRB-', '(')
    nnp_list = nnp_list.replace(', ,', ',')
    nnp_list = nnp_list.replace('RB', '')
    nnp_list = nnp_list.split()

    print(' '.join(nnp_list))

if __name__ == '__main__':
    for i in parse_nnp:
        nnp_list = search_NNP(i)
        for j in nnp_list:
            clean_print(j)
